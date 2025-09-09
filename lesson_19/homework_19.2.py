import os.path

import requests

url = "http://127.0.0.1:8080"
file_path = "cat.jpg"
print(os.path.exists(file_path))

with open(file_path, 'rb') as file:
    files = {'image': file}
    file_response = requests.post(f"{url}/upload", files=files)
    response_json = file_response.json()
    img_url = response_json['image_url']
print(file_response)
print(img_url)

with open("copy_cat.jpg", 'wb') as file:
    headers = {"Content-Type": "image"}
    response = requests.get(url=f"{url}/image/{file_path}", headers=headers)
    file.write(response.content)

response_delete = requests.delete(url=f"{url}/delete/{file_path}")
final_response = requests.get(url=f"{url}/image/{file_path}", headers={"Content-Type": "image"})