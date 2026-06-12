import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = "https://vbps271-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
sentiment_analyzer_url = os.environ.get('sentiment_analyzer_url')


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"

    request_url = backend_url + endpoint

    print("DEBUG URL:", request_url)

    try:
        response = requests.get(request_url)
        print("DEBUG STATUS:", response.status_code)
        print("DEBUG RESPONSE:", response.text)

        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print("ERROR:", e)
        return []


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")