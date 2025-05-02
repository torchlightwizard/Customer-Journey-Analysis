def fig (interactions, transactions):
    import plotly.express as px
    from dashboard.styles.figs import scatter_style, layout_style

    sessions_per_user = interactions.groupby(["customer_id"])["session_id"].nunique().reset_index()

    transactions_online = transactions[transactions["store_location"] == "Online"].copy()
    transactions_online["amount"] = transactions_online["quantity"] * transactions_online["price"]
    transactions_per_user = transactions_online.groupby(["customer_id"])["amount"].sum().reset_index()

    transactions_per_session_per_user = sessions_per_user.merge(transactions_per_user, 
                                                                left_on="customer_id",
                                                                right_on="customer_id").rename(columns={"session_id": "sessions"})

    fig = px.scatter(transactions_per_session_per_user, x="sessions", y="amount")

    fig.update_traces(**scatter_style)
    fig.update_layout(title_text="User Sessions Vs. Spending", 
                      xaxis_title="Number of Sessions", 
                      yaxis_title="Total Spending",
                      **layout_style)
    return fig