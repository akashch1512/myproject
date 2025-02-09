from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = "https://5b9d-2409-4081-178c-a2be-1c3-225b-67c0-4c3.ngrok-free.app/data"

    # Fetch the JSON response
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"pH Value: {data['pH']}")
        print(f"Turbidity: {data['turbidity']}")
    else:
        print("Failed to fetch data")

    data = {
        'ph' : data['pH'],
        'tur' : data['turbidity'],
    }

    return render(request, 'index.html', data)
