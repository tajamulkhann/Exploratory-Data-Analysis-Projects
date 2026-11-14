-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT device, COUNT(*) AS sessions, 100.0*AVG(purchase) AS purchase_rate_pct FROM facts GROUP BY device;
