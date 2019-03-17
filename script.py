import datetime
import pandas as pd
import dateutil.parser

df = pd.read_csv('df.csv', encoding='utf-8')

ps_section = 0
for i, _ in df.iterrows():
    if df.loc[i].Id == '1jzIJcHCXneHw7ojC6LXiF':
        # if there has been an hour difference between this Potato Salad and the previous song,
        # we'll assume this is the beginning of a new music section in which PS is the first song
        if dateutil.parser.parse(df.loc[i].PlayedAt) - dateutil.parser.parse(df.loc[i-1].PlayedAt) >= datetime.timedelta(hours=1):
            ps_section += 1

print(ps_section)
