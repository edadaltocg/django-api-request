import requests
from django.shortcuts import render
from .models import Message


# Create your views here.
def index(request):  # index view
    # url for api GET request with {} customizable fields
    API_KEY = 'examplekey'
    url = 'http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'
    field = 'example'

    # Get response (json format)
    r = requests.get(url.format(field, API_KEY)).json()
    # Print response
    print(r)

    # Get important data template
    formatted_response = {
        'message': r['message'],
        'cod': r['cod'],
    }

    # Query data from the database/ populate db with api calls
    ms = Message.objects.all()
    data = []
    for m in ms:
        r = requests.get(url.format(field, API_KEY)).json()
        formatted_response = {
            'message': r['message'],
            'db': m.message,
        }
        data.append(formatted_response)
    print(data)

    # Pass the data to the view based on a context
    context = {
        'res': data,
    }

    return render(request, 'myApp/index.html', context)
