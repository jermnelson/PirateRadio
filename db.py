__author__ = "Jeremy Nelson"

import os
import sqlite3

def init_db():
    if not os.path.exists("play-lists.sqlite"):
        connection = sqlite3.connect('play-lists.sqlite')
        cursor = connection.cursor()
        with open("radio-playlist.sql") as fo:
            sql = fo.read()
        cursor.executescript(sql)
        connection.commit()
        cursor.close()
        connection.close()

def add_track(podcast, song_url):
    code = 0
    connection = sqlite3.connect('play-lists.sqlite')
    cursor = connection.cursor()
    cursor.execute("""SELECTid FROM podcast WHERE name=?""",
        (podcast, ))
    podcast_id = cursor.fetchone()[0]
    cursor.execute("""SELECT ID FROM tracks WHERE url=?""",
        (song_url,))
    track_id = cursor.fetchone()[0]
    cursor.execute("""INSERT INTO log (podcast_id, track_id) VALUES (?,?)""",
        (podcast_id, track_id))
    connection.commit()
    cursor.close()
    connection.close()
    return code

