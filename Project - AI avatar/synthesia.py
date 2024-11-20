import requests
import json

url = "https://api.synthesia.io/v2/videos"

payload = {
    "test": "true",
    "visibility": "private",
    "title": "MY 2ND VIDEO",
    "input": [
        {
            "avatarSettings": {
                "horizontalAlign": "center",
                "scale": 1,
                "style": "rectangular",
                "seamless": False
            },
            "backgroundSettings": { "videoSettings": {
                    "shortBackgroundContentMatchMode": "freeze",
                    "longBackgroundContentMatchMode": "trim"
                } },
            "scriptText": "I AM GOOD.",
            "avatar": "1706b274-9d21-4985-a558-35b3d6f704e4",
            "background": "green_screen"
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "a3a7f20e6e8aa1fd72d299c4f2559e7a"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
