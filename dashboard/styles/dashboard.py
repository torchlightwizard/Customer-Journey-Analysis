from dashboard.styles.colors import *
from dashboard.styles.helpers import hex_to_rgba

label_font_size = 20
tick_size = 15

body_style = {
    "fontFamily": "Arial"
}

h1_style = {
    "width": "100%",
    "textAlign": "center",
    "color": secondary
}

main_content_style = {
    "display": "flex",
    "width": "100%",
    "gap": "25px",
}

label_style = {
    "fontWeight": "bold",
    "color": secondary
}

left_column_style = {
    "display": "flex",
    "flexDirection": "column",
    "width": "25%",
    "gap": "25px",
}

kpis_style = {
    "display": "grid",
    "gridTemplateColumns": "1fr 1fr",
    "gridTemplateRows": "auto auto",
    "gap": "25px"
}

kpi_box_style = {
    "padding": "15px",
    "border": "none", 
    "borderRadius": "20px",
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "center",
    "alignItems": "center",
    "minHeight": "6vh",
    "backgroundColor": hex_to_rgba(background, 0.5)
}

kpi_label_style = {
    "fontSize": "14px",
    "color": secondary,
    "textTransform": "uppercase",
    "letterSpacing": "0.5px",
    "textAlign": "center"
}

kpi_value_style = {
    "fontSize": "22px",
    "fontWeight": "bold",
    "color": primary
}

filters_style = {
    "display": "flex",
    "flexDirection": "column",
    "gap": "10px",
    "border": "none",
    "borderRadius": "20px",
    "padding": "10px",
    "height": "62vh",
    "backgroundColor": hex_to_rgba(background, 0.5)
}

right_column_style = {
    "display": "flex",
    "flexDirection": "column",
    "flex": "1",
    "gap": "25px",
    "height": "100%"
}

top_viz_row = {
    "display": "flex",
    "gap": "25px",
    "height": "39vh"
}

sub_viz_style = {
    "flex": "1",
    "display": "flex",
    "flexDirection": "column",
    "gap": "25px"
}

graph_style = {
    "width": "100%",
    "height": "100%",
    "margin": "0"
}

products_style = campaign_style = sales_style = {
    "flex": "1",
    "padding": "0px",
    "height": "100%",
    "border": "none",
    "borderRadius": "20px",
    "overflow": "hidden",
    "display": "flex",
    "alignItems": "stretch"
}

funnel_style = {
    "padding": "0px",
    "height": "46vh",
    "border": "none",
    "borderRadius": "20px",
    "overflow": "hidden",
    "display": "flex",
    "alignItems": "stretch"
}
