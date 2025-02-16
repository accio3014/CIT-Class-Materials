import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from openai import OpenAI

client = OpenAI(api_key=api_key)
from google_auth_oauthlib.flow import InstalledAppFlow

# 유튜브 API 사용 권한 요청 스코프
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)

def get_youtube_captions(video_id):
    youtube = get_authenticated_service()
    request = youtube.captions().list(
        part='snippet',
        videoId=video_id
    )
    response = request.execute()

    for item in response.get('items', []):
        if item['snippet']['language'] == 'en':
            return item['id']
    return None

# 나머지 코드와 함께 사용하세요


def get_youtube_captions(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.captions().list(
        part='snippet',
        videoId=video_id
    )
    response = request.execute()

    for item in response.get('items', []):
        if item['snippet']['language'] == 'en':
            return item['id']
    return None

def download_captions(caption_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.captions().download(
        id=caption_id,
        tfmt='srt'
    )
    response = request.execute()
    return response

def summarize_text(api_key, text, model="text-davinci-003", max_tokens=150):
    prompt = f"Summarize this text:\n\n{text}"
    response = client.completions.create(engine=model,
    prompt=prompt,
    max_tokens=max_tokens)
    return response.choices[0].text.strip()

def main(video_url, youtube_api_key, openai_api_key):
    video_id = video_url.split("v=")[1]
    caption_id = get_youtube_captions(video_id, youtube_api_key)
    if caption_id:
        captions = download_captions(caption_id, youtube_api_key)
        summary = summarize_text(openai_api_key, captions)
        print("Summary:", summary)
    else:
        print("No captions available for this video.")

# Usage

# main(video_url, youtube_api_key, openai_api_key)
