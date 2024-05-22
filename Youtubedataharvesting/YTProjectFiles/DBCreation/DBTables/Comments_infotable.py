#from YTProjectFiles.DBConfigs.DBconnect import Use_db as ub
import json

from YTProjectFiles.DBConfigs.DBconnect import check_db as cdb
from YTProjectFiles.DBConfigs.DBconnect import db_connect
from YTProjectFiles.ProjectFunctions.GetCommentDetails import comment_info


def Commentsinfotable(playlist_id,channel_id):
    z = comment_info(playlist_id,channel_id)
    test_json = json.loads(z)
    # create a nested list of the records' values
    values = [list(x.values()) for x in test_json]
    # print(values)

    # get the column names
    columns = [list(x.keys()) for x in test_json][0]

    # value string for the SQL string
    values_str = ""

    # enumerate over the records' values
    for i, record in enumerate(values):

        # declare empty list for values
        val_list = []

        # append each value to a new list of values
        for v, val in enumerate(record):
            if type(val) == str:
                val = "'{}'".format(val.replace("'", "''"))
            val_list += [str(val)]

        # put parenthesis around each record string
        values_str += "(" + ', '.join(val_list) + "),\n"

    # remove the last comma and end SQL with a semicolon
    values_str = values_str[:-2] + ";"

    # concatenate the SQL string
    table_name = "COMMENTS_INFO"
    sql_string = "INSERT INTO %s (%s)\nVALUES\n%s" % (
        table_name,
        ', '.join(columns),
        values_str
    )
    configfile=db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    #c=cdb()
    #if(c==None):
    #cursorObject.execute("""CREATE DATABASE YTHarvest""")
    #else:
     #cursorObject.execute("""USE YTHarvest""")
    cursorObject.execute("""CREATE DATABASE IF NOT EXISTS YTHarvest""")
    cursorObject.execute("""USE YTHarvest""")
    # creating the table for ChannelInfo
    Channelinfo = """CREATE TABLE IF NOT EXISTS COMMENTS_INFO (
                    COMMENT_ID VARCHAR(255) NOT NULL,
                    VIDEO_ID VARCHAR(255),
                    COMMENT_TEXT TEXT,
                    COMMENT_AUTHOR TEXT,
                    COMMENT_PUBLISH_DATE VARCHAR(255),
                    CHANNEL_ID VARCHAR(255),
                    FOREIGN KEY (CHANNEL_ID) REFERENCES CHANNEL_INFO(CHANNEL_ID)
                    )"""
    cursorObject.execute(Channelinfo)
    #taking value from dictionar
    cursorObject.execute(sql_string)
    configfile.commit()
    x = cursorObject.fetchall()
    configfile.commit()
    if (x != None):
        val = "Insert successful in Comments_info Table"
    else:
        val = "Some error Occured while inserting in Comments_info Table "
    return val


