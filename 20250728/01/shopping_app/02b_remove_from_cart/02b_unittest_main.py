import csv

from show_cart import show_cart
from add_to_cart313 import add_to_cart
#from add_to_cart312 import add_to_cart
from remove_from_cart import remove_from_cart
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
    g.cart = []    # 空の買い物カート用リスト(グルーバル変数)
    g.item_total_num = 0        # 商品の種類の総計

    try:
        load_products()
    except FileNotFoundError:
        print('test.csvが開けません')
        sys.exit()

    # 商品追加処理
    add_to_cart()
    print('======== 商品追加後のカート表示 ======== ')
    show_cart()
    # 商品削除処理
    remove_from_cart()
    print('======== 商品削除後のカート表示 ======== ')
    show_cart()
    # 商品削除処理
    remove_from_cart()
    print('======== 商品削除後のカート表示 ======== ')
    show_cart()
