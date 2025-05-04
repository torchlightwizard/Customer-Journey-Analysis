from dashboard.filters import interactions as ft_interactions
from dashboard.filters import transactions as ft_transactions
from dashboard.filters import customer as ft_customer

from dashboard.figs import sales as fg_sales



def plot (df_args, cb_args):
    customer_filtered = ft_customer.filter(df_args["customer"], cb_args)
    interactions_filtered = ft_interactions.filter(df_args["interactions"], customer_filtered, cb_args)
    transactions_filtered = ft_transactions.filter(df_args["transactions"], customer_filtered, cb_args)

    fig_sales = fg_sales.fig(interactions_filtered, transactions_filtered)
    return fig_sales