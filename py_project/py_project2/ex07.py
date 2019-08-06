import sys
input_file='datasets/supplier_data.csv'
output_file='outputs/output01.csv'
# 쉼표를 기준으로 구분
with open(input_file,'r') as filereader :
    with open(output_file,'w') as filewriter :
        header  = filereader.readline() ( #한줄읽기)
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader :
            row=rwo.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')