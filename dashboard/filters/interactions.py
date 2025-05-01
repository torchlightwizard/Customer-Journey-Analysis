def df ():
    import pandas as pd
    path = "./data/processed/"
    interactions = pd.read_csv(path+"interactions.csv")

    return interactions