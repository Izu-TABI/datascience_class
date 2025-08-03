import requests
import pandas as pd

# ロサンゼルスの緯度・経度
lat, lon = 34.05, -118.25

# APIエンドポイントとパラメータ
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": lat,
    "longitude": lon,
    "start_date": "2023-07-01",
    "end_date": "2023-07-02",
    "hourly": "temperature_2m,weathercode",
    "timezone": "America/Los_Angeles"
}

# API呼び出し
res = requests.get(url, params=params)
data = res.json()

# DataFrameに変換
df = pd.DataFrame({
    "datetime": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "weathercode": data["hourly"]["weathercode"]
})

# 最初の5行表示
print(df.head())
