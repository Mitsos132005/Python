list1 = [1,2,3]

print(list1)
m=1
for i in range(16):
    m=70+i
    list1.append(m)
print(list1)

n=2
for j in range(3):
    n=n+1
    l=j+4
    list1.insert(n,l)

print(list1)