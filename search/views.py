from django.shortcuts import render
import requests


def index(request):
    pass


    return render(request, 'index.html',locals())

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
    result = google_search(query)
    items = result["items"]
    total_results = result["searchInformation"]["totalResults"]

    #images
    result_images = google_search_images(query, search_type="image")
    images_items = result_images.get("items", [])
    image_urls = [item.get("link", "") for item in images_items]


    return render(request, 'search.html', locals())
