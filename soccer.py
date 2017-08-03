import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = "https://www.uefa.com/uefachampionsleague/season=2017/statistics/round=2000783/players/type=topscorers/index.html"

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")


uefa = []

def collect_data(switch):
	players = soup.find_all("tr",{"class":switch})
	stats = soup.find_all("td")
	for p in players:
		for stats in p:
			uefa.append(stats.text)

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


collect_data("on")
collect_data("off")
new_uefa = split(uefa,4)

df = pd.DataFrame(new_uefa, columns=("name","goal","time","club"))
df["goal"] = df["goal"].astype('int')
df["time"] = df["time"].astype('int')
df['min/goal'] = df['time']/df['goal']
print(df)


plt.plot(df.time, df.goal, "bo")
plt.axis([0,1500,0,20])
plt.xlabel('Time Played')
plt.ylabel('Goal')
plt.title('UEFA 16/17')
# plt.show()
