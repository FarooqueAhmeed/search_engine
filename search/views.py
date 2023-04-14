from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests



def index(request):
    pass
    return render(request, 'index.html')


from bs4 import BeautifulSoup

def search(request):
    query = request.GET.get('q')

    if query:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        data = response.json()
        print(data)
        # Extracting the values from the JSON response
        abstract = data['Abstract']
        abstract_source = data['AbstractSource']
        abstract_text = data['AbstractText']
        abstract_url = data['AbstractURL']
        answer = data['Answer']
        answer_type = data['AnswerType']
        definition = data['Definition']
        definition_source = data['DefinitionSource']
        definition_url = data['DefinitionURL']
        entity = data['Entity']
        heading = data['Heading']
        image = data['Image']
        image_height = data['ImageHeight']
        image_is_logo = data['ImageIsLogo']
        image_width = data['ImageWidth']
        infobox = data['Infobox']
        redirect = data['Redirect']
        related_topics = data['RelatedTopics']
        results = data['Results']
        result_type = data['Type']
        attribution = data['meta']['attribution']
        blockgroup = data['meta']['blockgroup']
        created_date = data['meta']['created_date']
        description = data['meta']['description']
        designer = data['meta']['designer']
        dev_date = data['meta']['dev_date']
        dev_milestone = data['meta']['dev_milestone']
        developer = data['meta']['developer']
        example_query = data['meta']['example_query']
        is_stackexchange = data['meta']['is_stackexchange']
        js_callback_name = data['meta']['js_callback_name']
        live_date = data['meta']['live_date']
        maintainer_github = data['meta']['maintainer']['github']
        name = data['meta']['name']
        perl_module = data['meta']['perl_module']
        producer = data['meta']['producer']
        production_state = data['meta']['production_state']
        repo = data['meta']['repo']
        signal_from = data['meta']['signal_from']
        src_domain = data['meta']['src_domain']
        src_id = data['meta']['src_id']
        src_name = data['meta']['src_name']
        src_options = data['meta']['src_options']
        src_url = data['meta']['src_url']
        status = data['meta']['status']
        tab = data['meta']['tab']
        topic = data['meta']['topic']
        unsafe = data['meta']['unsafe']


    else:

        # No query submitted, so set all variables to None

        abstract = None

        abstract_source = None

        abstract_text = None

        abstract_url = None

        answer = None

        answer_type = None

        definition = None

        definition_source = None

        definition_url = None

        entity = None

        heading = None

        image = None

        image_height = None

        image_is_logo = None

        image_width = None

        infobox = None

        redirect = None

        related_topics = None

        results = None

        result_type = None

        attribution = None

        blockgroup = None

        created_date = None

        description = None

        designer = None

        dev_date = None

        dev_milestone = None

        developer = None

        example_query = None

        is_stackexchange = None

        js_callback_name = None

        live_date = None

        maintainer_github = None

        name = None

        perl_module = None

    return render(request, 'search.html', locals())
