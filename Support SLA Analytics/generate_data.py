from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202609)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=3500
created=pd.to_datetime(rng.choice(pd.date_range('2025-12-01','2025-12-31 23:00',freq='h'),n));priority=rng.choice(['High','Medium','Low'],n,p=[.2,.5,.3]);response=rng.exponential(9,n).round(2);duration=response+rng.exponential(70,n)
snapshot=pd.Timestamp('2026-01-01'); age=(snapshot-created).total_seconds()/3600
resolved=duration<=age; response=np.where(response<=age,response,np.nan)
df=pd.DataFrame({'ticket_id':np.arange(n)+1,'date':created,'priority':priority,'first_response_hours':response,'resolution_hours':np.where(resolved,duration,np.nan),'csat':np.where(resolved&(rng.random(n)<.55),rng.integers(1,6,n),np.nan)})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
