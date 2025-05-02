def filter (interactions, customer, cb_args):
    min_date = cb_args["start_date"]
    max_date = cb_args["end_date"]
    customer_ids = customer["customer_id"]

    interactions = interactions[min_date <= interactions["interaction_date"]]
    if not cb_args["end_date"] is None:
        interactions = interactions[interactions["interaction   _date"] <= max_date]

    interactions = interactions[interactions["customer_id"].isin(customer_ids)]

    return interactions