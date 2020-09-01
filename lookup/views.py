from django.shortcuts import render


def home(request):
    import json
    import requests
    # http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Gwalior

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=5&API_KEY=7F276637-93A1-4CB9-9DC0-F21094BB712B")
        try:
            api = json.loads(api_requests.content)
            # print(api)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api, 'category_color': api[0]['Category']['Name'].replace(" ", "").lower()})

    else:
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=7F276637-93A1-4CB9-9DC0-F21094BB712B")

        # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=7F276637-93A1-4CB9-9DC0-F21094BB712B

        try:
            api = json.loads(api_requests.content)
            # print(api)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api, 'category_color': api[0]['Category']['Name'].replace(" ", "").lower()})


def about(request):
    return render(request, 'about.html', {})