from googleapiclient.discovery import build

filename = r"/Users/shashankkaundal/Downloads/Youtubedataharvesting/YTProjectFiles/API_Key/API_KEY.txt"
with open(filename,"rt") as f:
     text = f.readline()
api_key = text.strip().split()

from pyyoutube import Api
yt_api = Api(api_key=api_key)
yt_api.session.verify = False


def channeldetl_initiate(channel_id):
    playlist_id="UUsA5ODt5v-FU0njad7rXn2w"
    youtube = build('youtube', 'v3', developerKey=api_key)
    request1 = youtube.channels().list(
        part="snippet,statistics,contentDetails,status",
        id=channel_id
    )
    response1 = request1.execute()
    return response1
