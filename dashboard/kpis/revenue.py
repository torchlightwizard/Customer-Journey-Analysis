def kpi (interactions, transactions):
    sessions_per_user = interactions.groupby(["customer_id"])["session_id"].nunique().reset_index()

    transactions_online = transactions[transactions["store_location"] == "Online"].copy()
    transactions_online["amount"] = transactions_online["quantity"] * transactions_online["price"]
    transactions_per_user = transactions_online.groupby(["customer_id"])["amount"].sum().reset_index()

    transactions_per_session_per_user = sessions_per_user.merge(transactions_per_user, 
                                                                left_on="customer_id",
                                                                right_on="customer_id").rename(columns={"session_id": "sessions"})

    amount = transactions_per_session_per_user["amount"].sum()
    sessions = transactions_per_session_per_user["sessions"].sum()
    customers = transactions_per_session_per_user["customer_id"].count()
    
    sessions = sessions if sessions > 0 else 1
    customers = customers if customers > 0 else 1

    revenue_per_session_per_user = (( amount / sessions) / customers)

    return round(revenue_per_session_per_user, 2)