def df ():
    import pandas as pd
    path = "./data/processed/"
    customers = pd.read_csv(path+"customers.csv")

    return customers