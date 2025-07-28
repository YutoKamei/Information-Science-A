import global_value as g

# 会計処理
# 合計金額の計算処理
# calculate_total関数の説明をコメントで記載すること
#  -- カート内の商品の税抜き・税込み合計金額を計算する
def calculate_total():
    subtotal = 0                # カートにおける商品ごとの金額
    intax_total = 0             # 合計金額(税込み)
    extax_total = 0             # 合計金額(税抜き)
    # グローバル変数カート(リスト)から要素をひとつずつ取り出す
    # 取り出した要素は，辞書itemとして扱う
    for item in g.cart:
        subtotal = item['price'] * item['quantity']
        extax_total += subtotal
        # 税込み合計金額の求め方
        # 1. 辞書itemから商品カテゴリ番号を取り出す
        # 2. 商品カテゴリ番号を用いて，グローバル変数g.item_taxrate(辞書)から当該商品
        #    カテゴリの消費税率を得る(8%か10%か)
        # 3. 消費税率税率を得たら100で割って，subtotalにかけて，subtotalに足す
        intax_total += subtotal + ((subtotal * g.item_taxrate[item['category']]/100))

    # ローカル変数の値をグローバル変数の税抜き合計金額，税込み合計金額に代入
    g.ex_tax = extax_total
    g.in_tax = intax_total
    
