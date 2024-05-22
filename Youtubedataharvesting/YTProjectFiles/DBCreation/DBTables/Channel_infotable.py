import MySQLdb
import mysql
from YTProjectFiles.DBConfigs.DBconnect import db_connect
from YTProjectFiles.ProjectFunctions.Getchanneldetails import channel_info
def Channelinfotable(channel_id):
    val=True
    configfile=db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    # creating the table for ChannelInfo
    #c = cdb()
    #if (c == None):
    #cursorObject.execute("""CREATE DATABASE YTHarvest""")
    #else:
    cursorObject.execute("""CREATE DATABASE IF NOT EXISTS YTHarvest""")
    cursorObject.execute("""USE YTHarvest""")
    Channelinfo = """CREATE TABLE IF NOT EXISTS CHANNEL_INFO (
                    CHANNEL_ID VARCHAR(255) NOT NULL PRIMARY KEY,
                    CHANNEL_NAME VARCHAR(255),
                    CHANNEL_DESC TEXT,
                    SUB_COUNT INT,
                    CHANNEL_VIEWS INT,
                    PLAYLIST_ID VARCHAR(255),
                    CHANNEL_STATUS VARCHAR(255)
                    )"""
    cursorObject.execute(Channelinfo)
    #taking value from dictionary
    z=channel_info(channel_id)
    placeholders = ', '.join(['%s'] * len(z))
    columns = ', '.join(z.keys())
    sql = "INSERT INTO  CHANNEL_INFO (%s) VALUES (%s)" % (columns, placeholders)
    # creating the table for ChannelInfo\
    try:
        cursorObject.execute(sql, list(z.values()))
        x=cursorObject.fetchall()
        configfile.commit()
    except mysql.connector.IntegrityError as err:
        error=err
        if (error)==None:
            val = True
        else:
            val = False
    return val