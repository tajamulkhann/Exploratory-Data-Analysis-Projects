from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202600)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=6000
df=pd.DataFrame({'line_id':np.arange(n)+1,'date':rng.choice(dates,n),'category':rng.choice(['Electronics','Home','Clothing','Grocery'],n),'region':rng.choice(['North','South','East','West'],n),'quantity':rng.integers(1,6,n),'unit_price':rng.uniform(15,250,n).round(2),'discount':rng.choice([0,.05,.15,.30],n),'unit_cost_ratio':rng.uniform(.45,.85,n),'returned':rng.binomial(1,.07,n)})
df['unit_cost']=(df.unit_price*df.pop('unit_cost_ratio')).round(2)
df=pd.concat([df,df.iloc[:12]],ignore_index=True)
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
