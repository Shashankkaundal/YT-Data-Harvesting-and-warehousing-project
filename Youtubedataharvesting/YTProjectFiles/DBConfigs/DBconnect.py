import mysql.connector

# pymysql.install_as_MySQLdb()
from YTProjectFiles.Confighelpers.Dbconfigfile import dbconfigfile


#from Getchanneldetails import channel_info
def db_connect():
    cfile=dbconfigfile()
    dataBase = mysql.connector.connect(**cfile)
    return dataBase

def check_db():
    x=db_connect()
    cursorObject = x.cursor()
    # creating the DB for ChannelInfo
    cursorObject.execute("SHOW DATABASES LIKE 'YTHarvest'")
    c=cursorObject.fetchone()
    return c

"""#def Create_db():
    x=db_connect()
    cursorObject = x.cursor()
    cursorObject.execute("""""")
    return cursorObject
    x.commit()

#def Use_db():
    x = db_connect()
    cursorObject = x.cursor()
    # creating the DB for ChannelInfo
    #cursorObject.execute("""""")#
    return cursorObject
    x.commit()
    #print(dataBase)
#function for creating the table insidethe channdeinfodb

#x=check_db()
# Disconnecting from the server"""
