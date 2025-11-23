import csv

data = [
    {'ACC_ID': '1001', 'NAME': 'ARYAN', 'ACC_NUMBER': '10196', 'PIN': '1204', 'BALANCE': '10000.00'},
    {'ACC_ID': '1002', 'NAME': 'SIDHHART', 'ACC_NUMBER': '19567', 'PIN': '1946', 'BALANCE': '15800.00'},
    {'ACC_ID': '1003', 'NAME': 'YUVRAJ', 'ACC_NUMBER': '78546', 'PIN': '1256', 'BALANCE': '17000.00'},
    {'ACC_ID': '1004', 'NAME': 'HRITIK', 'ACC_NUMBER': '62345', 'PIN': '1241', 'BALANCE': '19300.00'},
    {'ACC_ID': '1005', 'NAME': 'GURJAPNEET', 'ACC_NUMBER': '17249', 'PIN': '1232', 'BALANCE': '1900.00'},
    {'ACC_ID': '1006', 'NAME': 'RUTURAJ', 'ACC_NUMBER': '18349', 'PIN': '1198', 'BALANCE': '15030.00'},
    {'ACC_ID': '1007', 'NAME': 'ROHIT', 'ACC_NUMBER': '19624', 'PIN': '1143', 'BALANCE': '25700.00'},
    {'ACC_ID': '1008', 'NAME': 'SURESH', 'ACC_NUMBER': '18567', 'PIN': '1982', 'BALANCE': '12880.00'},
    {'ACC_ID': '1009', 'NAME': 'ABHIJEET', 'ACC_NUMBER': '56832', 'PIN': '1221', 'BALANCE': '16000.00'},
    {'ACC_ID': '1010', 'NAME': 'ROSHAN', 'ACC_NUMBER': '19074', 'PIN': '1217', 'BALANCE': '13000.00'},
]

fieldnames = ['ACC_ID', 'NAME', 'ACC_NUMBER', 'PIN', 'BALANCE']
file_name = 'accounts.csv'

with open(file_name, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader() 
    writer.writerows(data) 

print(f"File '{file_name}' created successfully.")
