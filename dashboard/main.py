from dashboard.plots import sales
from dashboard.plots import campaigns as p_campaigns
from dashboard.plots import funnel
from dashboard.plots import products

from dashboard.kpis import revenue
from dashboard.kpis import clv
from dashboard.kpis import aov
from dashboard.kpis import conversion

from dashboard.filters import interactions, transactions, campaigns as f_campaigns, customer

from dashboard.styles.dashboard import *

from dash import Dash, dcc, html, Input, Output

min_age = int(customer.df()["age"].min())
max_age = int(customer.df()["age"].max())
genders = list(customer.df()["gender"].unique())
states = list(customer.df()["state"].unique())
payment_methods = list(transactions.df()["payment_method"].unique())
preferred_channels = list(customer.df()["preferred_channel"].unique())
min_date = interactions.df()["interaction_date"].min()



app = Dash(__name__)



app.layout = html.Div([
    html.H1("Customer Journey and Sales Dashboard", style=h1_style),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div(["Revenue"], style=kpi_label_style), 
                    html.Div([], id="revenue", style=kpi_value_style)
                    ], style=kpi_box_style),
                html.Div([
                    html.Div(["Conversions"], style=kpi_label_style), 
                    html.Div([], id="conversions", style=kpi_value_style)
                    ], style=kpi_box_style),
                html.Div([
                    html.Div(["Avg Order Value"], style=kpi_label_style), 
                    html.Div([], id="aov", style=kpi_value_style)
                    ], style=kpi_box_style),
                html.Div([
                    html.Div(["Customer Lifetime Value"], style=kpi_label_style), 
                    html.Div([], id="clv", style=kpi_value_style)
                    ], style=kpi_box_style),
            ], style=kpis_style),

            html.Div([
                html.Label("Select Age Range:", style=label_style),
                dcc.RangeSlider(min_age, max_age, 5, count=1, value=[min_age, min_age+10], id="age"),

                html.Label("Select Gender:", style=label_style),
                dcc.Dropdown(genders, genders, multi=True, id="gender"),

                html.Label("Select States:", style=label_style),
                dcc.Dropdown(states, states, multi=True, id="state"),

                html.Label("Select Payment Methods:", style=label_style),
                dcc.Dropdown(payment_methods, payment_methods, multi=True, id="payment_method"),

                html.Label("Select Channels Preferred by Audience:", style=label_style),
                dcc.Dropdown(preferred_channels, preferred_channels, multi=True, id="preferred_channel"),

                html.Label("Select Date Range:", style=label_style),
                dcc.DatePickerRange(
                    start_date=min_date,
                    end_date_placeholder_text='Select a date!',
                    id="dates"
                ),
            ], style=filters_style),

        ], style=left_column_style),

        html.Div([
            html.Div([
                html.Div([dcc.Graph(id="products", style=graph_style, config={"responsive": True})], style=products_style),
                html.Div([dcc.Graph(id="campaigns", style=graph_style, config={"responsive": True})], style=campaign_style),
                html.Div([dcc.Graph(id="sales", style=graph_style, config={"responsive": True})], style=sales_style),
            ], style=top_viz_row),

            html.Div([dcc.Graph(id="funnel", style=graph_style, config={"responsive": True})], style=funnel_style),
        ], style=viz_style),

    ], style=main_content_style),
], style=body_style)



@app.callback(
    Output("products", "figure"),
    Output("campaigns", "figure"),
    Output("sales", "figure"),
    Output("funnel", "figure"),

    Output("revenue", "children"),
    Output("conversions", "children"),
    Output("aov", "children"),
    Output("clv", "children"),

    Input("age", "value"))
def update_bar_chart(args):
    args = []

    kpi_revenue = revenue.kpi(interactions.df(*args), transactions.df(*args))
    kpi_conversions = conversion.kpi(f_campaigns.df(*args))
    kpi_aov = aov.kpi(transactions.df(*args))
    kpi_clv = clv.kpi(transactions.df(*args))


    fig_products = products.fig(transactions.df(*args))
    fig_campaigns = p_campaigns.fig(f_campaigns.df(*args))
    fig_sales = sales.fig(interactions.df(*args), transactions.df(*args))
    fig_funnel = funnel.fig(interactions.df(*args))

    return fig_products, fig_campaigns, fig_sales, fig_funnel, kpi_revenue, kpi_conversions, kpi_aov, kpi_clv



app.run(debug=True)