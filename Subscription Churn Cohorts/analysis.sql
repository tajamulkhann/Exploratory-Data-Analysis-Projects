-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT plan, COUNT(*) AS customers, 100.0*AVG(active_month6) AS retention6_pct FROM facts GROUP BY plan;
