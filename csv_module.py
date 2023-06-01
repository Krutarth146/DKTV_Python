import csv   # Comma Separted Values

filename = 'heart.csv'
fields = []
rows = []

# fp = open(filename,'r')

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)  # <_csv.reader object at 0x00000263090E1120>

    fields = next(csvreader)
    print(fields)
    print("Total No. of rows %d"%csvreader.line_num)   # 0

    for i in csvreader:
        rows.append(i)

    print(rows)

    for row in rows[:20]:
        for col in row:
            print("%10s"%col,end=' ')
        print()

    print("Total No. of rows %d"%csvreader.line_num)   # 919

print('Fields name are: ' + ', '.join(f for f in fields))

fields1 = ['Name', 'Branch', 'C_year', 'sub']

rows1 = [
    ['Dev', 'CE', '2025', '5'],
    ['Ayush', 'CE', '2026', '6'],
    ['Diya', 'IT', '2022', '7'],
    ['Yesha', 'ME', '2023', '2'],
    ['Harit', 'CE', '2028', '3'],
]

with open("student.csv","w") as csvfile1:
    csvwriter = csv.writer(csvfile1)

    csvwriter.writerow(fields1)
    csvwriter.writerows(rows1)


# Dictionary ---> Key-Value Pair

rows3 = [
    {'Name' : 'Krutarth', 'roll' : 89, 'branch' : 'CE', 'cgpa' : 8.70},
    {'Name' : 'Krutart1', 'roll' : 891, 'branch' : 'CE', 'cgpa' : 9},
    {'Name' : 'Krutart2', 'roll' : 892, 'branch' : 'CE', 'cgpa' : 6.70},
    {'Name' : 'Krutart3', 'roll' : 894, 'branch' : 'ME', 'cgpa' : 4.70},
    {'Name' : 'Krutart4', 'roll' : 896, 'branch' : 'CE', 'cgpa' : 3.70},
    {'Name' : 'Krutart5', 'roll' : 89, 'branch' : 'CE', 'cgpa' : 9.70},
]
    

fields4 = ['Name', 'roll', 'branch', 'cgpa']

filename3 = "uni_data.csv"
with open(filename3,"w") as csvfile9:
    writer = csv.DictWriter(csvfile9, fieldnames=fields4)

    writer.writeheader()
    writer.writerows(rows3)