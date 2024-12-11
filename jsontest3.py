import requests
import webbrowser

url = 'https://random.dog/woof.json'
response = requests.get(url)

if response.status_code == 200:
    dog_data = response.json()
    media_url = dog_data['url']

    # Check if the URL is a video or an image
    if media_url.endswith('.mp4'):
        print("Video URL:", media_url)
        # Open the video in the default web browser
        webbrowser.open(media_url)
    else:
        print("Image URL:", media_url)
        # If it's an image, you can display it using PIL
        from PIL import Image
        from io import BytesIO

        image_response = requests.get(media_url)
        if image_response.status_code == 200:
            img = Image.open(BytesIO(image_response.content))
            img.show()
        else:
            print(f"Error fetching image: {image_response.status_code}")
else:
    print(f"Error fetching data: {response.status_code}")
