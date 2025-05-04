from dashboard.filters import campaigns as ft_campaigns
from dashboard.filters import interactions as ft_interactions
from dashboard.filters import transactions as ft_transactions
from dashboard.filters import customer as ft_customer

from dashboard.kpis import revenue as k_revenue
from dashboard.kpis import clv as k_clv
from dashboard.kpis import aov as k_aov
from dashboard.kpis import conversion as k_conversion



def plot (df_args, cb_args):
    customer_filtered = ft_customer.filter(df_args["customer"], cb_args)
    interactions_filtered = ft_interactions.filter(df_args["interactions"], customer_filtered, cb_args)
    transactions_filtered = ft_transactions.filter(df_args["transactions"], customer_filtered, cb_args)
    campaigns_filtered = ft_campaigns.filter(df_args["campaigns"], customer_filtered, cb_args)

    kpi_revenue = k_revenue.kpi(interactions_filtered, transactions_filtered)
    kpi_conversions = k_conversion.kpi(campaigns_filtered)
    kpi_aov = k_aov.kpi(transactions_filtered)
    kpi_clv = k_clv.kpi(transactions_filtered)

    return kpi_revenue, kpi_conversions, kpi_aov, kpi_clv