import logging
import sys
import pandas_gbq
import pandas as pd
import sys

logger = logging.getLogger('pandas_gbq')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

# read data from BigQuery
query = """
SELECT
  *
FROM
  `{}`
ORDER BY
  PlayedAt
""".format(sys.argv[1])
df = pandas_gbq.read_gbq(query, project_id=sys.argv[2],
                         dialect='standard')

df.to_csv('df.csv', index=False, encoding='utf-8')

potato_df = df.loc[df['Id']== '1jzIJcHCXneHw7ojC6LXiF']

potato_df.to_csv('potato_df.csv', index=False, encoding='utf-8')