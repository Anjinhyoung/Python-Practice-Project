a=list()

for i in range(10):
    a.append('a')

print(a)

b=list()
for i in range(3):
    line=[]                 # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)      # 안쪽 리스트에 0 추가
    b.append(line)          # 전체 리스트에 안 쪽 리스트 추가
                    # append에 리스트를 넣으면 리스트 안에 리스트가 들어가는 특성을 이용함
print(b)

print("한 박자 쉬고")

aaa=[['c' for j in range(2)] for i in range(3)]
print(aaa)


c=[3,1,3,2,5]           # 가로 크기를 저장한 리스트
d=[]                    # 빈 리스트 생성

for i in c:             # 가로 크기를 저장한 리스트로 반복
    line2 =[]           # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):      # 리스트 a에 저장된 가로 크기만큼 반복
        line2.append(5)
    d.append(line2)         # 리스트 b에 안쪽 리스트를 추가가

print(d)

print("두 박자 쉬고")

ccc=[[10]*i for i in [3,1,3,2,5]]
print(ccc)

f=[[10,20],[30,40]]
g=f
g[0][0]=500
print(f)
print(g)

# 2차원 리스트를 완전히 복사할라면 deepcopy 함수를 사용해야 함

fff=[[10,20],[30,40]]
import copy
ggg=copy.deepcopy(fff)
ggg[0][0]=500
print(fff)
print(ggg)







