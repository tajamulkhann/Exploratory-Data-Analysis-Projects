-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT category, SUM(net_sales) AS net_sales, SUM(contribution) AS contribution FROM facts GROUP BY category ORDER BY net_sales DESC;
