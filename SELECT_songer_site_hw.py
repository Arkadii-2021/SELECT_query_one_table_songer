import psycopg2
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql+psycopg2://songer_site:123@localhost:5432/songer_site_playlist_DB')connection = engine.connect()

sel_1 = connection.execute("""SELECT album_name, year_of_issue FROM album
WHERE year_of_issue = 2018;
""").fetchall()

sel_2 = connection.execute("""SELECT name_track, track_duration FROM track
ORDER BY track_duration DESC
LIMIT 1;
""").fetchall()

sel_3 = connection.execute("""SELECT name_track, track_duration FROM track
WHERE track_duration > 210;
""").fetchall()

sel_4 = connection.execute("""SELECT collection_name, year_of_issue FROM collection
WHERE year_of_issue BETWEEN 2018 AND 2020;
""").fetchall()

sel_5 = connection.execute("""SELECT artist_name FROM artist
WHERE NOT artist_name LIKE '%% %%';
""").fetchall()

sel_6 = connection.execute("""SELECT name_track FROM track
WHERE artist_name LIKE '%% %%';
""").fetchall()
