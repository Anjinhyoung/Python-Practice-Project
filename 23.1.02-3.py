x={'a':10,'b':20,'c':30}
for key in x.keys():
    print(key, end=' ')

print()

for value in x.values():
    print(value,end=' ')

print("\n한박자 쉬고")

keys=['a','b','c','d']
v={key:value for key, value in dict.fromkeys(keys).items()}
print(v)
# 이건 ppt보기

print({key:0 for key in dict.fromkeys(['a','b','c']).keys()})
# 키만 가져옴

print({value:0 for value in {'a':10,'b':20,'c':30,'d':40}.values()})
# 값을 키로 사용

print({value:key for key, value in {'a':10,'b':20,'c':30}.items()})
# 키랑 값을 바꿈

z={'a':10, 'b':20, 'c':30}
z={key: value for key,value in z.items() if value!=20}
print(z)

# 딕셔너리에서는 키를 삭제 하면 안됨

xx={'a':0,'b':10,'c':20}
yy=xx.copy()
# 딕셔너리 복사


