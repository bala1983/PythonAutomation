import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url = url, params = params)

response_json = response.json()

list_of_photos = response_json.get('photos', [])

for index, element in enumerate(list_of_photos, start = 1):

    img_url = element['img_src']
    response = requests.get(url = img_url)

    file_name = f"mars_photo{index}.jpg"
    with open(file_name, 'wb') as file:
        file.write(response.content)