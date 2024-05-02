import json
from YTProjectFiles.API_ConnectionInitiate.Api_initiate_comment_details import get_allcomments
def comment_info(playlist_id,channel_id):
    commentdetails=get_allcomments(playlist_id)
    #print(len(commentdetails))
    k=0
    channel_info=[]
    for i in range(0,len(commentdetails)):
        channel_info.append({
        "Comment_ID":commentdetails[i]["CommentID"],
        "Video_ID": commentdetails[i]["VideoID"],
        "Comment_Text":commentdetails[i]["Comment"],
        "Comment_Author":commentdetails[i]["Username"],
        "Comment_Publish_Date":commentdetails[i]["Date"],
        "Channel_ID":channel_id
        })
    #print("_________")
    json_str = json.dumps(channel_info)
    #print(json_str)
    return (json_str)
#x=comment_info()


