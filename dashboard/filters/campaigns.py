def filter (campaings, customer, cb_args):
    customer_ids = customer["customer_id"]
    payment_methods = cb_args["payment_method"]

    campaings = campaings[campaings["customer_id"].isin(customer_ids)]
    campaings = campaings[campaings["payment_method"].isin(payment_methods)]

    return campaings