import os
tempat_file= input("Masukan Path :")

res = os.listdir(tempat_file)
# print(res)

FILE= []
NAMA_FILE = []
for  index,value in enumerate(res):
    print(index, value)
    FILE.append(value)

for x in range(806, 866):
    for index, value in enumerate(res):
        NAMA_FILE.append(f'{x}-{value}')
# os.system(["C:\xampp2\xampp-control.exe"])

print(NAMA_FILE)