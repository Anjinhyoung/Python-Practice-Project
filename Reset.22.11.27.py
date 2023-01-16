# abc="""hello
# world
# 헬로우"""
# ''' ''' = """ """ 같은 기능

# print(abc)

# ab=" '안녕하세요' "
# print(ab)

# cb= ' "안녕하세요" '
# print(cb)

# 리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 넣을 수 있으
a=['james',17,17.5,True]
print(a)

b=[]
c=list()
# b,c 는 빈 리스트 만드는 법



abs=range(0,15)
# range 자체는 뭐 없음 (리스트랑 튜플 안에 넣어야 함 그냥 print해도 안돼)
ddd=list(abs)
print(ddd)

d=[range(0,10)]
print(d)

# 빈 리스트에다 넣은 거지만 둘이 확실히 다름

e=list(range(0,10))
print(e)
print("한 번 쉬고")
# 이게 더 정확

f=(1,2,3,5,6)
print(f)
# 튜플도 list처럼 여러 자료형을 섞어도 괜찮음

# 요소가 한 개인 튜플

g=(1,)
print(g)

h=tuple(range(10))
print(h)

i=[1,2,3]

print(tuple(i))

k=(1,2,3)
print(list(k))
#이렇게 하는 게 맞음

j=(5,5,5)
list(j) # 그냥 보여주기 식 막상 print(j)하면 나오지 않음 print 안에다가 넣어야 함
print(j)
# 이렇게 하면 안됨
