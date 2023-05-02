from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    pass
    return render(request, 'index.html',locals())


def web_bing(query):
    url = f"https://www.bing.com/search?q={query}&setlang=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    search_results = soup.find_all("li", class_="b_algo")
    results = []
    for result in search_results:
        title = result.find("h2").text
        url = result.find("a")["href"]
        snippet = result.find("div", class_="b_caption").find("p").text
        results.append({"title": title, "url": url, "snippet": snippet})
    return results




def bing_images(query):
    image_url = f"https://www.bing.com/images/search?q={query}&setlang=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(image_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find_all("div", class_="imgpt")

    # Create an empty list to store the image links
    links = []

    # Loop through the search results and get the src attribute of each img tag
    for result in search_results:
        img = result.find("img")
        if img:
            # Use a try-except block to handle the KeyError
            try:
                link = img["src"]
                # Append the link to the list
                links.append(link)
            except KeyError:
                # Skip the tag if it does not have a src attribute
                pass
    return links


def bing_news(query):
    url = f"https://www.bing.com/news/search?q={query}&setlang=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_cards = soup.find_all("div", class_="news-card")
    news_list = []
    for card in news_cards:
        title = card.find("a", class_="title").text
        link = card.find("a", class_="title")["href"]
        news_list.append({'title': title, 'link': link})
    return news_list



def bing_video(query):
    url = f"https://www.bing.com/videos/search?q={query}&setlang=en"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all video results
    video_results = soup.find_all('div', {'class': 'dg_u'})

    # extract the aria-label and href attributes for each a tag inside the class="mc_vtvc"
    results = []
    for video in video_results:
        mc_vtvc_div = video.find('div', {'class': 'mc_vtvc'})
        a_tags = mc_vtvc_div.find_all('a')

        for a_tag in a_tags:
            aria_label = a_tag.get('aria-label', '')
            url = a_tag.get('href', '')

            results.append({'aria_label': aria_label, 'url': url})

    return results



def get_news(query):
    url = f"https://www.google.com/search?q={query}&tbm=nws"

    # Set the headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    news_div = soup.find('div', class_='MjjYud')

    news_list = []
    # Loop through all the news articles and add their details to the list
    for article in news_div.find_all('div', class_='SoaBEf'):
        headline = article.find('div', class_='vJOb1e').get_text()
        link = article.find('a')['href']
        news_dict = {'headline': headline, 'link': link}
        news_list.append(news_dict)

    return news_list


def get_video_results(query):
    url = f"https://www.google.com/search?q={query}&tbm=vid"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    video_links = soup.find_all("div", class_="DhN8Cf")

    results = []
    for link in video_links:
        href_link = link.a['href']
        title = link.h3.text
        results.append({'link': href_link, 'title': title})

    return results



def google_search_images(query, search_type='web'):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": 'AIzaSyDxBnA4Wwhh1sH3gFOZ2nQl_smU3uO3BBA',
        "cx": "c772d9b1605014105",
        "searchType": search_type,
    }
    response = requests.get(url, params=params)
    return response.json()


def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": 'AIzaSyDxBnA4Wwhh1sH3gFOZ2nQl_smU3uO3BBA',
        "cx": "c772d9b1605014105",
    }
    response = requests.get(url, params=params)
    return response.json()


def search(request):
    query = request.GET.get('q')

    #Google
    result = google_search(query)
    items = result["items"]
    total_results = result["searchInformation"]["totalResults"]

    #images
    # result_images = google_search_images(query, search_type="image")
    # images_items = result_images.get("items", [])
    # image_urls = [item.get("link", "") for item in images_items]

    # #news
    # news_list = get_news(query)

    # #videos
    # video_results = get_video_results(query)


    #Bing
    bing_result_web = web_bing(query)
    # bing_result_images = bing_images(query)
    # bing_news_list = bing_news(query)
    # bing_video_list    = bing_video(query)


    return render(request, 'search.html', locals())


def google_images_search(request,query):

    #images
    result_images = google_search_images(query, search_type="image")
    images_items = result_images.get("items", [])
    image_urls = [item.get("link", "") for item in images_items]
    print("image_urls",image_urls)
    bing_result_images = bing_images(query)
    print("bing_result_images",bing_result_images)

    return render(request, 'google_images_search.html', locals())


def news(request,query):
    # news
    news_list = get_news(query)
    bing_news_list = bing_news(query)

    return render(request, 'news.html', locals())


def videos(request,query):
    #videos
    video_results = get_video_results(query)
    bing_video_list    = bing_video(query)
    return render(request, 'videos.html', locals())


#google search scrape :





#web
#
#
# import requests
# from bs4 import BeautifulSoup
#
# query = "web scraping with python"
# url = f"https://www.google.com/search?q={query}"
#
# # Set the headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
#
# # Send a GET request to the Google search results page
# response = requests.get(url, headers=headers)
#
# # Create a BeautifulSoup object
# soup = BeautifulSoup(response.content, "html.parser")
#
# # Find all search result links and titles
# search_results = soup.select(".yuRUbf a")
# for result in search_results:
#     link = result.get("href")
#     title = result.find("h3").get_text()
#     print("Link:", link)
#     print("Title:", title)
#
#
#
#
#
# #images
#
#
# import requests
# from bs4 import BeautifulSoup
#
# query = "apple"
# url = f"https://www.google.com/search?q={query}&tbm=isch"
#
# # Set the headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
#
# # Send a GET request to the Google Images search results page
# response = requests.get(url, headers=headers)
#
# # Create a BeautifulSoup object
# soup = BeautifulSoup(response.content, "html.parser")
#
# # Find all image URLs and display them
# image_links = soup.select(".rg_i")
# for link in image_links:
#     try:
#         image_url = link["data-src"]
#     except KeyError:
#         image_url = link["src"]
#     print("Image URL:", image_url)
#
#
#
# #news:
#
# import requests
# from bs4 import BeautifulSoup
#
# query = "apple"
# url = f"https://www.google.com/search?q={query}&tbm=nws"
#
# # Set the headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# news_div = soup.find('div', class_='MjjYud')
#
#
# # Loop through all the news articles and print their details
# for article in news_div.find_all('div', class_='SoaBEf'):
#     headline = article.find('div', class_='vJOb1e').get_text()
#     link = article.find('a')['href']
#     print("Headline and Link:", [headline, link])
#
#
#
#
#
#
#
# #videos :
#
#
#
# import requests
# from bs4 import BeautifulSoup
#
# query = "apple"
# url = f"https://www.google.com/search?q={query}&tbm=vid"
#
# # Set the headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
#
# # Send a GET request to the URL with headers
# response = requests.get(url, headers=headers)
#
# # Parse the HTML content of the response with BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")
#
# # Find all the links with class "DhN8Cf" inside the video section
# video_links = soup.find_all("div", class_="DhN8Cf")
#
# # Loop through the links and extract the href links and the text inside the h3 tag
# for link in video_links:
#     href_link = link.a['href']
#     title = link.h3.text
#     print(f"Link: {href_link}")
#     print(f"Title: {title}\n")
#
#
