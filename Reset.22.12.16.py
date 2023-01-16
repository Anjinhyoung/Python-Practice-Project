lux={"health":490,"mana":334, "melee":550, "armor":18.72}
print(lux)
# key:value

lux2={"health":490,"mana":334, "melee":550, "armor":18.72, "armor":18}
print(lux2)
# 이름이 중복되면 뒤에 것 표시

# 딕셔너리도 정수, 실수, 불도 포함

c={}
d=dict()

f=dict(health=490, mana=550)
# 이때 '',""를 사용하면 안됨

f['health2']=300,100
f['health3']=1000
# 이건 그냥 맨 뒤에 추가
print(f)
# dict()에서도 value값을 변경 할 때 '' or " "을 붙여줘야 함

f['health']=550
print(f)
# 아직은 이렇게 하나씩만 해야 바꿀 수 잇음

f['마나']=330
print(f)
# 이건 그냥 추가

print('마나' in f)
# 이거는 key 값만 됨
print(len(f))

f['죽고싶어요']="자살하는 방법좀"
print(f)