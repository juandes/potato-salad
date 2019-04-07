import datetime
import pandas as pd
import dateutil.parser

df = pd.read_csv('df.csv', encoding='utf-8')

ps_sessions = 0
total_sessions = 0
sessions_songs = {}
for i, _ in df[1:].iterrows():
        song_id = df.loc[i].Id
        # if there has been an hour difference between this Potato Salad and the previous song,
        # we'll assume this is the beginning of a new music section in which PS is the first song
        if dateutil.parser.parse(df.loc[i].PlayedAt) - dateutil.parser.parse(df.loc[i-1].PlayedAt) >= datetime.timedelta(hours=2):
            total_sessions += 1
            if song_id in sessions_songs:
                sessions_songs[song_id] += 1
            else:
                sessions_songs[song_id] = 1
            if song_id == '1jzIJcHCXneHw7ojC6LXiF':
                ps_sessions += 1

print("total sessions {}, Potato Salad sessions {} or {}%".format(total_sessions, ps_sessions, (ps_sessions/total_sessions) * 100))
# key is a function applied prior to executing the sort, in this case we are sorting by value (kv[1]).
# remember that .items returns a list of tuple [(key, value)...]
print("top 5 songs sessions {}".format(sorted(sessions_songs.items(), key=lambda kv: kv[1], reverse = True)[:5]))
