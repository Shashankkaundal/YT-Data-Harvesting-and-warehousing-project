from YTProjectFiles.API_ConnectionInitiate.Api_initiate_Channel_details import channeldetl_initiate

#channel_id='UCsA5ODt5v-FU0njad7rXn2w'
#from YTProjectFiles.Streamlitinterface import userinput_data
def channel_info(channel_id):
    channel_data=channeldetl_initiate(channel_id)
    channel_informations = {
        'channel_id': channel_data['items'][0]['id'],
        'channel_name' : channel_data['items'][0]['snippet']['title'],
        'channel_desc' : channel_data['items'][0]['snippet']['description'],
        'sub_count': channel_data['items'][0]['statistics']['subscriberCount'],
        'channel_views': channel_data['items'][0]['statistics']['videoCount'],
        'playlist_id': channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
        'channel_status':channel_data['items'][0]['status']['privacyStatus']}
        #'thumbnails': channel_data['items'][0]['thumbnails']['default']['url']}
    return channel_informations

def extract_playlist_id_from_channel_info(channel_id):
    channel_data = channeldetl_initiate(channel_id)
    play_informations_from_channel_info= channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    #print(play_informations_from_channel_info)
    return play_informations_from_channel_info
def extract_channel_name_from_channel_info(channel_id):
    channel_name = channeldetl_initiate(channel_id)
    channel_name_from_channel_info= channel_name['items'][0]['snippet']['title']
    #print(play_informations_from_channel_info)
    return channel_name_from_channel_info

#x=extract_playlist_id_from_channel_info(channel_id)



