#課題(2)(c) calculate_total関数を作成後2行目の2行目のコメントを削除する
from calculate_total import calculate_total
import global_value as g

def show_cart():
    # g.cartの長さを調べて，長さが0であればカートの中身は空である
    if len(g.cart) == 0:
        print('カートには何も登録されていません。')
        return -1
    print('カートの中身')
    print('カートの番号: 商品名: 価格 x 個数 (小計(税抜))')
    i = 1
    for item in g.cart:
        # 【商品名】，【価格】，【個数】，【価格*個数】をitemリストを使って記述
        print(f"{i}: {item['name']}: {item['price']} x {item['quantity']} ({item['price'] * item['quantity']})")
        i += 1
    # 課題(2) (c) calculate_total関数を作成後18,19行目のコメントを削除する
    calculate_total()
    print(f'合計: {g.in_tax:.0f}円(税込), {g.ex_tax}円(税抜)')
