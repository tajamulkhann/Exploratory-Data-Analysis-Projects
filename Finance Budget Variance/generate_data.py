from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202607)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
rows=[]
for d in pd.date_range('2025-01-01','2025-12-01',freq='MS'):
 for unit in ['Consumer','Business','Enterprise']:
  for account,base in [('Revenue',150000),('COGS',80000),('Opex',42000)]:
   budget=round(base*rng.uniform(.85,1.15),2);actual=round(budget*rng.uniform(.85,1.2),2);rows.append([d,unit,account,budget,actual])
df=pd.DataFrame(rows,columns=['date','business_unit','account','budget','actual'])
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
