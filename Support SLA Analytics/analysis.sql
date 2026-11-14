-- SQLite dialect. facts is created by analysis.ipynb after validation.
SELECT priority, SUM(sla_eligible) AS eligible, SUM(sla_met) AS met, SUM(open_ticket) AS open_tickets FROM facts GROUP BY priority;
