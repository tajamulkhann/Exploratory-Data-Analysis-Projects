# Run from this project directory. Notebook companion with identical code.

from pathlib import Path
import json, sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
BASE = Path.cwd()
assert (BASE/'data/raw.csv').exists(), 'Run from this project directory'
OUT = BASE/'outputs'
OUT.mkdir(exist_ok=True)
pd.set_option('display.max_columns', 20)
plt.rcParams.update({'figure.dpi':120, 'axes.spines.top':False, 'axes.spines.right':False})
df = pd.read_csv(BASE/'data/raw.csv')
if 'date' in df:
    df['date'] = pd.to_datetime(df['date'])
print('Raw shape:',df.shape)
display(df.head())


audit=pd.DataFrame({'dtype':df.dtypes.astype(str),'missing':df.isna().sum(),'unique_values':df.nunique()})
display(audit)
print('Exact duplicate rows:',df.duplicated().sum())
audit.to_csv(OUT/'data_quality.csv')


assert df.ticket_id.is_unique
snapshot=pd.Timestamp('2026-01-01');df['age_hours']=(snapshot-df.date).dt.total_seconds()/3600
df['sla_hours']=df.priority.map({'High':4,'Medium':12,'Low':24})
df['sla_eligible']=df.first_response_hours.notna()|(df.age_hours>df.sla_hours)
df['sla_met']=(df.first_response_hours<=df.sla_hours).astype(int)
df['open_ticket']=df.resolution_hours.isna().astype(int)
summary=df.groupby('priority').agg(tickets=('ticket_id','size'),eligible=('sla_eligible','sum'),met=('sla_met','sum'),open_tickets=('open_ticket','sum'))
summary['sla_pct']=100*summary.met/summary.eligible
metrics={'Eligible response SLA met (%)':100*df.sla_met.sum()/df.sla_eligible.sum(),'Open tickets':df.open_ticket.sum(),'CSAT response coverage of closed (%)':100*df.csat.notna().sum()/df.resolution_hours.notna().sum()}
chart=summary.sla_pct; ylabel='Eligible response SLA met (%)'
df[df.open_ticket==1].to_csv(OUT/'open_ticket_aging.csv',index=False)


open_df=df[df.open_ticket==1].copy();open_df['age_band']=pd.cut(open_df.age_hours,bins=[0,24,72,168,np.inf],labels=['0-24h','24-72h','72-168h','168h+'],include_lowest=True)
detail=open_df.groupby('age_band',observed=False).agg(open_tickets=('ticket_id','size'),mean_age_hours=('age_hours','mean'))
assert detail.open_tickets.sum()==df.open_ticket.sum()
display(detail.round(2))
fig,ax=plt.subplots(figsize=(8,4));detail.open_tickets.plot.bar(ax=ax,color='#a06536',rot=0);ax.set_ylabel('Open tickets');ax.set_title('Backlog aging at snapshot');fig.tight_layout();fig.savefig(OUT/'detail.png');plt.show()
worst=summary.sla_pct.idxmin()
recommendation=f'{worst} has the lowest eligible first-response SLA compliance ({summary.loc[worst,"sla_pct"]:.2f}%). Investigate triage and staffing while retaining overdue unanswered tickets in the metric.'

detail.to_csv(OUT/'detail.csv')
print(recommendation)
(OUT/'recommendation.txt').write_text(recommendation+'\n')


display(summary.round(4))
display(pd.Series(metrics,name='value').to_frame())
summary.to_csv(OUT/'summary.csv')
(OUT/'metrics.json').write_text(json.dumps({k:float(v) for k,v in metrics.items()},indent=2))
df.to_csv(OUT/'analysis_ready.csv',index=False)
assert all(np.isfinite(float(v)) for v in metrics.values()), 'Invalid KPI'


with sqlite3.connect(':memory:') as conn:
    df.to_sql('facts',conn,index=False,if_exists='replace')
    sql_result=pd.read_sql_query((BASE/'analysis.sql').read_text(),conn)
