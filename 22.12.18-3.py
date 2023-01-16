# enumerate 일단은 for이랑 같이 돌리기

a=[10,20,30,40,50]

for index,value in enumerate(a,start=1):
    print(index,value)

print("0박자 쉬고")

for b in enumerate(a,start=1):
    print(b)    #한 개만 하면 ()가 있음 # start만 고칠 수 있음 print에서 못 고침

# 파이썬 다운 방법

print("한 박자 쉬고")

b=[100,200,300,400,500]

for index,value in enumerate(b):
    print(index+1,value)

print("두 박자 쉬고")

c=[-1,-2,-3,-4,-5]

i=0

while i<len(c):
    print(c[i])
    i+=1

d=[30,20,50,700,20,1]
smallest =d[0]

for i in d:
    if i< smallest:
        smallest = i

print(smallest)

f=[50,20,30,100,200,500]

largest=f[0]

for i in f:
    if i>largest:
        largest=i

print(largest)


aaa=[100000000,1,2,3,-10000000000]
print(min(aaa))
print(max(aaa))
print("세박자 쉬고")

dict1={"이름":"안진형","나이":26,"몸무게":"56kg"}
dict2=dict(이름="안진형",나이="26",몸무게="56kg")
data=enumerate(dict1,start=1)
# 그냥 print하면 아무것도 없음

for name,b in data:
    print(name,dict1[b])

# for name,value in data:
#    print(name,":",dict1[value])

# 안진형, 26, 56kg나옴

