def hex_to_rgba(hex_color, alpha=0.8):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return f"rgba({r}, {g}, {b}, {alpha})"



def hex_to_rgba_tup(hex_color, alpha=0.8):
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return (r/255, g/255, b/255, alpha)



def get_set (items):
    import numpy as np

    _, idx = np.unique(items, return_index=True)
    return np.array(items)[idx]



def filter_set(items, criteria):
    import numpy as np

    items = np.array(items)
    mask = np.isin(items, criteria)
    return np.where(mask, items, "Other")



def get_last (my_list):
    if isinstance(my_list, list):
        last_el = my_list[-1]
        return get_last(last_el)
    else:
        return my_list
    


def get_interaction_combination (outer_list, new_el):
    last_el = get_last(outer_list)
    new_list = [last_el, new_el]

    if isinstance(outer_list, list):
        if isinstance(outer_list[-1], list):
            return [*outer_list, new_list]
        else:
            return [outer_list, new_list]
        
    return [new_list]



def get_interaction_combinations (df):
    from collections import Counter
    from functools import reduce

    df = df["interaction_type"].apply(lambda x: reduce(get_interaction_combination, x))
    all_interactions = [(sub_list[0], sub_list[1]) for row in df for sub_list in row]
    count_interactions = Counter(all_interactions).items()
    return count_interactions



def get_sankey (df, criteria):
    count_interactions = get_interaction_combinations(df)
    source = []
    target = []
    value = []
    for count in count_interactions:
        source.append(criteria.index(count[0][0]))
        target.append(criteria.index(count[0][1]))
        value.append(count[1])
    return source, target, value



def plot_sankey (df, criteria, criteria_colors, title="Customer Journey"):
    import plotly.graph_objects as go
    from dashboard.styles.constants import color5, layout_style

    layout_style["font"]["size"] = 12
    
    source, target, value = get_sankey(df, criteria)

    source_colors_hex = [criteria_colors[ind] for ind in source]
    source_colors_rgba = [hex_to_rgba(hex) for hex in source_colors_hex]

    fig = go.Figure(data=[go.Sankey(
        node = {
            "pad": 15,
            "thickness": 20,
            "line": {
                "color": color5,
                "width": 0.5
            },
            "label": criteria,
            "color": criteria_colors
        },
        link = {
            "arrowlen": 10,
            "source": source,
            "target": target,
            "value": value,
            "color": source_colors_rgba
        }
    )])

    fig.update_layout(title_text=title, 
                      **layout_style)

    return fig



def fig (interactions):
    import pandas as pd
    import numpy as np

    primary = "#F5C45E" # yellow
    secondary = "#E78B48" # orange

    color2 = "#F0386B" # red
    color3 = "#EDC9FF" # purple
    color4 = "#00CFC1" # green 2
    color5 = "#F7F7FF" # white
    color6 = "#F88DAD" # pink
    color7 = "#40F99B" # electric green
    color8 = "#C20114" # very red

    important_pages = ["Wishlist_Add", "Add_To_Cart", "Checkout", "Other", "Page_View", "Product_View", "Purchase", "Search", "Leave"]
    important_pages_colors = [primary, secondary, color7, color2, color3, color4, color5, color6, color8]

    interactions_filtered = interactions[interactions["channel"].isin(["Web", "Mobile App"])].copy()
    interactions_filtered["interaction_date"] = pd.to_datetime(interactions_filtered["interaction_date"])
    interactions_filtered = interactions_filtered.sort_values(by=["customer_id", "session_id", "interaction_date"])

    journey = interactions_filtered.groupby(by=["customer_id"])["interaction_type"].agg(list).reset_index()
    journey["interaction_type"] = journey["interaction_type"].apply(lambda items: get_set(items)).apply(lambda items: filter_set(items, important_pages))
    journey["interaction_type"] = journey["interaction_type"].apply(lambda x: np.append(x, "Leave"))

    pages_visited = journey["interaction_type"].apply(lambda items: len(items)).value_counts().reset_index().sort_values(by=["interaction_type"])
    pages_visited.columns = ["pages", "users"]

    return plot_sankey(journey, important_pages, important_pages_colors, title="Unique Customer Journey Through Select Pages")