# record = {'1001' : {'pName' : "5 Star", 'qn' : 90, 'price' : 20},
#           '1002' : {'pName' : "Parle G", 'qn' : 202, 'price' : 5},
#           '1003' : {'pName' : "Oats", 'qn' : 400, 'price' : 30},
#           '1004' : {'pName' : "Kellogs", 'qn' : 220, 'price' : 60}}
import json

f1 = open("record.txt","r")
temp = f1.read()
record = json.loads(temp)
f1.close()



# print(record)
# print(record['1003']['price'])  # 30
# print(record['1004']['pName'])  # Kellogs

print("-------------Menu--------------")


for i in record.keys():
    print(i,"--->",record[i]['pName'], '||', record[i]['qn'], '||',record[i]['price'])


user_need =  input("Enter Product Id: ")
quantity = int(input("Enter Quantity: "))

if quantity <= 0:
    print("pls Enter valid Quantity.")
    exit()

total_bill = 0
if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print("Your Bill Amount is",total_bill)
    print("Thank you! Inventory Updated !!!")
else:
    print(f"We have only {record[user_need]['qn']} Quantities.")
    temp = input("If you need then Press Y or y: ")
    if temp.lower() == 'y':
        total_bill = record[user_need]['qn'] * record[user_need]['price']
        record[user_need]['qn'] = 0
        print("Your Bill Amount is",total_bill)
        print("Thank you! Inventory Updated !!!")
    else:
        print("Thank You! Visit Again!")

print(record[user_need]['qn'])


# File   w, r, a, x, t, b, +

fp = open("record.txt","w")
js = json.dumps(record)
fp.write(js)
fp.close()

# Task
# Bill ---> Userid or Name, date, billamount in different File