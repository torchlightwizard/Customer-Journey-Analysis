def kpi (transactions):
    transactions_online = transactions[transactions["store_location"] == "Online"].copy()

    transactions_online["amount"] = transactions_online["quantity"] * transactions_online["price"]
    transactions_agg = transactions_online.groupby(["customer_id"]).agg(revenue=("amount", "sum"), orders=("product_name", "count"))
    aov = (transactions_agg["revenue"] / transactions_agg["orders"]).reset_index().rename(columns={0: "aov"})

    pf = transactions_online.groupby(["customer_id"]).agg(orders=("product_name", "count")).reset_index()

    cltv_kpi = aov["aov"].mean() * pf["orders"].mean()
    return round(cltv_kpi, 2)