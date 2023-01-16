a=[[10,20],[30,40],[50,60]]


b=[[10,20],
   [30,40],
   [50,60]]
print(b)

# 똑같이 나옴

print(a[0][0])
print(a[0][1])
print(a[2][1])

print("0박자 쉬고")

#  a[0][0]  a[0][1]

#   10         20
#   30         40
#   50         60

# 1차원 리스트는 x,y가 안됨

for x,y in a:
    print(x,y)
# 2행 2열일 때만 가능
print("한 박자 쉬고")

for i in a: # 안쪽 리스트를 꺼냄
    for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j,end=' ')
    print() #  end 때문에 계속 붙어서 한 번 띄어주는 역할이 필요함

print("두 박자 쉬고")


for i in range(len(a)): # 세로 크기, i는 0,1,2이 이렇게 됨
    for j in range(len(a[i])):  #가로 크기
        print(a[i][j],end=' ')
    print()
    
print("세 박자 쉬고")

i=0

while i < len(a):   # 세로 크기
    x,y=a[i]
    print(x,y)# 요소 두 개를 한꺼번에 가져오기
    i+=1
    # 2행 2열일 때만 가능

print("네 박자 쉬고")

k=0

while k<len(a): # 세로 크기
    j=0
    while j<len(a[k]): # 가로 크기
        print(a[k][j], end=' ')
        j+=1    # 가로 인덱스를 1 증가시킴
    print()
    k+=1    # 세로 인덱스를 1 증가시킴


b=[[0,20,40,50,60],[30,40],[50,60],[20,30,50,100]]

for i in range(len(b)): # 세로 크기, i는 0,1,2이 이렇게 됨
    for j in range(len(b[i])):  #가로 크기
        #print(b[i][j],end=' ')
        print(b[i][j],end=" ")
    print()






