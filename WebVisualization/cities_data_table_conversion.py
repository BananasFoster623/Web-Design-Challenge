import pandas as pd
from pathlib import Path

# print(Path.cwd())

readpath = Path.cwd() / 'Resources' / 'cities.csv'
writepath = Path.cwd() / 'Resources' / 'csv_data.html'

df = pd.read_csv(readpath)

df.to_html(writepath, index=False)
