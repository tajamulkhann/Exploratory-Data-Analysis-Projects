-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT supplier, COUNT(*) AS orders, 100.0*AVG(otif) AS otif_pct FROM facts GROUP BY supplier;
