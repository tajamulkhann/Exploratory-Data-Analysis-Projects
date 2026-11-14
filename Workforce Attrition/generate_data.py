from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202606)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=1800
dep=rng.choice(['Engineering','Sales','Operations','Finance','Support'],n);eng=rng.integers(1,6,n)
df=pd.DataFrame({'employee_id':np.arange(n)+1,'department':dep,'tenure_years':rng.uniform(.2,12,n).round(1),'engagement_score':eng,'annual_salary':rng.integers(35000,130000,n),'exited_2025':rng.binomial(1,np.where(eng<=2,.23,.10))})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