display(sql_result)
sql_result.to_csv(OUT/'sql_results.csv',index=False)
# Reconcile at least one common aggregate by group, rather than trusting the SQL output.
key=sql_result.columns[0]
py=summary.reset_index()
common=[c for c in sql_result.columns[1:] if c in py.columns]
assert common, 'No comparable aggregate'
joined=sql_result.merge(py,on=key,suffixes=('_sql','_python'),validate='one_to_one')
assert len(joined)==len(summary)==len(sql_result)
for col in common:
    assert np.allclose(joined[col+'_sql'],joined[col+'_python'],rtol=1e-8,atol=1e-6), col
print('SQL / Python reconciliation passed:',common)


fig,ax=plt.subplots(figsize=(9,4.6))
chart.plot(kind='bar',ax=ax,color='#246577',rot=25)
ax.set_ylabel(ylabel)
ax.set_xlabel('')
ax.set_title('Customer Support SLA and Backlog',loc='left',fontweight='bold',pad=15)
fig.tight_layout()
fig.savefig(OUT/'overview.png',bbox_inches='tight')
plt.show()


# Standalone dashboard: no remote JavaScript, server or account required.
import html, base64
cards=''.join('<article><span>'+html.escape(k)+'</span><strong>'+f'{v:,.4f}'+'</strong></article>' for k,v in metrics.items())
image=base64.b64encode((OUT/'overview.png').read_bytes()).decode()
table=summary.round(4).to_html(classes='data',border=0)
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Customer Support SLA and Backlog</title>
<style>body{font:16px system-ui;margin:0;background:#f3f5f7;color:#172c3b}main{max-width:1100px;margin:auto;padding:36px}header{border-bottom:3px solid #246577;margin-bottom:24px}small{color:#51616c}.cards{display:flex;gap:14px;flex-wrap:wrap}article{background:white;padding:18px;border:1px solid #d7e0e5;flex:1;min-width:175px}strong{display:block;font-size:27px;margin-top:12px}img{max-width:100%;margin-top:24px}table{border-collapse:collapse;background:white;width:100%;font-size:14px}td,th{padding:12px;text-align:right;border-bottom:1px solid #d7e0e5}input{padding:12px;margin:20px 0;width:280px;max-width:90%}.scroll{overflow:auto}footer{margin-top:24px}</style>
<main><header><small>TAJAMUL KHAN · DATA ANALYST PORTFOLIO</small><h1>Customer Support SLA and Backlog</h1><p>Where is the support queue missing service commitments?</p><p><b>Synthetic teaching data · Fictional 2025 case study</b></p></header><section class="cards">'''+cards+'''</section><img alt="Analysis overview chart" src="data:image/png;base64,'''+image+'''"><h2>Explore summary groups</h2><label for="filter">Filter summary rows</label><br><input id="filter" placeholder="Type a group name"><div class="scroll">'''+table+'''</div><p>SLA is measured in elapsed hours, not business hours. Resolution duration applies only to closed tickets and has survivor bias. CSAT is voluntary.</p><footer>Instagram @tajamul.codes · linkedin.com/in/tajamulkhann/</footer></main>
<script>document.getElementById('filter').addEventListener('input',function(){const q=this.value.toLowerCase();document.querySelectorAll('tbody tr').forEach(r=>r.hidden=!r.textContent.toLowerCase().includes(q))});</script></html>'''
detail_image=base64.b64encode((OUT/'detail.png').read_bytes()).decode()
page=page.replace('<h2>Explore summary groups</h2>','<h2>Analyst finding</h2><p>'+html.escape(recommendation)+'</p><img alt="Supporting analysis" src="data:image/png;base64,'+detail_image+'"><h2>Explore summary groups</h2>')
(OUT/'dashboard.html').write_text(page)
print('Saved dashboard.html, overview.png, summary.csv, metrics.json, SQL results and analysis-ready data.')
