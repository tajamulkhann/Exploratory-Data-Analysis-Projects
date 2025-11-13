# 🚨 911 Calls EDA

An exploratory data-analysis project focused on analyzing 911 emergency call data to uncover patterns, trends, and insights in call volumes and responses.

---

## 📌 Project Overview

This project carries out a full EDA workflow: loading and cleaning the 911 call dataset (timestamps, locations, types of emergencies, response times), conducting a variety of univariate and multivariate analyses, creating derived features (time-of-day, weekday/weekend), visualising trends, and summarising key insights. The goal is to understand call patterns and help emergency services better allocate resources.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset containing 911 call records: features such as call timestamp, call type (fire, medical, traffic, etc.), location (city/neighbourhood), response times, and possibly incident outcome.

### 2. Exploratory Data Analysis (EDA)

* Distribution of call volumes by emergency type, time of day, weekday vs weekend
* Visualisations: heatmaps or bar charts of incident count by hour and by day, location clusters of high‐volume zones
* Analysis of response time distributions and their relation to call type or location
* Correlation and joint plots of features like response time vs call type, time of day
* Identifying missing data, outliers (e.g., extreme response times), and skewed distributions

### 3. Feature Engineering & Insights

* Extracted time features: hour, day of week, weekend flag
* Categorised incident types into broader groups if necessary
* Calculated derived metrics: calls per hour/day per neighbourhood, average response time per incident type and location
* Visualised peak call hours, hotspot locations, and incident type trends
* Examined temporal patterns — e.g., increased medical calls late night, traffic incidents during peak hours

### 4. Key Analytical Findings

* Certain types of incidents concentrated by hour (e.g., traffic calls during rush hour, medical emergencies at late night)
* Locations (zones/neighbourhoods) show clusters of high call volume and longer response times
* Weekend vs weekday patterns differ for incident type mix and call volumes
* Response time varies by incident type and location, suggesting resource allocation opportunities
* Seasonality/holiday spikes may exist in call volumes (if dataset includes date span)

### 5. Business/Operational Recommendations

* Resource planning: Increase staffing or ambulances/call units during peak hours and in hotspot zones
* Incident type prioritisation: Faster response lines or dedicated units for high-risk call types (medical vs traffic)
* Location route optimisation: Dispatch centres closer to high-volume hotspots to reduce response times
* Data-powered scheduling and shift planning: align workforce with observed call peaks and types

---

## 📁 Project Structure

```
911-Calls-EDA/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Peak call hours typically occurred during evening and late night for medical emergencies
* Traffic and accident-related calls peaked during commute hours
* Specific neighbourhoods consistently generated higher call volumes, often with longer response times
* Derived features like “hour of day” and “neighbourhood call rate” significantly improved insight quality
* EDA supports emergency services in shifting from reactive to proactive resource deployment

---

## 🚀 Future Improvements

* Integrate external datasets: weather, event schedules, holidays to explain spikes in call volume
* Incorporate geospatial visualisations (heatmaps, interactive maps) to better identify location clusters and dispatch optimisation
* Build dashboards (Plotly, Streamlit) for real-time monitoring of call patterns and response-time analytics
* Extend to predictive modelling: forecast call volumes by type and location, enabling proactive resource allocation
* Perform anomaly detection for unusual incidents or call volume surges, triggering alerts for emergency planners

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
