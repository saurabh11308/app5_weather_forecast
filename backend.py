import requests
API_KEY = "f914a30a25e0980f477c6786a25d19f8"


def get_data(city,days):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast"
                            f"?q={city}&appid={API_KEY}")
    response_j = response.json()
    days_data = response_j['list'][:days*8]
    temp_list = [day_data['main']['temp']/10 for day_data in days_data]
    print(response_j)


if __name__ == "__main__":
    get_data("Airoli",2)