def kpi (campaigs):
    conversion_rate = campaigs["conversion_rate"].mean()

    conversion_rate = round(conversion_rate, 2)
    return conversion_rate