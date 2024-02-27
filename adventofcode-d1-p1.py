a =''' 1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

p = a.split("\n")
result=[]
for i in p:
    k = [int(j) for j in i if j.isdigit()]
    if len(k)>=1:
        result.append(k[0]*10+k[-1])
print(result)
print(sum(result))
        