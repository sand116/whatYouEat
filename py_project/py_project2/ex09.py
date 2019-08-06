import pandas as pd 
input_file="datasets/supplier_data.csv"
output_file="outputs/output03.csv"
df=pd.read_csv(input_file)
print(df)
df['Cost']=df['Cost'].str.strip('$').astype(float)
#함수형 언어의 좋은 방식은 ...으로 계속 연결할 수 있음
print(df)
df2=df.loc[df['Supplier Name'].str.contains('Z') | (df['Cost']>600.0), :['Supplier Name','Cost']] #loc 로케이션 [[컬럼명조건],]
print(df2)

df2.to_csv(output_file,index=False)
#[row값,colum값] (row중에서 z를 포함하고 cost가 600이상인 모든 컬럼을 추출해라)