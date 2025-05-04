from dashboard.plots import kpis as p_kpis
from dashboard.plots import products as p_products
from dashboard.plots import campaigns as p_campaigns
from dashboard.plots import sales as p_sales
from dashboard.plots import funnel as p_funnel

from dashboard.styles.dashboard import *

from dash import Dash, dcc, html, Input, Output
import pandas as pd

from concurrent.futures import ThreadPoolExecutor



# CONFIG LAYER (APPARENTLY)
executor = ThreadPoolExecutor(max_workers=4)



# DATA Layer
path = "./data/processed/"
campaigns_df = pd.read_csv(path+"conversions.csv")
customer_df = pd.read_csv(path+"customers.csv")
interactions_df = pd.read_csv(path+"interactions.csv")
transactions_df = pd.read_csv(path+"transactions.csv")

min_age = int(customer_df["age"].min())
max_age = int(customer_df["age"].max())
genders = list(customer_df["gender"].unique())
states = list(customer_df["state"].unique())
payment_methods = list(transactions_df["payment_method"].unique())
preferred_channels = list(customer_df["preferred_channel"].unique())
min_date = transactions_df["transaction_date"].min()



# APP LAYER
app = Dash(__name__)



app.layout = html.Div([
    html.H1("Customer Journey and Sales Dashboard", style=h1_style),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div(["Revenue Per User Per Session"], style=kpi_label_style), 
                    html.Div([], id="revenue", style=kpi_value_style)
                    ], id="kpi1", style=kpi_box_style),
                html.Div([
                    html.Div(["Conversions"], style=kpi_label_style), 
                    html.Div([], id="conversions", style=kpi_value_style)
                    ], id="kpi2", style=kpi_box_style),
                html.Div([
                    html.Div(["Avg Order Value"], style=kpi_label_style), 
                    html.Div([], id="aov", style=kpi_value_style)
                    ], id="kpi3", style=kpi_box_style),
                html.Div([
                    html.Div(["Customer Lifetime Value"], style=kpi_label_style), 
                    html.Div([], id="clv", style=kpi_value_style)
                    ], id="kpi4", style=kpi_box_style),
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
            html.Div([dcc.Graph(id="funnel", style=graph_style, config={"responsive": True})], className="fig", style=funnel_style),

            html.Div([
                html.Div([dcc.Graph(id="products", style=graph_style, config={"responsive": True})], className="fig", style=products_style),
                html.Div([dcc.Graph(id="campaigns", style=graph_style, config={"responsive": True})], className="fig", style=campaign_style),
                html.Div([dcc.Graph(id="sales", style=graph_style, config={"responsive": True})], className="fig", style=sales_style),
            ], style=top_viz_row),
        ], id="viz_style",style=right_column_style),

    ], style=main_content_style),
], style=body_style)



# UPDATE LAYER
@app.callback(
    Output("revenue", "children"),
    Output("conversions", "children"),
    Output("aov", "children"),
    Output("clv", "children"),

    Input("age", "value"),
    Input("gender", "value"),
    Input("state", "value"),
    Input("payment_method", "value"),
    Input("preferred_channel", "value"),
    Input("dates", "start_date"), 
    Input("dates", "end_date"))
def update_kpis (age, gender, state, payment_method, preferred_channel, start_date, end_date):
    cb_args = {
        "age":age, 
        "gender": gender, 
        "state": state, 
        "payment_method": payment_method, 
        "preferred_channel": preferred_channel, 
        "start_date": start_date, 
        "end_date": end_date
    }

    df_args = {
        "customer": customer_df,
        "interactions": interactions_df,
        "transactions": transactions_df,
        "campaigns": campaigns_df
    }
        
    return executor.submit(p_kpis.plot, df_args, cb_args).result()



@app.callback(
    Output("products", "figure"),

    Input("age", "value"),
    Input("gender", "value"),
    Input("state", "value"),
    Input("payment_method", "value"),
    Input("preferred_channel", "value"),
    Input("dates", "start_date"), 
    Input("dates", "end_date"))
def update_products (age, gender, state, payment_method, preferred_channel, start_date, end_date):
    cb_args = {
        "age":age, 
        "gender": gender, 
        "state": state, 
        "payment_method": payment_method, 
        "preferred_channel": preferred_channel, 
        "start_date": start_date, 
        "end_date": end_date
    }

    df_args = {
        "customer": customer_df,
        "interactions": interactions_df,
        "transactions": transactions_df,
        "campaigns": campaigns_df
    }

    return executor.submit(p_products.plot, df_args, cb_args).result()



@app.callback(
    Output("campaigns", "figure"),

    Input("age", "value"),
    Input("gender", "value"),
    Input("state", "value"),
    Input("payment_method", "value"),
    Input("preferred_channel", "value"),
    Input("dates", "start_date"), 
    Input("dates", "end_date"))
def update_campaigns (age, gender, state, payment_method, preferred_channel, start_date, end_date):
    cb_args = {
        "age":age, 
        "gender": gender, 
        "state": state, 
        "payment_method": payment_method, 
        "preferred_channel": preferred_channel, 
        "start_date": start_date, 
        "end_date": end_date
    }

    df_args = {
        "customer": customer_df,
        "interactions": interactions_df,
        "transactions": transactions_df,
        "campaigns": campaigns_df
    }

    return executor.submit(p_campaigns.plot, df_args, cb_args).result()



@app.callback(
    Output("sales", "figure"),

    Input("age", "value"),
    Input("gender", "value"),
    Input("state", "value"),
    Input("payment_method", "value"),
    Input("preferred_channel", "value"),
    Input("dates", "start_date"), 
    Input("dates", "end_date"))
def update_sales (age, gender, state, payment_method, preferred_channel, start_date, end_date):
    cb_args = {
        "age":age, 
        "gender": gender, 
        "state": state, 
        "payment_method": payment_method, 
        "preferred_channel": preferred_channel, 
        "start_date": start_date, 
        "end_date": end_date
    }

    df_args = {
        "customer": customer_df,
        "interactions": interactions_df,
        "transactions": transactions_df,
        "campaigns": campaigns_df
    }

    return executor.submit(p_sales.plot, df_args, cb_args).result()



@app.callback(
    Output("funnel", "figure"),

    Input("age", "value"),
    Input("gender", "value"),
    Input("state", "value"),
    Input("payment_method", "value"),
    Input("preferred_channel", "value"),
    Input("dates", "start_date"), 
    Input("dates", "end_date"))
def update_funnel (age, gender, state, payment_method, preferred_channel, start_date, end_date):
    cb_args = {
        "age":age, 
        "gender": gender, 
        "state": state, 
        "payment_method": payment_method, 
        "preferred_channel": preferred_channel, 
        "start_date": start_date, 
        "end_date": end_date
    }

    df_args = {
        "customer": customer_df,
        "interactions": interactions_df,
        "transactions": transactions_df,
        "campaigns": campaigns_df
    }

    return executor.submit(p_funnel.plot, df_args, cb_args).result()



app.run(debug=True)