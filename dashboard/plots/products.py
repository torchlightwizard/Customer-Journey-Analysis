from dashboard.filters import transactions as ft_transactions
from dashboard.filters import customer as ft_customer

from dashboard.figs import products as fg_products



def plot (df_args, cb_args):
    customer_filtered = ft_customer.filter(df_args["customer"], cb_args)
    transactions_filtered = ft_transactions.filter(df_args["transactions"], customer_filtered, cb_args)

    fig_products = fg_products.fig(transactions_filtered)
    return fig_products