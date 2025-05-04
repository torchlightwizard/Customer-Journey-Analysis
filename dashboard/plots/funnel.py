from dashboard.filters import interactions as ft_interactions
from dashboard.filters import customer as ft_customer

from dashboard.figs import funnel as fg_funnel



def plot (df_args, cb_args):
    customer_filtered = ft_customer.filter(df_args["customer"], cb_args)
    interactions_filtered = ft_interactions.filter(df_args["interactions"], customer_filtered, cb_args)

    fig_funnel = fg_funnel.fig(interactions_filtered)
    return fig_funnel