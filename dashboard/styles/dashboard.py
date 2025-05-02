label_font_size = 20
tick_size = 15
line_width = 2

primary = "#F5C45E" # yellow
secondary = "#E78B48" # orange
background = "#102E50" # dark blue

color1 = "#03B5AA" # green
color2 = "#F0386B" # red
color3 = "#EDC9FF" # purple
color4 = "#00CFC1" # green 2
color5 = "#F7F7FF" # white
color6 = "#F88DAD" # pink
color7 = "#40F99B" # electric green
color8 = "#C20114" # very red
color9 = "#51CB20" # very green
color10 = "#07A0C3" # blue  

body_style = {
    "backgroundColor": background,
    "fontFamily": "Arial"
}

h1_style = {
    "width": "100%",
    "textAlign": "center",
    "color": secondary
}

label_style = {
    "fontWeight": "bold",
    "color": secondary
}

left_column_style = {
    "display": "flex",
    "flexDirection": "column",
    "width": "25%",
    "gap": "10px",
}

kpis_style = {
    "display": "grid",
    "gridTemplateColumns": "1fr 1fr",
    "gridTemplateRows": "auto auto",
    "gap": "10px",
}

kpi_box_style = {
    "padding": "15px",
    "border": f"5px solid {secondary}", 
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "center",
    "alignItems": "center",
    "minHeight": "6vh",
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
    "border": None
}

main_content_style = {
    "display": "flex",
    "width": "100%",
    "gap": "10px",
}

viz_style = {
    "display": "flex",
    "flexDirection": "column",
    "flex": "1",
    "gap": "20px",
    "height": "100%"
}

top_viz_row = {
    "display": "flex",
    "gap": "10px",
    "height": "39vh"
}

products_style = {
    "flex": "1",
    "padding": "0px",
    "height": "100%",
    "border": "solid",
    "borderWidth": 5,
    "borderColor": secondary,
    "display": "flex",
    "alignItems": "stretch"
}

sub_viz_style = {
    "flex": "1",
    "display": "flex",
    "flexDirection": "column",
    "gap": "20px"
}

campaign_style = sales_style = {
    "flex": "1",
    "padding": "0px",
    "height": "100%",
    "border": "solid",
    "borderWidth": 5,
    "borderColor": secondary,
    "display": "flex",
    "alignItems": "stretch"
}

funnel_style = {
    "padding": "0px",
    "height": "45vh",
    "border": "solid",
    "borderWidth": 5,
    "borderColor": secondary,
    "display": "flex",
    "alignItems": "stretch"
}

graph_style = {
    "width": "100%",
    "height": "100%",
    "margin": "0"
}
