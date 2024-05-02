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
all_comments = []
def commentdetails_initiate(video_id):
    all_comment = []
    next_page_token = None
    while True:
        comment_request = youtube.commentThreads().list(
            part="snippet,id",
            videoId=video_id,
            pageToken=next_page_token,
            textFormat="plainText",
            maxResults=100
        )
        comment_response = comment_request.execute()

        for item in comment_response['items']:
            top_comment = item['snippet']['topLevelComment']['snippet']
            comment_id=item['snippet']['topLevelComment']['id']
            all_comment.append({
                'Timestamp': top_comment['publishedAt'],
                'Username': top_comment['authorDisplayName'],
                'VideoID': video_id,  # Directly using video_id from function parameter
                'Comment': top_comment['textDisplay'],
                'Date': top_comment['updatedAt'] if 'updatedAt' in top_comment else top_comment['publishedAt'],
                'CommentID': comment_id
            })
        next_page_token = comment_response.get('nextPageToken')
        if not next_page_token:
            break

    return all_comment

def get_allcomments(playlist_id):
    dic={}
    playlist_value=[]
    playlist_value.append(playlist_id)
    video_ids = get_all_video_ids_from_playlists(playlist_value)
    for video_id in video_ids:
        video_comments = commentdetails_initiate(video_id)
        all_comments.extend(video_comments)
    return (all_comments)