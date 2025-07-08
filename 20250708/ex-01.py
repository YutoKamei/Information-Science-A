import matplotlib.pyplot as plt
import csv
import datetime

# 気象庁過去の気象データ・ダウンロードより
# 2024年1月から12月までの大分市の平均気温，最高気温，最低気温，降水量，平均湿度を入手
# https://www.data.jma.go.jp/gmd/risk/obsdl/
# 温度は摂氏で表記
# (ダウンロードして，データ整形済み)
# 大分市(data-oita.csv)，日田市(data-hita.csv)，豊後高田市(data-bungotakada.csv)
fileoita = 'data-oita-2024.csv'
filehita = 'data-hita-2024.csv'
filebungotakada = 'data-bungotakada-2024.csv'

dates_list = []
oita_tave = []
hita_tave = []
bungotakada_tave = []

with open(fileoita) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから日付と大分市の平均気温を取得
    for row in reader:
        dt = datetime.datetime.strptime(row[1], '%Y-%m-%d')
        dates_list.append(dt)
        tave = float(row[2])
        oita_tave.append(tave)
        # ht = float(row[3])
        # high_temp_list.append(ht)
        # lt = float(row[4])
        # low_temp_list.append(lt)
        # prcp = float(row[5])
        # precipitiation_list.append(prcp)

with open(filehita) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから日田市の平均気温を取得
    for row in reader:
        tave = float(row[2])
        hita_tave.append(tave)

with open(filebungotakada) as fc:
    reader = csv.reader(fc)
    header_row = next(reader)

    # CSVファイルのデータから豊後高田市の平均気温を取得
    for row in reader:
        tave = float(row[2])
        bungotakada_tave.append(tave)

# 2024年1月から12月までの1日ごとの平均気温のグラフを描画
plt.grid(True)
plt.plot(dates_list, oita_tave, linestyle='solid', label='Oita')
plt.plot(dates_list, hita_tave, linestyle='dashed', label='Hita')
plt.plot(dates_list, bungotakada_tave, linestyle='dashdot', label='Bungotakada')
# plt.plot(dates_list, high_temp_list)
# plt.plot(dates_list, low_temp_list)
# plt.bar(dates_list, precipitiation_list)
plt.title('Daily average temperatures, 2024.')
# plt.title('Daily amount of preciptiation')
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
# plt.ylabel('Preciptiation (mm)', fontsize=16)
plt.legend()
plt.show()
plt.close()
