from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202601)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=6500
df=pd.DataFrame({'order_id':np.arange(n)+1,'customer_id':rng.integers(1,1301,n),'date':rng.choice(dates,n),'order_value':rng.gamma(2,65,n).round(2)})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
