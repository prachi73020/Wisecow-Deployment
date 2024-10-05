import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application is UP, Status Code: {response.status_code}")
        else:
            print(f"Application might be DOWN, Status Code: {response.status_code}")
    except requests.ConnectionError:
        print("Failed to connect to the application. Application is DOWN.")

check_application_status("http://your-app-url.com")
