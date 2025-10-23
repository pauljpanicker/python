attendance = [18, 20, 19, 15, 21]
count_t=0
for x in attendance:
    if x>=20:
        print("class is full")
        count_t=count_t+1
    else:
       print("class is not full")
print("the total day of class full:",count_t)
total_day=sum(attendance)
print("sum of total day attendance:",total_day)