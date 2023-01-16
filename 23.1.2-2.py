a={"a":10,"b":20}
a.setdefault('c',30)
print(a)

a.update(a=100,c=300)   # 여러 개 고칠 수 있음
print(a)
# updata는 키가 문자열 일 때만 사용할 수 있음


print("하이요")

b={1:'1', 2:'2'}
b.update({1:'ONE',2:'TWO'}) # 숫자만 가능
print(b)

b.pop(2)
del a['a']
print(a)
print()
print(b)
# 딕셔너리 팝이랑 del은 다름
# del도 삭제 방법
b.update([['three','Three'],[4,'fivee']])
print(b)




print("몇 박자를 쉬는 거임")
# popitem은 딕셔너리에서 임의 키-값 쌍을 삭제한 뒤 삭제한 키-값-쌍을 튜플로 반환함

x={'a':10,'b':20,'c':30}
x.popitem()
z=('c',30)
print(z)
print(x)



print("헷갈려요입니다.")

# clear 사용하면 다 사라짐
print(x.get('a'))

print(x.items())
print(x.keys())
print(x.values())

keys=['a','b','c','d']
hhh=dict.fromkeys(keys)
print(hhh)

keysx=['a','b','c','d']
kkk=dict.fromkeys(keysx,100)
print(kkk)


print("몇 박자를 쉬는 가죠?")

aaa={'a':10, 'b':20,'c':30}

for key,value in aaa.items():
    print(key,value)



ccccc=dict(health=300,mana=500)
ccccc.pop('health')
print(ccccc)
