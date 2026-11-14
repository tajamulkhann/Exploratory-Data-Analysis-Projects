-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT department, COUNT(*) AS headcount, SUM(exited_2025) AS exits, 100.0*AVG(exited_2025) AS cohort_exit_rate_pct FROM facts GROUP BY department;
