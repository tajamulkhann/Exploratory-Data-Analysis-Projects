-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT channel, SUM(spend) AS spend, SUM(attributed_revenue)/SUM(spend) AS roas FROM facts GROUP BY channel;
