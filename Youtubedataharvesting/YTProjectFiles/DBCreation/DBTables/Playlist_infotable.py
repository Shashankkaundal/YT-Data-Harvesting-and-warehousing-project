from YTProjectFiles.DBConfigs.DBconnect import check_db as cdb
from YTProjectFiles.DBConfigs.DBconnect import db_connect
from YTProjectFiles.ProjectFunctions.GetPlaylistDetails import playlist_info


def Playlistinfotable(playlist_id,channel_id):
    configfile=db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    # creating the table for ChannelInfo
    c = cdb()
    #if (c == None):
    # cursorObject.execute("""CREATE DATABASE YTHarvest""")
    #else:
    cursorObject.execute("""CREATE DATABASE IF NOT EXISTS YTHarvest""")
    cursorObject.execute("""USE YTHarvest""")
    Channelinfo = """CREATE TABLE IF NOT EXISTS PLAYLIST_INFO (
                    CHANNEL_ID VARCHAR(255) NOT NULL,
                    PLAYLIST_ID VARCHAR(255),
                    PLAYLIST_NAME TEXT,
                    FOREIGN KEY (CHANNEL_ID) REFERENCES CHANNEL_INFO(CHANNEL_ID)
                    )"""
    cursorObject.execute(Channelinfo)
    #taking value from dictionary
    z=playlist_info(playlist_id,channel_id)
    placeholders = ', '.join(['%s'] * len(z))
    columns = ', '.join(z.keys())
    sql = "INSERT INTO  PLAYLIST_INFO (%s) VALUES (%s)" % (columns, placeholders)
    # creating the table for ChannelInfo
    cursorObject.execute(sql, list(z.values()))
    x = cursorObject.fetchall()
    configfile.commit()
    if (x != None):
        val = "Insert successful in Playlist_info Table"
    else:
        val = "Some error Occured while inserting in PlayList_info Table "
    return val