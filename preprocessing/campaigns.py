import pandas as pd

conversion_purchase_rate = 1
campaign_revenue_threshold = 0.7

path = "./data/processed/"
campaigns = pd.read_csv(path+"campaigns.csv")
transactions = pd.read_csv(path+"transactions.csv")



def get_transactions_during (start_date, end_date):
    transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
    transactions_filtered = transactions[["transaction_date", "quantity", "price"]].copy()
    transactions_filtered["revenue"] = transactions_filtered["quantity"] * transactions_filtered["price"]
    transactions_filtered = transactions_filtered.drop(columns=["quantity", "price"])
    transactions_filtered = transactions_filtered[
        (start_date <= transactions_filtered["transaction_date"]) & 
        (transactions_filtered["transaction_date"] < end_date)]
    return transactions_filtered["revenue"]



def optimize_conversion_purchase_rate (conversion_purchase_rate, row, threshold=campaign_revenue_threshold):
    if row["diff"] >= (1 - threshold):
        return row

    conversion_purchase_rate = conversion_purchase_rate / 2
    row["campaign_revenue"] = row["conversions"] * conversion_purchase_rate * row["aov"]
    row["diff"] = (row["total_revenue"] - row["campaign_revenue"]) / row["total_revenue"]
    return optimize_conversion_purchase_rate (conversion_purchase_rate, row)



transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
campaigns["start_date"] = pd.to_datetime(campaigns["start_date"])
campaigns["end_date"] = pd.to_datetime(campaigns["end_date"])
transactions["key"] = 1
campaigns["key"] = 1
conversions = transactions.merge(campaigns, how="left", on="key")
conversions = conversions[(conversions["start_date"] <= conversions["transaction_date"]) & (conversions["transaction_date"] <= conversions["end_date"])]
conversions = conversions[["customer_id", "payment_method", "campaign_type", "conversion_rate"]]

conversions.to_csv("./data/processed/conversions.csv")