import global_value as g

# 在庫情報の更新処理(カートへの登録時および商品補充に対応)
def update_stock(id, quantity, flag):
    # flag: 1 は商品補充時あるいはカートの商品をキャンセル
    #      -1 はカートへの登録時の処理を表す
    g.product[id][2] += flag*quantity
