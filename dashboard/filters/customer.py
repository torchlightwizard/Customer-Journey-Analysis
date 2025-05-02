def filter (customers, cb_args):
    min_age = cb_args["age"][0]
    max_age = cb_args["age"][1]
    genders = cb_args["gender"]
    states = cb_args["state"]
    preferred_channels = cb_args["preferred_channel"]

    customers = customers[(min_age <= customers["age"]) & (customers["age"] <= max_age)]
    customers = customers[customers["gender"].isin(genders)]
    customers = customers[customers["state"].isin(states)]
    customers = customers[customers["preferred_channel"].isin(preferred_channels)]

    return customers