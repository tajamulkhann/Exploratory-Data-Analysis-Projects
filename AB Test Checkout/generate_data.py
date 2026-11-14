from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202608)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=12000
arm=rng.choice(['Control','Treatment'],n)
df=pd.DataFrame({'user_id':np.arange(n)+1,'variant':arm,'converted':rng.binomial(1,np.where(arm=='Treatment',.128,.11))})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
