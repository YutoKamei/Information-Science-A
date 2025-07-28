from update_stock import update_stock
from show_cart import show_cart
import global_value as g

# 購入処理
# checkout関数の説明をコメントで記載すること
#  -- カート内の商品を購入または破棄する処理を行う
def checkout():
    # カートの内容をshow_cart関数を呼び出して表示
    show_cart()
    print('カートの商品を購入します。')
    # 税込みの合計金額をグロバール変数の合計金額(税込み)を参照して表示(小数点以下は表示しない)
    print(f'合計金額: {g.in_tax:.0f}円(税込) です。')

    # 購入に進み，購入する場合は，合計金額の支払い方法を提示(実際には提示しない)
    # カートの中身を削除する
    check1 = input('購入しますか？(y/n)>')
    if check1 == 'y':
        print('ご利用ありがとうございました。')
        print(f'合計金額: {g.in_tax:.0f}円(税込) です。支払方法を選んでください(実際には選ばない)。')
        g.cart.clear()          # カートの内容の削除
    elif check1 == 'n':
        # カートの中身を買わない(noの場合)
        # カートの内容をあとで買うか，買わないかを選択(yかnを入力)
        check2 = input('カートの中身をあとで買いますか？(y/n)>')

        # yの場合
        if check2 == 'y':
            print('カートの内容はそのままでメニュー選択に戻ります。')
        # nの場合
        elif check2 == 'n':
            print('カートの内容を破棄しました。')
            # カートの内容を在庫数に反映させ，カートの内容を削除
            for item in g.cart:
                # ひとつひとつカートの内容を読み取り，update_stock関数を呼び
                # 引数: 商品番号，個数，フラグ(在庫を戻すので1)
                # 第1引数と第2引数は，辞書itemを用いる
                update_stock(item['id'], item['quantity'], 1)
            g.cart.clear()      # カートの内容削除
