from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202605)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=2600
ordered=rng.integers(20,250,n);lead=rng.integers(2,16,n)
df=pd.DataFrame({'po_id':np.arange(n)+1,'date':rng.choice(dates,n),'supplier':rng.choice(['Aster','Beacon','Cedar','Delta'],n),'ordered_units':ordered,'delivered_units':np.maximum(0,ordered-rng.choice([0,0,0,5,15],n)),'promised_days':lead,'actual_days':np.maximum(1,lead+rng.integers(-2,5,n)),'stock_units':rng.integers(10,800,n),'daily_demand':rng.integers(5,65,n)})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
