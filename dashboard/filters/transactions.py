def filter (transactions, customer, cb_args):
    min_date = cb_args["start_date"]
    max_date = cb_args["end_date"]
    customer_ids = customer["customer_id"]
    payment_methods = cb_args["payment_method"]

    transactions = transactions[min_date <= transactions["transaction_date"]]
    if not cb_args["end_date"] is None:
        transactions = transactions[transactions["transaction_date"] <= max_date]

    transactions = transactions[transactions["customer_id"].isin(customer_ids)]
    transactions = transactions[transactions["payment_method"].isin(payment_methods)]

    return transactions