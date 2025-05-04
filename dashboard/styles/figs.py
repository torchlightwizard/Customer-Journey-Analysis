from dashboard.styles.colors import *
from dashboard.styles.helpers import hex_to_rgba

label_font_size = 20
tick_size = 15
line_width = 0.2

layout_style = {
    "plot_bgcolor": hex_to_rgba(background, 0),
    "paper_bgcolor": hex_to_rgba(background, 0.5),
    "font": {
        "size": label_font_size,
        "color": secondary
    },
    "title": {
        "font": {
            "size": label_font_size,
            "color": secondary
        },
        "x": 0.5,
        "xanchor": "center", 
    },
    "xaxis": {
        "title": {
            "font": {
                "size": label_font_size,
                "color": secondary
            }
        },
        "tickfont": {
            "size": tick_size,
            "color": secondary
        },
        "gridcolor": hex_to_rgba(secondary, 0.5),
        "gridwidth": line_width,
        "showgrid": True,
        "zeroline": False,
        "linecolor": hex_to_rgba(secondary, 0.5),
        "linewidth": line_width,
    },
    "yaxis": {
        "title": {
            "font": {
                "size": label_font_size,
                "color": secondary
            }
        },
        "tickfont": {
            "size": tick_size,
            "color": secondary
        },
        "gridcolor": hex_to_rgba(secondary, 0.5),
        "gridwidth": line_width,
        "showgrid": True,
        "zeroline": False,
        "linecolor": hex_to_rgba(secondary, 0.5),
        "linewidth": line_width,
    },
    "autosize": True,
    "height": None
}

scatter_style = {
    "marker": {
        "color": primary,
        "line": {
            "color": secondary,
            "width": line_width
        },
        "size": 15,
        "opacity": 0.8
    }
}

sunburst_style = {
    "marker": {
        "colors": [],
        "line": {
            "color": secondary,
            "width": line_width
        }
    },
    "insidetextfont": {
        "size": label_font_size,
        "color": color5
    },
    "outsidetextfont": {
        "size": label_font_size,
        "color": color5
    },
    "branchvalues": "total"
}

bar_style = {
    "marker": {
        "line": {
            "color": secondary, 
            "width": 0
        },
        "color": primary,
        "opacity": 0.8
    }
}
