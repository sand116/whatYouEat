import numpy as np
import pandas as pd

df=pd.read_csv('datasets/supplier_data.csv') #메모리에 자동으로 다 올려줌
print(df)

df.to_csv("outputs/output02.csv",index=False) 