from googleapiclient.discovery import build

from YTProjectFiles.API_ConnectionInitiate.Api_get_video_id import get_all_video_ids_from_playlists
filename = r"/Users/shashankkaundal/Downloads/Youtubedataharvesting/YTProjectFiles/API_Key/API_KEY.txt"
with open(filename,"rt") as f:
     text = f.readline()
api_key = text.strip().split()


from pyyoutube import Api
yt_api = Api(api_key=api_key)
yt_api.session.verify = False

youtube = build('youtube', 'v3', developerKey=api_key)
def playlistname_initiate(playlist_id):
    playlist_name_request = youtube.playlists().list(
    part="snippet,contentDetails",
    id=playlist_id
    )
    playlist_name_response = playlist_name_request.execute()
    all_playlistname={
        'Playlist_Name':playlist_name_response['items'][0]['snippet']['title']
        }
    return all_playlistname

"""def get_allvideodetails():
    video_ids = get_all_video_ids_from_playlists(youtube, playlist_ids)
    for video_id in video_ids:
        video_comments = commentdetails_initiate(youtube, video_id)
        all_videos.extend(video_comments)
    return (*all_videos,)
    #print(all_videos)
#get_allvideodetails()"""