from pathlib import Path
import numpy as np
import pandas as pd
rng=np.random.default_rng(202604)
dates=pd.date_range('2025-01-01','2025-12-31',freq='D')
n=9000
device=rng.choice(['Mobile','Desktop','Tablet'],n,p=[.6,.32,.08]);view=rng.binomial(1,.76,n);cart=view*rng.binomial(1,.38,n);checkout=cart*rng.binomial(1,.72,n);purchase=checkout*rng.binomial(1,np.where(device=='Mobile',.51,.72))
df=pd.DataFrame({'session_id':np.arange(n)+1,'date':rng.choice(dates,n),'device':device,'visit':1,'product_view':view,'add_to_cart':cart,'checkout':checkout,'purchase':purchase})
if __name__ == '__main__':
    df.to_csv(Path(__file__).parent/'data'/'raw.csv',index=False)
    print('Generated',len(df),'synthetic rows')
