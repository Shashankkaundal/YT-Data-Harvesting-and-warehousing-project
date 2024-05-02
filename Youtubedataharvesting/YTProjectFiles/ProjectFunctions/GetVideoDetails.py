import json
import isodate
from YTProjectFiles.API_ConnectionInitiate.Api_initiate_video_details import get_allvideodetails
from YTProjectFiles.ProjectFunctions.Getchanneldetails import extract_channel_name_from_channel_info
def video_info(playlist_id,channel_id):
    videodetails=get_allvideodetails(playlist_id)
    channelname=extract_channel_name_from_channel_info(channel_id)
    #print(len(commentdetails))
    k=0
    video_info=[]
    for i in range(0,len(videodetails)):
        video_info.append({
        'Video_ID':videodetails[i]['VideoID'],
        'Video_Name': videodetails[i]['VideoName'],
        'Video_Description':videodetails[i]['VideoDescription'],
        'Published_Date':videodetails[i]['PublishedDate'],
        'View_Count': videodetails[i]['ViewCount'],
        'Like_Count': videodetails[i]['LikeCount'],
        'Favourite_Count': videodetails[i]['FavouriteCount'],
        'Comment_Count': videodetails[i]['CommentCount'],
        'Duration': videodetails[i]['Duration'],
        'ThumbNail': videodetails[i]['ThumbNail'],
        'Caption_Status': videodetails[i]['CaptionStatus'],
        'Channel_ID':channel_id,
        'Channel_Name':channelname
        })
    #print("_________")
    json_data=json.dumps(video_info)
    #print(json_data)
    return(json_data)
#x=video_info()


