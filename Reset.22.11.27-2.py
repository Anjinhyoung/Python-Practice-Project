a=[10,20,30]

print(30 in a)

print(10 not in a)

# 튜플이랑 문자열도 가능함

b="python"
print("p" in b)

c=[1,2,3]
d=[5,5]
f=c+d
print(f)
# 튜플도 가능함

# range는 리스트처럼 더할 수 없음 but list안에   range는 가능함 튜플도 가능함


e=[1,2,3]*3
print(e)
# range는 위와 마찬가지로 리스트랑 튜플이랑 같이 써야 함

print(len(e)) # 개수 알아보는 법
# len은 그냥 range에다 해도 상관 없음

f=[1,2,3,4,5]
print(f[0]) # 0번째  숫자 찾는 법

g=(1,2,3,4,5)
print(g[0]) # [ ]를 작성해야 해당 번호 숫자를 알 수 있음, range도 len이랑 같이 그냥 해도 돼, 문자열도

ab=[0,0,0,0,0]
ab[0]=1
ab[1]=2
print(ab)

del ab[4]
print(ab)