import matplotlib.pyplot as plt
import csv
import datetime

# 気象庁過去の気象データ・ダウンロードより
# 2024年1月から12月までの大分市・日田市・豊後高田市の平均気温などを取得
# https://www.data.jma.go.jp/gmd/risk/obsdl/
# 温度は摂氏で表記（ダウンロード後に整形済み）
fileoita = 'data-oita-2024.csv'
filehita = 'data-hita-2024.csv'
filebungotakada = 'data-bungotakada-2024.csv'

dates_list = []
oita_thigh = []
hita_thigh = []
bungotakada_thigh = []

with open(fileoita) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから日付と大分市の最高気温を取得
    for row in reader:
        dt = datetime.datetime.strptime(row[1], '%Y-%m-%d')
        dates_list.append(dt)
        thigh = float(row[3])
        oita_thigh.append(thigh)

with open(filehita) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから日田市の最高気温を取得
    for row in reader:
        thigh = float(row[3])
        hita_thigh.append(thigh)

with open(filebungotakada) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから豊後高田市の最高気温を取得
    for row in reader:
        thigh = float(row[3])
        bungotakada_thigh.append(thigh)

# 2024年1月〜12月の日別最高気温グラフを描画
plt.grid(True)
plt.plot(dates_list, oita_thigh, linestyle='solid', label='Oita')
plt.plot(dates_list, hita_thigh, linestyle='dashed', label='Hita')
plt.plot(dates_list, bungotakada_thigh, linestyle='dashdot', label='Bungotakada')
plt.title('Daily high temperatures, 2024.')
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.legend()
plt.show()
plt.close()
