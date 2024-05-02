Hi,
Welcome to YT data harvesting and warehousing project below are the steps in order to run the program.
1.Ensure below things are installed
->Pycharm or any other IDE
->My SQl or equivalent
->Github
>Libraries to be installed:
->Streamlit
->google api python client
->my sql and mysql client
Once all above things are installed.Do below steps in order to run the project
>Create the DB in MYSQL with Name as YTharvest(CREATE DATABASE YTHarvest).
>Now import the project in pycharm IDE.
>Go to ConfigHelpers Directory->DBConfigfile.py->Add your DB username,password,root details.
>Go to API_KEY directory->API_KEY.txt->Add your API key in this file.
>change path of below code
>filename = r"/*your local path*/Youtubedataharvesting/YTProjectFiles/API_Key/API_KEY.txt" in below mentioned directory for all .py files
>>>>API_Connectioninitiate
>Now open the terminal and run the Streamlitinterface.py file using below command[Ensure you run this command in the directory where this file is present.]
-->streamlit run Streamlitinterface.py
>Now Streamlit interface should open and you can do channel_id search and DB queries.

____-------------------------__________________________------------------------------___________________________---------------______________

Execution Flow and Structure

User input channel_id in Channel_ID serach interface on streamlit-->the channel_id passed to channel_infotable.py which creates the channel_info table->this function will inturn call getchannel_details.py ->this functional calls Api_initiate_channel_details->then its displayed on UI.
Same execution happens for other tables video_info,comment_info,playlist_info and results are displayed on UI.
