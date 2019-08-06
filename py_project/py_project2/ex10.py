import pandas as import pd
import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
data_frame=pd.read_excel(input_file,sheetname='january_2013')
writer=pd.ExcelWriter(output_file)
data_frame.to_excel(writer,sheet_name='jan_13_output',index=False)
writer.save()
#특정 조건을 충족하는 행의 필터링
#특정 집합의 값을 포함하는 행의 필터링
#패턴을 활용한 필터링
#열의 인덱스 값을 사용하여 특정 열 선택하기