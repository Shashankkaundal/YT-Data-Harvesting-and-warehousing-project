from googleapiclient.discovery import build
import isodate
from YTProjectFiles.API_ConnectionInitiate.Api_get_video_id import get_all_video_ids_from_playlists
filename = r"/Users/shashankkaundal/Downloads/Youtubedataharvesting/YTProjectFiles/API_Key/API_KEY.txt"
with open(filename,"rt") as f:
     text = f.readline()
api_key = text.strip().split()


from pyyoutube import Api
yt_api = Api(api_key=api_key)
yt_api.session.verify = False

youtube = build('youtube', 'v3', developerKey=api_key)
all_videos = []
def videodetails_initiate(video_id):
    all_videos_detl = []
    next_page_token = None
    while True:
        video_detail_request = youtube.videos().list(
            part="snippet,contentDetails,statistics,status",
            id=video_id
        )
        video_detail_response = video_detail_request.execute()

        for item in video_detail_response['items']:
            all_videos_detl.append({
                'VideoID': item['id'],
                'VideoName':item['snippet']['title'] ,
                'VideoDescription': item['snippet']['description'],
                'PublishedDate': item['snippet']['publishedAt'],
                'ViewCount': item['statistics']['viewCount'],
                'LikeCount':item['statistics']['likeCount'],
                'FavouriteCount':item['statistics']['favoriteCount'],
                'CommentCount':item['statistics']['commentCount'],
                'Duration':item['contentDetails']['duration'],
                'ThumbNail':item['snippet']['thumbnails']['default']['url'],
                'CaptionStatus':item['contentDetails']['caption']
            })
        next_page_token = video_detail_response.get('nextPageToken')
        if not next_page_token:
            break

    return all_videos_detl

def get_allvideodetails(playlist_ids):
    playlist_value=[]
    playlist_value.append(playlist_ids)
    video_ids = get_all_video_ids_from_playlists(playlist_value)
    for video_id in video_ids:
        video_comments = videodetails_initiate(video_id)
        all_videos.extend(video_comments)
    return (*all_videos,)