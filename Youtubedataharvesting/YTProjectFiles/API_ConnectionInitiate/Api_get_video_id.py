from googleapiclient.discovery import build
from YTProjectFiles.API_Key import *

filename = r"/Users/shashankkaundal/Downloads/Youtubedataharvesting/YTProjectFiles/API_Key/API_KEY.txt"
with open(filename,"rt") as f:
     text = f.readline()
api_key = text.strip().split()

from pyyoutube import Api
yt_api = Api(api_key=api_key)
yt_api.session.verify = False

youtube = build('youtube', 'v3', developerKey=api_key)


def get_all_video_ids_from_playlists(playlist_ids):
    all_videos = []  # Initialize a single list to hold all video IDs

    for playlist_id in playlist_ids:
        next_page_token = None

        # Fetch videos from the current playlist
        while True:
            playlist_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token)
            playlist_response = playlist_request.execute()

            all_videos += [item['contentDetails']['videoId'] for item in playlist_response['items']]

            next_page_token = playlist_response.get('nextPageToken')

            if next_page_token is None:
                break

    return all_videos
    #print(all_videos)
#y=get_all_video_ids_from_playlists(youtube,playlist_ids)


# Fetch all video IDs from the specified playlists
