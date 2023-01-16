i=0
while True:
    print(i)
    i += 1 # 얘 떄문에 5까지 안 감
    if i==5:
        break

# break는 반복문 끝내기기
print()

for k in range(7):
    print(k)
    if k==5:
        break

for n in range(10):
    if n%2==0:
        continue
    print(n)

print("a 시작합니다.")

a=1
while a<10:
    a += 1
    if a%2==0:
        continue
    print(a)




# a=0
# while a<10:
    # if a%2==0:
        # continue
    # print(a)
    # a += 1

# 이렇게는 안됨




# count = int(input("반복할 횟수를 입력하세요:"))
# b=0
# while True:
#     print(b)
#     b+=1
#     if b== count:
#         break
# count = int(input("반복할 횟수를 입력하세요:"))
# for i in range(count+1):
#     if i%2==0:
#         continue
#     print(i)