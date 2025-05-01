fig_width = 1080
fig_height = 720
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

layout_style = {
    "plot_bgcolor": background,
    "paper_bgcolor": background,
    "width": fig_width,
    "height": fig_height,
    "font": {
        "size": label_font_size,
        "color": secondary,
        "family": "Arial",
    },
    "title": {
        "font": {
            "size": label_font_size,
            "color": secondary,
            "family": "Arial"
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
        "gridcolor": secondary,
        "gridwidth": line_width,
        "showgrid": True,
        "zeroline": False,
        "linecolor": secondary,
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
        "gridcolor": secondary,
        "gridwidth": line_width,
        "showgrid": True,
        "zeroline": False,
        "linecolor": secondary,
        "linewidth": line_width,
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
            "width": 3
        },
        "opacity": 0.8
    }
}