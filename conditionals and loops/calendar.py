year = int(input("enter year"))
mon = 0
months=[32, 29,32,31,32,31,32,32,31,32,31,32]
index = (5*((year-1)%4)+4*((year-1)%100 )+6*((year-1)%400 ))%7
print("calender for January", year)
print("mo\ttu\twe\tth\tfr\tsa\tsu")
for i in range(32-index,32):
    print(i, end="\t")
  
for j in range(1,months[mon]):
    if((index+j)%7==0):
        print(j)
    else:
        print(j, end="\t")    