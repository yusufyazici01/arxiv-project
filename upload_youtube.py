import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from src.config import Config

def upload_to_youtube(video_path, title, description=""):
   
    youtube = build("youtube", "v3", developerKey=Config.YOUTUBE_API_KEY)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["arxiv", "short", "AI", "CS"],
                "categoryId": "28"  # 28 => Science & Technology
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )
    response = request.execute()
    print("Video uploaded:", response)
    return response
