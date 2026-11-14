-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT segment, COUNT(*) AS customers, SUM(monetary) AS revenue FROM facts GROUP BY segment;
