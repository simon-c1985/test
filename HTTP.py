# import requests
#
# url = 'https://www.google.ru/'
# response = requests.get(url)
# print(f'Request to {url}. Status code is {response.status_code}')
# print(response.text)

import requests

# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'

# parametr = {
#     'format': 'geojson',
#     'starttime': '2019-01-01',
#     'endtime': '2019-02-01',
#     'latitude': '51.51',
#     'longitude': '-0.12',
#     'maxradiuskm': '2000'
# }

# response = requests.get(url, headers={'Accept': 'application/json'}, params=parametr)

# print(response.json())

# data = response.json()
# print(data["features"][1]["properties"]["place"])


def get_requests():
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    parametr = {'format': 'geojson',
                'starttime': input('Input Start time (2019-01-01): ') or '2019-01-01',
                'endtime': input('Input End time (2019-02-01): ') or '2019-02-01',
                'latitude': input('Input Latitude (51.51): ') or '51.51',
                'longitude': input('Input Longitude (-0.12): ') or '-0.12',
                'maxradiuskm': input('Input End time (2000): ') or '2000',
                'minmagnitude': input('Input Minimal magnitude (2): ') or '2'
                }
    response = requests.get(url, headers={'Accept': 'application/json'}, params=parametr)
    data = response.json()
    i = 0
    # while data["features"][i]:
    #     print(data["features"][i]["properties"]["place"], data["features"][i]["properties"]["mag"])
    #     i += 1
    i = 0
    for dat in data["features"]:
        print(f'{i + 1}. Place: {dat["properties"]["place"]}. Magnitude: {dat["properties"]["mag"]}')
        i += 1


get_requests()
