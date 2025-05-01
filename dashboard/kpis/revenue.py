def kpi (interactions, transactions):
    sessions_per_user = interactions.groupby(["customer_id"])["session_id"].nunique().reset_index()

    transactions_online = transactions[transactions["store_location"] == "Online"].copy()
    transactions_online["amount"] = transactions_online["quantity"] * transactions_online["price"]
    transactions_per_user = transactions_online.groupby(["customer_id"])["amount"].sum().reset_index()

    transactions_per_session_per_user = sessions_per_user.merge(transactions_per_user, 
                                                                left_on="customer_id",
                                                                right_on="customer_id").rename(columns={"session_id": "sessions"})

    revenue_per_session_per_user = ((transactions_per_session_per_user["amount"].sum() / 
                                    transactions_per_session_per_user["sessions"].sum()) / 
                                    transactions_per_session_per_user["customer_id"].count())

    return round(revenue_per_session_per_user, 2)