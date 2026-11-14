-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT account, SUM(budget) AS budget, SUM(actual) AS actual, SUM(favorable_variance) AS favorable_variance FROM facts GROUP BY account;
