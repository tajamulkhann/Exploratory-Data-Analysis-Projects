# ✈️ Flight Price EDA

A data exploration project focused on airfare variations and the factors influencing flight ticket pricing.

---

## 📌 Project Overview

This project undertakes a comprehensive exploratory data analysis of flight fare data, analyzing how variables like airline, source–destination pair, departure time, stops, and duration affect ticket prices. The goal is to uncover pricing trends, detect outliers and patterns, and derive business-relevant insights into airfare dynamics.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset containing flight booking records with features such as airline, date of journey, source, destination, departure time, arrival time, stops, duration, and price.

### 2. Exploratory Data Analysis (EDA)

* Distribution of ticket prices across airlines, routes, and stop counts
* Visualizations of departure time vs price, duration vs price, stops vs price
* Boxplots for price by airline, route, day of the week, and month
* Correlation analysis between numerical features and price
* Detection of outliers and anomalies (e.g., ultra-high fares or very short durations)
* Analysis of categorical features: airline market share, popular routes, stop frequency

### 3. Feature Engineering Insights

* Extracted time features from date of journey: day, month, weekday, hour
* Derived features like total travel time (duration), number of stops encoded numerically
* Categorised duration into bins (short/medium/long haul)
* One-hot or label encoding of categorical features where relevant
* Observed skewness in price distribution and applied log-transform for better visualization

### 4. Key Analytical Findings

* Flights with more stops tend to have lower prices, but exceptions exist due to route complexity
* Duration positively correlates with price – longer flights cost more, as expected
* Departure time (e.g., early morning vs evening) shows variation in pricing across airlines
* Certain airlines command premium pricing on specific high-demand routes
* Seasonal/weekday effects visible: fares vary by booking date, day of week, and time to departure

### 5. Business Insights & Recommendations

* For consumers: booking earlier, choosing non-peak times and fewer stops often leads to lower fares
* For airlines: route pricing dynamics reflect supply–demand and competition; fine-tune pricing for stop-heavy routes
* For aggregators/travel platforms: highlight best value flights by combining features like fewer stops + shorter duration + off-peak timing
* Data suggests opportunities for predictive modelling of ticket pricing if used as next step

---

## 📁 Project Structure

```
Flight-Price-EDA/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Duration and number of stops are strong price predictors in exploratory visuals
* Relevant time features (day of week, month) add new context to pricing patterns
* Price distribution is right-skewed; log-transformation improves normality for modelling
* Some outlier fares indicate potential data issues or premium/charter segments worth separate analysis
* Insight: combining visual and statistical analysis provides actionable guidance for pricing strategies

---

## 🚀 Future Improvements

* Extend analysis into predictive modelling (regression) to forecast ticket prices based on features
* Incorporate booking lead time (days between booking and travel) and seat-class data for deeper insight
* Visualise interactive dashboards (Plotly/Streamlit) for travel analysts or consumers
* Enrich data with external factors: holidays, airport competition, fuel prices, airline alliances
* Analyse route-specific dynamics (domestic vs international, hub vs regional airports) for more granular insights

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
