![Sample Report Page](public/ScreenShot%201.PNG)
![Sample Report Page](public/ScreenShot%202.PNG)

# Tntro
An analysis conducted on user session behaviour, transactions and demographics data. The data spans from 2020 to 2025.

# Problem Statement
What patterns in our customers’ journeys drive spend, repeat purchases, and campaign ROI, and how can Marketing optimize touchpoints to boost revenue and retention?

# Solutions
1. We do notebook eda.
2. Build a classification model for early detection of low or high cltv.
3. Build a dashboard for a thorough demographic representation of data.

# How to run
1. Setup
```
python -m venv .localenv
.localenv\Scripts\python -m pip install -r requirements.txt
```
2. ProcessedData Generation
    1. Run the Preprocessing.ipynb notebook
    2. For conversions data set run
    ```
    .localenv\Scripts\python -m preprocessing campaigns
    ```
3. Run Dashboard
```
.localenv\Scripts\python -m dashboard.main
```

# Key Insights gained
1. The highest quantile `1/30` of total customers contribute to `1/2` of total revenue/spending. Then our pareto's cummulative sum crossed the `80%` total revenue/spending at the top `11th` quantile or `~1/3` of total customers.<br>
    This aligns with the `80/20` rule that `20%` customers contribute to the `80%` revenue/spending. In our case it was `70/30`.
2. Search Engine Marketing has almost 3 times the ROI of all other campaign types. The second highest ROIs is of Email Marketing followed by In-Store Marketing.<br>
    We should take note that Social Media Marketing is only slightly better performance than the regular old channels, it is not very performant.
3. After checkout the users don't go directly to purchase, they go to mostly page view deciding on what to finalize or having one last time thoughts, or go to somewhere else in case they changed their mind or are still browsing.
4. By putting items in wishlist, the people seem to feel the need to browse from other sites or maybe from local store, before finalizing purchase, so they leave the site.
5. Home items and smartphones had the highest increase in purchases. They trended for the total duration. The products were `Ring Doorbell`, `Baking Sheet` and `Google Pixel 6`.<br>
    The sale of `USB-C hub` declined over the total duration.
6. `Cookware`, `Ipad` and `Coffee Makers` have the highest cart abandonment rates.


# Dataset
https://www.kaggle.com/datasets/raghavendragandhi/retail-customer-and-transaction-dataset
