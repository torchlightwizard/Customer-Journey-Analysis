def hex_to_rgba(hex_color, alpha=1):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return f"rgba({r}, {g}, {b}, {alpha})"



def polar_to_xy(theta_rad, base_r=0.65):
    import numpy as np

    if np.cos(theta_rad) > 0:
        r = base_r - ((base_r/3) * np.cos(theta_rad))
    else:
        r = base_r * 1.0

    x = 0.5 + r * np.cos(theta_rad)
    y = 0.5 + r * np.sin(theta_rad)
    return x, y



def compute_annotation_angles (values):
    import numpy as np

    total = sum(values)
    angles = []
    current_angle = 0

    for val in values:
        fraction = val / total
        span = 360 * fraction  # degrees
        start = current_angle
        end = current_angle + span
        mid = start + span / 2
        angles.append((start, end, mid))
        current_angle = end
    
    mid_radians = [np.deg2rad(a[2]) for a in angles]
    return mid_radians



def annotate_at_angle (fig, theta, label, color):
    import numpy as np

    x_a, y_a = polar_to_xy (theta)

    fig.add_annotation(
        x=x_a,
        y=y_a,
        xref="paper",
        yref="paper",
        text=f"{label}",
        font_size=12,
        font_color=color,
        showarrow=True,
        arrowhead=2,
        ax=30,
        ay=0
    )



def fig (campaigns):
    import plotly.express as px
    import numpy as np
    import plotly.graph_objects as go
    from dashboard.styles.figs import primary, color2, color3, secondary, color5, color6, color8, color7, color9, color10
    from dashboard.styles.figs import layout_style, sunburst_style

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
        color10,
        color2
    ]

    top_10_colors = [hex_to_rgba(c) for c in top_10_colors]

    sunburst_style["marker"]["colors"] = top_10_colors
    sunburst_style["insidetextfont"]["size"] = 15

    rev_est_calc = campaigns[["campaign_type", "budget", "roi"]].copy()
    rev_est_calc["revenue"] = campaigns["budget"] * (1 + (campaigns["roi"] / 100))
    rev_est_calc = rev_est_calc.drop(columns=["budget", "roi"]).groupby(
        ["campaign_type"]).sum().reset_index().sort_values(
        by=["revenue"], ascending=False).reset_index().drop(columns=["index"])

    labels = rev_est_calc["campaign_type"].tolist()
    parents = ["Revenue Share" for i in range(rev_est_calc.shape[0])]
    values = rev_est_calc["revenue"].tolist()

    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        textinfo="none",
        hoverinfo="label+value",
        **sunburst_style
    ))

    # Compute angles for annotations
    mid_radians = compute_annotation_angles(values)

    # Annotate at those angles
    for i in range(len(labels)):
        annotate_at_angle (fig, mid_radians[i], labels[i], top_10_colors[i])

        layout_style["title"]["y"] = 0.95
        layout_style["title"]["yanchor"] = "top"

    fig.update_layout(title_text="Revenue Share by Campaign Type", 
                    **layout_style)

    return fig