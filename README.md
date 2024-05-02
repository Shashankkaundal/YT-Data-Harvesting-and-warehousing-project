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
>Now open the terminal and run the Streamlitinterface.py file using below command[Ensure you run this command in the directory where this file is present.]
-->streamlit run Streamlitinterface.py
>Now Streamlit interface should open and you can do channel_id search and DB queries.
