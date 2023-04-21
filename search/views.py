from django.shortcuts import render
import requests


def index(request):
    pass
    return render(request, 'index.html')

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
    print(result)

    items = result["items"]
    total_results = result["searchInformation"]["totalResults"]
    searchTime = result["searchInformation"]["searchTime"]
    print("Total Results: ", total_results)
    print("searchTime : ", searchTime)

    for item in items:
        title = item["title"]
        link = item["link"]
        snippet = item["snippet"]

        print("Title: ", title)
        print(" Link: ", link)
        print("Snippet: ", snippet)
        print("\n")

    return render(request, 'search.html', locals())
