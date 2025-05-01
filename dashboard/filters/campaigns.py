def df ():
    import pandas as pd
    path = "./data/processed/"
    campaigns = pd.read_csv(path+"campaigns.csv")

    return campaigns