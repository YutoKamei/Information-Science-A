# 配布用
from update_stock import update_stock
from show_products import show_products

import global_value as g

# カートへの登録処理
# add_to_cart関数の説明をコメントで記載すること
#  -- 商品番号と数量を受け取り、在庫を確認後カートに商品を追加する
def add_to_cart():
    print('購入する商品番号と数量を入力してください。')
    show_products()
    itemid = int(input('商品番号>'))

    # 入力した商品番号(itemid)が，global変数item_total_numよりも
    # 大きい値であれば無効として扱う
    if itemid > g.item_total_num:
        print('入力した商品番号は無効です。')
        print('もう一度最初からやりなおしてください。')
        return -1
    # 購入する個数の入力
    quantity = int(input('購入数>'))

    # 入力した購入数が在庫数を超えていると無効
    if g.product[itemid][2] < quantity:
        print('入力した購入数は在庫数を超えています。')
        print('もう一度最初からやり直してください。')
        return -1
    # 入力した購入数が0以下の場合無効
    if quantity <= 0:
        print('入力した購入数は無効です。')
        print('もう一度最初からやり直してください。')
        return -1

    # カートへの挿入
    # カートの構造: リストの要素として，辞書をもつ
    # 辞書: {'id':商品番号, 'quantity':購入数, 'price':価格, 'name':商品名, 'category':商品カテゴリ}
    g.cart.append({'id': itemid, 'quantity':quantity, 'price':g.product[itemid][1], 'name':g.product[itemid][0], 'category':g.product[itemid][3]})

    print(f'{g.product[itemid][0]}を{quantity}個カートに追加しました。')

    update_stock(itemid, quantity, -1)
    # 同じ商品を別々に購入した際，カートの内容をひとまとめにする
    # カートの内容が2つ以上のときで
    if len(g.cart) >= 2:
        # 最後にカートに追加した商品番号を取得
        lastitemid = g.cart[-1]['id']
        # カートの0番目から最後から2番目まで走査
        for item in g.cart[0:-1]:
            # 最後にカートに追加した商品番号と同じ商品番号があれば統合
            if item['id'] == lastitemid:
                # 最後にカートに追加した購入数を前にカートに追加した購入数に加算
                item['quantity'] += g.cart[-1]['quantity']
                # 最後にカートに追加した情報は削除
                del g.cart[-1]
