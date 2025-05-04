from dashboard.filters import campaigns as ft_campaigns
from dashboard.filters import customer as ft_customer

from dashboard.figs import campaigns as fg_campaigns



def plot (df_args, cb_args):
    customer_filtered = ft_customer.filter(df_args["customer"], cb_args)
    campaigns_filtered = ft_campaigns.filter(df_args["campaigns"], customer_filtered, cb_args)

    fig_campaigns = fg_campaigns.fig(campaigns_filtered)
    return fig_campaigns