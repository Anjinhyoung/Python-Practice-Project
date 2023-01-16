#for i in range(11,3,-2):
#    print(i,"hello world")

for k in reversed(range(3)):
    print(k,"hello")

a=['a','b','c'] # 튜플도 가능함
for q in a:
    print("안녕하세요!!")

print("한번 쉬기")

b='python'
for d in b:
    print(d,end=" ")

print()

#count=int(input("반복할 숫자를 입력하세요:"))

#for j in range(count):
#    print(j,"반복")

i=0     # 초기식

while i<5: # while 조건식
    print("hello world") # 반복할 코드
    i+=1 # 변화식

# while은 변화식이 필요함

#count = int(input("반복할 횟수를 입력하세요: "))

#k=10

#while k > count:
#    print("반복할 숫지", k)
#    k-=1



import random
print(random.random()) # 0.0<=x <1.0
#random.uniform(1,10) 1.0=<a<10.0

# print(random.randint(3,100))
print(random.randrange(1,2,1)) # 1이상 7미만
print(random.choice('choice'))
o=0
while o!=2:
    o=random.randint(1,2) #1이상 3이하
    print("안녕하세요",o)
 #무수한 숫자가 반복

# while True:
#    print("무한 반복")
# 0이 아닌 숫자는 True, 내용있는 건 True로 취급
# while은 반복 횟수가 안 정해져 있을 때 for 반복문은 반복 횟수가 정해져 있을 때

# count=int(input("숫자를 입력하세요:"))

# k=10

# while count<10:
#	print("hello world",count)
#	count+=1