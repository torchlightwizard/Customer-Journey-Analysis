import plotly.express as px
from dashboard.styles.figs import primary, color2, color3, secondary, color5, color6, color8, color7, color9, color10
from dashboard.styles.figs import bar_style, layout_style



def hex_to_rgba(hex_color, alpha=1):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return f"rgba({r}, {g}, {b}, {alpha})"



def fig (transactions):
    top_10_colors = [
        primary,
        color2,
        color3,
        secondary,
        color5,
        color6,
        color8,
        color7,
        color9,
        color10
    ]

    top_10_colors = [hex_to_rgba(c) for c in top_10_colors]

    products = transactions.groupby(by=["product_name"])["customer_id"].count().reset_index()
    products = products.rename(columns={"customer_id": "freq"}).sort_values(by=["freq"], ascending=False).reset_index(drop=True)
    products = products.iloc[:10]

    max_x = products["freq"].max()
    max_x = (max_x * 1.1)
    min_x = products["freq"].min()
    min_x = min_x - (min_x*0.05)

    fig = px.bar(products, 
                 x="freq", 
                 y="product_name",
                 category_orders={'product_name': products['product_name'].tolist()},
                 orientation='h',
                 range_x=[min_x, max_x])
    
    fig.update_traces(**bar_style)
    fig.update_layout(title_text="Top Sold Products", 
                    xaxis_title="No. of Items Sold", 
                    yaxis_title="Products",
                    **layout_style,
                    showlegend=False)
    return fig