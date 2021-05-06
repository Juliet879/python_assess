# question1
a = {6,7,8,9,10}
b = {5,6,7,8,9}
a.add(4)
b.add(3)
a.union(b)
a.difference(b)
b.difference(a)
a.intersection(b)

# question1
list = [11,100,99,1000,999,99]
list[0] = -1
print(list[1])
print(list[5])
print(list.count(99))
sum = 0
for number in list:
    sum+=number
print(sum)
minimum = min(list)
print(minimum)

# question3
leap = range(2020,2070)
for year in leap:
    if year%4==0 and year%100==0 and year%400==0:
        print(year)

# question4
numbers = range(1000,2000)
for num in numbers:
    if num%7==0 and num%5!=5:
        print(num)

# question5
x = 1
while x < 10:
    print("counting")
    x+=1

# question6
ultimum = range(20,30)
for num in ultimum:
    if num%2 !=0:
        print(num)

# question7
q = []
nums = range(100,200)
for item in nums:
    if item%7==0:
        q.append(item)
print(q)        

# question8
colors = range(1,50)
for color in colors:
    if color%3==0 and color%5==0:
        print("PurpleWHite")
    elif color%3==0:
        print("Purple")
    elif color%5==0:
        print("Whilte")
   