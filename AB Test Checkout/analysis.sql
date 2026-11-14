-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT variant, COUNT(*) AS users, SUM(converted) AS conversions, 100.0*AVG(converted) AS conversion_pct FROM facts GROUP BY variant;
