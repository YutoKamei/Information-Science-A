import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np

filepath = 'data-20230630-48h.csv'

dates_list = []
prcp_list = []

with open(filepath) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから各地域の降水量を取得
    for row in reader:
        dt = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
        dates_list.append(dt)
        city_labels = [
            'Oita', 'Saiki', 'Hita', 'BungoTakada', 'Nakatsu',
            'Taketa', 'Kamae', 'Usuki', 'Kitsuki', 'Kusu'
        ]
        prcp_list.append([
            float(row[1]), float(row[2]), float(row[3]), float(row[4]),
            float(row[5]), float(row[6]), float(row[7]), float(row[8]),
            float(row[9]), float(row[10])
        ])

x_list = [i for i in range(1, 49)]

fig = plt.figure()
# 2023年6月30日1時から48時間の降水量のグラフを描画
plt.grid(True)
plt.title('Hourly amount of preciptiation, Jun. 30th - Jul. 1st, 2023')
plt.xlabel('', fontsize=16)
plt.ylabel('Preciptiation (mm)', fontsize=16)

for i in range(10):
    prcp_mm = [f[i] for f in prcp_list]
    plt.plot(x_list, prcp_mm, label=city_labels[i])

plt.legend()
plt.show()

fig.savefig('48h.png')
plt.close()
