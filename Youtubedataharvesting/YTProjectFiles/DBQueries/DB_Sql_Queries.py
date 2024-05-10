from YTProjectFiles.DBConfigs.DBconnect import db_connect
import pandas as pd
def query1():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query1 = """(select a.video_name,b.channel_name from VIDEO_INFO a join CHANNEL_INFO b
                where a.channel_id=b.channel_id
                        )"""
    cursorObject.execute(query1)
    #x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME", "CHANNEL_NAME"])
    return df

def query2():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query2="""(select count(a.video_id) as Video_Counts,b.channel_id,b.channel_name from video_info a join 
                CHANNEL_INFO b on a.channel_id=b.channel_id group by b.channel_id,b.channel_name order by 
                count(a.video_id) desc)"""
    cursorObject.execute(query2)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_COUNTS", "CHANNEL_ID","CHANNEL_NAME"])
    return df
def query3():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query3="""(select video_name,channel_name 
    from video_info where view_count in 
    (select max(view_count) from video_info group by channel_name) limit 10)"""
    cursorObject.execute(query3)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME", "CHANNEL_NAME"])
    return df
def query4():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query4="""(select video_name,comment_count from video_info)"""
    cursorObject.execute(query4)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME", "COMMENT_COUNT"])
    return df
def query5():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query5="""(select video_name,channel_name
    from video_info where like_count in (select max(like_count) from video_info group by channel_name))"""
    cursorObject.execute(query5)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME", "CHANNEL_NAME"])
    return df
def query6():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query6="""(select a.like_count,a.video_name,b.channel_name from video_info a join channel_info b
            on a.channel_id=b.channel_id)"""
    cursorObject.execute(query6)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_LIKE_COUNT","VIDEO_NAME", "CHANNEL_NAME"])
    return df
def query7():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query7="""(Select CHANNEL_NAME,CHANNEL_VIEWS from CHANNEL_INFO)"""
    cursorObject.execute(query7)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["CHANNEL_NAME", "CHANNEL_VIEWS"])
    return df
def query8():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query8="""(select A.VIDEO_NAME,CAST(A.PUBLISHED_DATE as DATETIME) AS PUBLISHED_DATE,B.CHANNEL_NAME from 
    VIDEO_INFO A JOIN CHANNEL_INFO B on 
        a.channel_id=b.channel_id
        where PUBLISHED_DATE LIKE "%2022%")"""
    cursorObject.execute(query8)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME","PUBLISHED_DATE","CHANNEL_NAME"])
    return df
def query9():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query9="""(SELECT CHANNEL_NAME, 
                        SUM(duration_sec) / COUNT(*) AS average_duration 
                        FROM (
                            SELECT B.CHANNEL_NAME ,
                            CASE
                                WHEN DURATION REGEXP '^PT[0-9]+H[0-9]+M[0-9]+S$' THEN 
                                TIME_TO_SEC(CONCAT(
                                SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'H', 1), 'T', -1), ':',
                            SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'M', 1), 'H', -1), ':',
                            SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'S', 1), 'M', -1)
                            ))
                                WHEN DURATION REGEXP '^PT[0-9]+M[0-9]+S$' THEN 
                                TIME_TO_SEC(CONCAT(
                                '0:', SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'M', 1), 'T', -1), ':',
                                SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'S', 1), 'M', -1)
                            ))
                                WHEN DURATION REGEXP '^PT[0-9]+S$' THEN 
                                TIME_TO_SEC(CONCAT('0:0:', SUBSTRING_INDEX(SUBSTRING_INDEX(DURATION, 'S', 1), 'T', -1)))
                                END AS duration_sec
                        FROM VIDEO_INFO A JOIN CHANNEL_INFO B ON A.CHANNEL_ID=B.CHANNEL_ID
                        ) AS subquery
                        GROUP BY CHANNEL_NAME)"""
    cursorObject.execute(query9)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["CHANNEL_NAME", "AVERAGE_DURATION(IN SECS)"])
    return df
def query10():
    configfile = db_connect()
    # preparing a cursor object
    cursorObject = configfile.cursor()
    cursorObject.execute("""USE YTHarvest""")
    query10="""(select video_name,channel_name
        from video_info where comment_count in (select max(comment_count)
        from video_info group by channel_name))"""
    cursorObject.execute(query10)
    # x=cursorObject.fetchall()
    df = pd.DataFrame(cursorObject.fetchall(), columns=["VIDEO_NAME", "CHANNEL_NAME"])
    return df
