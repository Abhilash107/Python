months = {'January': 1, 'February': 2, 'March': 3}

months2 = {number: name for name, number in months.items()}
#unpacks in the reverse key-pair manner
print(months2)

# What if months contained duplicate values? As these become the keys in months2,
# attempting to insert a duplicate key simply updates the existing key’s value. So if 'February'
# and 'March' both mapped to 2 originally, the preceding code would have produced
# {1: 'January', 2: 'March'}

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

avg_grades = {k: sum(v)/len(v) for k, v in grades.items()}
avg_grades2 = {}
for k, v in grades.items():
    avg_grades2.update({k:sum(v)/len(v)})
print(avg_grades)
print(avg_grades2)

# nums = {n: n**3 for n in range(1,6)}
# print(nums)# automatically assigns keys