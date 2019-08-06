#data01.py
import numpy as np
import pandas as pd

s=pd.Series([1,3,5,np.nan,6,8]) #np.nan는 숫자가 아닌것이 들어있다는말 nan은 결측치
print(s)
#numpy는 주로 배열을 컨트롤
#pandas - 데이터 분석 통계(주로 2차원 설계)
dates=pd.date_range('20130101',periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4), index=dates,columns=['A','B','C','D']) #row, colum
print(df)
# jupyter notebook ->브라우저 실습
df.head(3)
df.index
df.columns
df.values
df.info
print(df.describe())

#               A         B         C         D
# count  6.000000  6.000000  6.000000  6.000000
# mean  -0.111961  0.340303  0.421309 -0.223080
# std    1.359790  1.001487  1.087335  1.243388
# min   -1.349969 -0.771991 -0.677043 -1.940744
# 25%   -1.131170 -0.450483 -0.391569 -1.049502
# 50%   -0.643682  0.178835  0.269222 -0.129677
# 75%    1.041134  1.202033  0.871777  0.691298
# max    1.656496  1.573297  2.205656  1.252770
# count가 전체 열 수와 같으면 결측치가 없다는 말
# std 표준편차

df.sort_values(by='B'.ascending=False) #큰값에서 작은값으로 
df['A'] #A컬럼만 보고싶다.
df[0:2] #데이터 개수(row기준) 0,1
df['20130102':'20130104']

