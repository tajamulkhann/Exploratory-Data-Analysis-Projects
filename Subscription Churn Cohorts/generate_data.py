from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202602)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=2200
signup=pd.to_datetime(rng.choice(pd.date_range('2025-01-01','2025-06-01',freq='MS'),n))
plan=rng.choice(['Basic','Pro'],n)
churn=np.minimum(rng.geometric(np.where(plan=='Basic',.13,.08)),13)
df=pd.DataFrame({'customer_id':np.arange(n)+1,'date':signup,'plan':plan,'first_inactive_month':churn})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
