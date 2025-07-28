import csv

from show_cart import show_cart
from add_to_cart313 import add_to_cart
#from add_to_cart312 import add_to_cart
from clear_cart import clear_cart
import global_value as g

# お買い物カートアプリ

# 変数の定義
# 商品カテゴリ
item_cat = {10:'食品', 20:'文房具', 30:'飲料', 40:'書籍', 50:'雑貨', 60:'電気製品'}
item_taxrate = {10:8, 20:10, 30:8, 40:10, 50:10, 60:10}
product = {} # 商品管理用辞書(グローバル変数) {id: [商品名,価格,数量,商品カテゴリ番号]}
cart = []    # 空の買い物カート用リスト(グルーバル変数)
in_tax = 0
ex_tax = 0
item_total_num = 0

# 商品管理処理
# ファイルからの商品の読み込み処理
def load_products(filename='test.csv'):
    # global product
    # global item_total_num
    with open(filename, 'r', encoding='utf-8') as csvfile:
        productreader = csv.reader(csvfile, delimiter=',')
        for row in productreader:
            g.product[int(row[0])] = [row[1], int(row[2]), int(row[3]), int(row[4])]
            g.item_total_num = int(row[0])

# 商品の情報を表示
def show_products():
    print("商品一覧")
    print('商品ID,商品名,価格(税抜),在庫数')
    for pkey,pvalues in g.product.items():
        print(pkey, f"{pvalues[0]}, {pvalues[1]}円, {pvalues[2]}")

# メイン処理(最初に実行する処理)
if __name__ == '__main__':
    g.item_cat = {10:'食品', 20:'文房具', 30:'飲料', 40:'書籍', 50:'雑貨', 60:'電気製品'}
    g.product = {} # 商品管理用辞書(グローバル変数) {id: [商品名,価格,数量,商品カテゴリ番号]}
    g.cart = []    # 空の買い物カート用リスト(グルーバル変数)
    g.item_total_num = 0

    try:
        load_products()
    except FileNotFoundError:
        print('test.csvが開けません')
        sys.exit()

    print('======== 商品一覧表示 ======== ')
    show_products()
    add_to_cart()
    print('======== 商品追加後のカート表示 ======== ')
    show_cart()
    clear_cart()
    print('======== 商品削除後のカート表示 ======== ')
    show_cart()
