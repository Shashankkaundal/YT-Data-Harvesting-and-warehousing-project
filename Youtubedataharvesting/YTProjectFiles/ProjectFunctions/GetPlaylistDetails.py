from YTProjectFiles.API_ConnectionInitiate.Api_initiate_Channel_details import channeldetl_initiate
from YTProjectFiles.API_ConnectionInitiate.Api_initiate_playlist_name_details_s import playlistname_initiate
#from YTProjectFiles.Streamlitinterface import userinput_data
#youtube = build('youtube', 'v3', developerKey=api_key)
channel_id = 'UCsA5ODt5v-FU0njad7rXn2w'
playlist_id="UUsA5ODt5v-FU0njad7rXn2w"
def playlist_info(playlist_id,channel_id):
    channel_data=channeldetl_initiate(channel_id)
    #playlistdata=playlistdetl_initiate()
    playlistname=playlistname_initiate(playlist_id)
    print(playlistname)
    playlist_informations = {
        "channel_id": channel_id,
        "playlist_id": playlist_id,
        "playlist_name": playlistname['Playlist_Name']}
    print(playlist_informations)
    return playlist_informations
x=playlist_info(playlist_id,playlist_id)



