from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=5&API_KEY=7F276637-93A1-4CB9-9DC0-F21094BB712B")

    else:
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=7F276637-93A1-4CB9-9DC0-F21094BB712B")

    try:
        api = json.loads(api_requests.content)
        category_color = api[0]['Category']['Name'].replace(" ", "").lower()
    except Exception as e:
        api = "Error..."
        category_color = 'No Output'

    return render(request, 'home.html', {'api': api, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})