import csv
import sys

from show_products import show_products
from update_stock import update_stock
from show_cart import show_cart
from add_to_cart import add_to_cart
from remove_from_cart import remove_from_cart
from calculate_total import calculate_total
from checkout import checkout

import global_value as g

# お買い物カートアプリ

# 商品管理処理
# ファイルからの商品の読み込み処理
def load_products(filename='products.csv'):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        productreader = csv.reader(csvfile, delimiter=',')
        for row in productreader:
            g.product[int(row[0])] = [row[1], int(row[2]), int(row[3]), int(row[4])]
            g.item_total_num = int(row[0])

# ファイルへの現在の商品情報の保存処理
def save_products(filename='products.csv'):
    # カートに商品が残っている場合には，キャンセル扱いで商品の在庫を戻す
    for item in g.cart:
        update_stock(item['id'], item['quantity'], 1)

    with open(filename, 'w', encoding='utf-8') as csvfile:
        for pkey, pvalues in g.product.items():
            str = f'{pkey},{pvalues[0]},{pvalues[1]},{pvalues[2]},{pvalues[3]}\n'
            csvfile.write(str)

# メニュー表示処理
def show_menu():
    print("""
    **** お買い物カートアプリ ****
    1. 商品一覧を表示
    2. 商品をカートに追加
    3. カートの中身を表示
    4. 商品をカートから削除
    5. 購入
    0. 終了
    """)

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
        print('products.csvが開けません')
        sys.exit()

    while True:
        show_menu()
        choice = int(input("(番号を入力)> "))

        if choice == 1:
            show_products()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            show_cart()
        elif choice == 4:
            remove_from_cart()
        elif choice == 5:
            checkout()
        elif choice == 0:
            save_products()
            print('終了します。ご利用ありがとうございました')
            break
        else:
            print('無効な番号です。選び直してください。')
