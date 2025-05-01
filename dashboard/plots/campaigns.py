def hex_to_rgba(hex_color, alpha=0.8):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return f"rgba({r}, {g}, {b}, {alpha})"



def fig (campaigns):
    import plotly.express as px
    import plotly.graph_objects as go
    from dashboard.styles.constants import primary, color2, color3, secondary, color5, color6, color8, color7, color9, color10
    from dashboard.styles.constants import layout_style, sunburst_style

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

    sunburst_style["marker"]["colors"] = top_10_colors
    sunburst_style["insidetextfont"]["size"] = 15

    rev_est_calc = campaigns[["campaign_type", "budget", "roi"]].copy()
    rev_est_calc["revenue"] = campaigns["budget"] * (1 + (campaigns["roi"] / 100))
    rev_est_calc = rev_est_calc.drop(columns=["budget", "roi"]).groupby(
        ["campaign_type"]).sum().reset_index().sort_values(
        by=["revenue"], ascending=False).reset_index().drop(columns=["index"])

    parents = ["Revenue Share" for i in range(rev_est_calc.shape[0])]

    fig = go.Figure(go.Sunburst(
        labels=rev_est_calc["campaign_type"],
        parents=parents,
        values=rev_est_calc["revenue"],
        **sunburst_style
    ))

    fig.update_layout(title_text="Revenue Share by Campaign Type", 
                    **layout_style)

    return fig