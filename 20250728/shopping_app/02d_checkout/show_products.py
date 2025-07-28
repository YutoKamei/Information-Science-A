import global_value as g

# 商品の情報を表示
def show_products():
    print("商品一覧")
    print('商品ID,商品名,価格(税抜),在庫数')
    for pkey,pvalues in g.product.items():
        print(pkey, f"{pvalues[0]}, {pvalues[1]}円, {pvalues[2]}")
