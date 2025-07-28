from show_cart import show_cart
import global_value as g

# カートからの削除処理
# remove_from_cart関数の説明をコメントで記載すること
#  -- カートから指定された商品を削除、または数量を変更する
def remove_from_cart():
    # グローバル変数カート(リスト)の長さが0であれば，
    # カートには何も登録されていないので削除処理は無効
    if len(g.cart) == 0:
        print('カートには何も登録されていません。')
        return -1
    # カートの内容を表示
    show_cart()
    print('削除するカートの番号を指定してください。')

    # 実際に削除するカート番号とリストの要素番号が1つずれているので-1
    delcartid = int(input('削除するカート番号>')) - 1

    # カートの長さ(カートに登録されている商品の数)を求める
    certlen = len(g.cart)

    # 削除するカートの番号が負数 または，カートの長さよりも大きな番号の場合，処理無効
    if delcartid < 0 or delcartid >= certlen:
        print('カートにない番号のキャンセル処理は受付できません。')
        print('最初からやり直してください。')
        return -1

    # 削除する前に，商品名と購入数を提示
    print(f"{g.cart[delcartid]['name']}が{g.cart[delcartid]['quantity']}個カートに入っています。")
    # 削除する個数の上限(カードに入っている個数)を提示
    print(f"何個カートから削除しますか？ ({g.cart[delcartid]['quantity']}個まで)")

    # 削除する個数を入力
    delqu = int(input('削除する個数>'))

    # 削除する個数がカートに入っている個数を超えると無効
    if delqu > g.cart[delcartid]['quantity']:
        print('カートの個数以上のキャンセルはできません。')
        print('最初からやり直してください。')
        return -1

    # カートから削除した商品の個数は，商品管理の在庫数に反映
    # カートに入っている個数を全部削除した場合には，カートから当該商品を削除
    if g.cart[delcartid]['quantity'] - delqu == 0:
        print(f"{g.cart[delcartid]['name']}をカートから削除しました。")
        g.product[g.cart[delcartid]['id']][2] += delqu # 2は数量を表す要素番号
        del g.cart[delcartid]
    elif g.cart[delcartid]['quantity'] - delqu > 0:
        # 購入個数がまだある場合
        print(f"{g.cart[delcartid]['name']}の購入数は，{g.cart[delcartid]['quantity'] - delqu}個に変更しました。")
        g.cart[delcartid]['quantity'] -= delqu
        g.product[g.cart[delcartid]['id']][2] += delqu # 2は数量を表す要素番号
