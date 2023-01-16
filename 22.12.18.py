# FizzBuzz 문제는 공모전 끝나고

# append는 리스트 끝에 요소 하나 추가

a=[10,20,30]
a.append(500)
print(a)

b=list()
b.append(1)
print(b)

print("한 박자 쉬고")

c=[10,20,30]
c.append([500,600])

print(c)
#d.extend([30,40,50])   # extend는 ()안에 []를 넣어야 함
#print(d)
#print(len(d))

print("두 박자 쉬고")

f=[10,20,30]
f.insert(len(f),40) # 이 기능은 잘 활용해서 잘 알기
print(f)

g=[10,20,30]
g.insert(1,[500,200])
print(g)



print("세 박자 쉬고")

h=[10,20,30]
h[1:1]=500,300          # [ ] 붙이나 안 붙이나 상관 없음
print(h)

print(len(c))

d=[10,20]
ab=[10,20,30]
ab[1:1]=[['a','b','c']]    # []  붙이나 안 붙이나 상관 없음
print(ab)

abs=[10,20,30]
abs[1:1]='a','b','c'
print(abs)
print(abs[len(abs)-1])
