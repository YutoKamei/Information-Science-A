import csv

from show_cart import show_cart
from calculate_total313 import calculate_total
from add_to_cart313 import add_to_cart
from checkout import checkout
#from calculate_total312 import calculate_total
#from add_to_cart312 import add_to_cart
import global_value as g

# お買い物カートアプリ

# 商品管理処理
# ファイルからの商品の読み込み処理
def load_products(filename='test.csv'):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        productreader = csv.reader(csvfile, delimiter=',')
        for row in productreader:
            g.product[int(row[0])] = [row[1], int(row[2]), int(row[3]), int(row[4])]
            g.item_total_num = int(row[0])

# メイン処理(最初に実行する処理)
if __name__ == '__main__':
    g.item_cat = {10:'食品', 20:'文房具', 30:'飲料', 40:'書籍', 50:'雑貨', 60:'電気製品'}
    g.product = {} # 商品管理用辞書 {id: [商品名,価格,数量,商品カテゴリ番号]}
    # g.product[id]: 商品ごとの管理データ
    # g.product[id][0]: 商品名
    # g.product[id][1]: 価格
    # g.product[id][2]: 数量(在庫数)
    # g.product[id][3]: 商品カテゴリ番号
    g.item_taxrate = {10:8, 20:10, 30:8, 40:10, 50:10, 60:10}
    g.cart = []    # 空の買い物カート用リスト(グルーバル変数)
    g.item_total_num = 0        # 商品の種類の総計
    g.in_tax = 0                # 税込みの合計価格
    g.ex_tax = 0                # 税抜きの合計価格

    try:
        load_products()
    except FileNotFoundError:
        print('test.csvが開けません')
        sys.exit()

    # 商品追加処理
    add_to_cart()
    print('======== 商品追加後のカート表示 ======== ')
    show_cart()
    # 商品追加処理
    add_to_cart()
    print('======== 商品追加後のカート表示 ======== ')
    show_cart()
    # 商品購入処理
    checkout()
    print('======== 商品購入後のカート表示 ======== ')
    show_cart()
