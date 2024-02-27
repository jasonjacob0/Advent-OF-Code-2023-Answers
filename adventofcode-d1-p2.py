p = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
f = p.replace('two','t2o').replace('nine','n9e').replace('one','o1e').replace('three','t3e').replace('four','f4r').replace('five','f5e').replace('six','s6x').replace('seven','s7n').replace('eight','e8t')
result =[]
for i in f.split('\n'):
    a = [int(j) for j in i if j.isdigit()]
    if len(a)>=1:
        result.append(a[0]*10+a[-1])
print(sum(result))
