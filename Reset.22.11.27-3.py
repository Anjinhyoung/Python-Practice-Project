a=[1,2,3,4,5]
a[0:3]='a','b','c'  # 대량으로 바꾸는 법
print(a)

b=[1,2,3,4,5]
b[0:3]='a'
print(b)

c=[1,2,3]
c[0:1]='a','b','c'
print(c)

d=[1,2,3]
d.insert(0,-1)
print(d)

print("한 박자 쉬고")

g=[1,2,3,4,5]
g.extend([6,7])
print(g)

g.insert(0,0)
print(g)

# remove, pop

# remove는 숫자 그 자체를 없애주고, pop은 숫자 번호를 없애줌

abs=[1,2,5]
abs.pop(0)
abs.remove(5)
print(abs)