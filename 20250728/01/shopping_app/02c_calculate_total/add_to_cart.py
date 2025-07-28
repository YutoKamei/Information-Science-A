from show_products import show_products
from update_stock import update_stock
import global_value as g

# カートへの登録処理
# add_to_cart関数の説明をコメントで記載すること
def add_to_cart():
    print('購入する商品番号と数量を入力してください。')
    show_products()
    itemid = int(input('商品番号>'))
    if itemid > g.item_total_num:
        print('入力した商品番号は無効です。')
        print('もう一度最初からやりなおしてください。')
        return -1
    quantity = int(input('購入数>'))
    if g.product[itemid][2] < quantity:
        print('入力した購入数は在庫数を超えています。')
        print('もう一度最初からやり直してください。')
        return -1
    if quantity <= 0:
        print('入力した購入数は無効です。')
        print('もう一度最初からやり直してください。')
        return -1
    
    g.cart.append({'id': itemid, 'quantity':quantity, 'price':g.product[itemid][1], 'name':g.product[itemid][0], 'category':g.product[itemid][3]})
    print(f'{g.product[itemid][0]}を{quantity}個カートに追加しました。')
    update_stock(itemid, quantity, -1)
    # 同じ商品を別々に購入した際，カートの内容をひとまとめにする
    # カートの内容が2つ以上のときで
    if len(g.cart) >= 2:
        lastitemid = g.cart[-1]['id']
        for item in g.cart[0:-1]:
            if item['id'] == lastitemid:
                item['quantity'] += g.cart[-1]['quantity']
                del g.cart[-1]
