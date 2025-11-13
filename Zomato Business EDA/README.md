# 🍽️ Zomato Business EDA

A data exploration project focused on analysing the business landscape of restaurants using the Zomato dataset — uncovering trends in pricing, ratings, cuisine, and locations.

---

## 📌 Project Overview

This exploratory data analysis project uses restaurant attributes (e.g., cuisines, average cost for two, rating, location) from the Zomato dataset to uncover actionable business insights. The goal is to help stakeholders in restaurant operations and food­tech platforms identify key patterns such as high/low demand cuisines, pricing strategies, and geographic hotspots.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Restaurant listing data from Zomato including features such as city, locality, cuisines, average cost for two, rating, votes, and other metadata.

### 2. Exploratory Data Analysis (EDA)

* Distribution of restaurant ratings and average cost for two
* Visualisations: cost vs rating, cost by cuisine type, rating by city/locality
* Analysis of popular cuisines, top cities/localities in terms of listings/ratings
* Scatter plots/histograms of cost, rating, votes
* Correlation analysis between numerical variables (cost, rating, votes)
* Identification of outlier listings (very high cost or very low rating)

### 3. Feature Engineering & Insights

* Derived features such as ratings × votes to personalise rating weight, cost buckets (low/medium/high)
* Encoding or grouping of cuisines into primary categories (e.g., ‘North Indian’, ‘Fast Food’, ‘Desserts’)
* Analysing locality performance: average rating & cost by locality/city
* Visualising heatmaps or bar plots of cuisine vs cost vs rating

### 4. Key Analytical Findings

* Certain cuisines (e.g., ‘North Indian’, ‘Desserts’) show higher ratings and moderate cost segments
* High-cost restaurants often have higher ratings but smaller listing counts
* Some cities/localities cluster higher cost and higher ratings—indicating premium segments
* Cost and rating are positively correlated but not perfectly — suggesting other factors (votes, cuisine) influence ratings

### 5. Business / Operational Recommendations

* Restaurants in mid-cost buckets but with high ratings present attractive investment targets
* Food-tech platforms should emphasise under-rated/high-cost listings for promotion or improved UX
* Geographic segmentation: focus expansion in cities/localities with healthy cost-rating balance
* For new restaurants: target cuisines with above-average ratings but moderate cost to maximise ROI

---

## 📁 Project Structure

```
Zomato-Business-EDA/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Moderate-cost restaurants (cost for two in the middle range) combined with niche cuisines often outperform in rating compared to either low-cost or ultra-premium segments
* Votes and number of reviews (popularity) strengthen rating reliability and business viability
* City and locality matter: clusters of high-rated restaurants indicate saturation zones; emerging localities show growth potential
* Exploratory visuals helped validate assumptions about cost vs rating, unsupported by raw variables alone

---

## 🚀 Future Improvements

* Incorporate time-series data: how ratings, cost, and votes evolve over time for restaurants
* Integrate external data such as foot traffic, user behaviour or delivery metrics to enrich analysis
* Deploy a dashboard (e.g., Streamlit or Tableau) for interactive exploration of restaurant cost-rating hotspots
* Perform predictive modelling: e.g., given cuisine, locality and cost, predict expected rating and listing growth
* Expand dataset to include more cities/or international listings to generalise insights

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.datascientist/" target="_blank">
<img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://topmate.io/tajamulkhan" target="_blank">
<img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0MCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white">
</a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f">
<img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>
<a href="https://t.me/tajamul_khan">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://substack.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719">
</a>
<a href="https://www.kaggle.com/tajamulkhan">
<img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
</a>
<a href="https://github.com/tajamulkhann">
<img src="https://img.shields.io/badge/Github-12100E?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://medium.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">
</a>
<a href="https://www.youtube.com">
<img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</a>
</div>
