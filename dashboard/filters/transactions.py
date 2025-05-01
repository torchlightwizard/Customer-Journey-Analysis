def df ():
    import pandas as pd
    path = "./data/processed/"
    transactions = pd.read_csv(path+"transactions.csv")

    return transactions