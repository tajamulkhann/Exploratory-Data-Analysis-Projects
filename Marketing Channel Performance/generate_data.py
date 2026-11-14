from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202603)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
rows=[]
for d in pd.date_range('2025-01-01','2025-12-31',freq='D'):
 for channel,p in [('Search',.045),('Social',.025),('Email',.06),('Display',.015)]:
  clicks=int(rng.integers(100,500)); conv=int(rng.binomial(clicks,p)); spend=round(clicks*rng.uniform(.3,1.5),2)
  rows.append([d,channel,clicks,conv,int(rng.binomial(conv,.65)),spend,round(conv*rng.uniform(45,95),2)])
df=pd.DataFrame(rows,columns=['date','channel','clicks','conversions','new_customers','spend','attributed_revenue'])
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
