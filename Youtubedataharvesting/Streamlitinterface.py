import streamlit as st
import pandas as pd
from YTProjectFiles.API_ConnectionInitiate.Api_initiate_Channel_details import channeldetl_initiate
from YTProjectFiles.DBCreation.DBTables.Channel_infotable import Channelinfotable
from YTProjectFiles.DBCreation.DBTables.Playlist_infotable import Playlistinfotable
from YTProjectFiles.ProjectFunctions.Getchanneldetails import channel_info
from YTProjectFiles.ProjectFunctions.Getchanneldetails import extract_playlist_id_from_channel_info
from YTProjectFiles.DBCreation.DBTables.Video_infotable import Videoinfotable
from YTProjectFiles.DBCreation.DBTables.Comments_infotable import Commentsinfotable
from YTProjectFiles.DBCreation.DBTables.Comments_infotable import comment_info
from YTProjectFiles.API_ConnectionInitiate.Api_get_video_id import get_all_video_ids_from_playlists
from YTProjectFiles.DBQueries.DB_Sql_Queries import query1
from YTProjectFiles.DBQueries.DB_Sql_Queries import query2
from YTProjectFiles.DBQueries.DB_Sql_Queries import query3
from YTProjectFiles.DBQueries.DB_Sql_Queries import query4
from YTProjectFiles.DBQueries.DB_Sql_Queries import query5
from YTProjectFiles.DBQueries.DB_Sql_Queries import query6
from YTProjectFiles.DBQueries.DB_Sql_Queries import query7
from YTProjectFiles.DBQueries.DB_Sql_Queries import query8
from YTProjectFiles.DBQueries.DB_Sql_Queries import query9
from YTProjectFiles.DBQueries.DB_Sql_Queries import query10
def HomePage():
    import streamlit as st
    st.write("# Welcome to Youtube Harvesting Project 👋")
    st.sidebar.success("Select an option above.")
    st.markdown(
        """
        Project Problem Objective:
        
        #The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. 
        
        The Project has below functionalities:
        
        #Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.
        
        #Ability to collect data for up to 10 different YouTube channels and store them in the database clicking a button.
        
        #Option to store the data in a MYSQL.
        
        #Ability to search and retrieve data from the SQL database using different search options.  
    """
    )
def DBqueries():
    import streamlit as st
    st.write("Before Doing DB queries ensure to insert at least 1 channelID in DB")
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        Select a DB query from below.
"""
    )
    option = st.selectbox(
        label='Select a query?',
    options=("1. What are the names of all the videos and their corresponding channels?",
     "2. Which channels have the most number of videos, and how many videos do they have?",
     "3. What are the top 10 most viewed videos and their respective channels?",
     "4. How many comments were made on each video, and what are their corresponding video names?",
     "5. Which videos have the highest number of likes, and what are their corresponding channel names?",
     "6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?",
     "7. What is the total number of views for each channel, and what are their corresponding channel names?",
     "8. What are the names of all the channels that have published videos in the year 2022?",
     "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?",
     "10.Which videos have the highest number of comments, and what are their corresponding channel names?")
    )
    #t=st.write(option)

    if(option=='1. What are the names of all the videos and their corresponding channels?'):
        x=query1()
        st.write(x)
    elif (option == '2. Which channels have the most number of videos, and how many videos do they have?'):
        x = query2()
        st.write(x)
    elif (option == '3. What are the top 10 most viewed videos and their respective channels?'):
        x = query3()
        st.write(x)
    elif (option == '4. How many comments were made on each video, and what are their corresponding video names?'):
        x = query4()
        st.write(x)
    elif (option == '5. Which videos have the highest number of likes, and what are their corresponding channel names?'):
        x = query5()
        st.write(x)
    elif (option == "6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?"):
        x = query6()
        st.write(x)
    elif (option == "7. What is the total number of views for each channel, and what are their corresponding channel names?"):
        x = query7()
        st.write(x)
    elif (option == "8. What are the names of all the channels that have published videos in the year 2022?"):
        x = query8()
        st.write(x)
    elif (option == "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?"):
        x = query9()
        st.write(x)
    elif (option == "10.Which videos have the highest number of comments, and what are their corresponding channel names?"):
        x = query10()
        st.write(x)
def Chidsearch():
    import streamlit as st
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    user_input=st.text_input("Enter Channel ID")
    pr=st.button("Get Channel info")
    inr=st.button("Insert into DB")
    st.write("💡: Go to ChannelDesc->Share Channel->Copy ChannelID")
    if(pr==True):
        x = channeldetl_initiate(user_input)
        y=channel_info(user_input)
        #l1=[]
        for k, v in y.items():
            st.write(k+":"+" "+v)
    if(inr==True):
        #calling the channel_info_details_function
        call_channel_detl = channeldetl_initiate(user_input)
        #calling the channel_info table creation function
        call_channel_info_table = Channelinfotable(user_input)
        #x=st.write(call_channel_info_table)
        if(call_channel_info_table==True):
            st.write("Insert successful in Channel_Info Table")
            extract_playlist_id=extract_playlist_id_from_channel_info(user_input)
            call_Playlist_info_table=Playlistinfotable(extract_playlist_id,user_input)
            st.write(call_Playlist_info_table)
            #call_video_id_func=get_all_video_ids_from_playlists(extract_playlist_id)
            call_video_table=Videoinfotable(extract_playlist_id,user_input)
            st.write(call_video_table)
            call_comment_info_table=Commentsinfotable(extract_playlist_id,user_input)
            st.write(call_comment_info_table)
        else:
            st.write("Insert not possible without unique Channel ID.")
page_names_to_funcs = {
    "Home": HomePage,
    "Channel ID Search": Chidsearch,
    "DB Queries": DBqueries
}
demo_name = st.sidebar.selectbox("Choose an option", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()