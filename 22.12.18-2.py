a=[10,20,30]
a.pop(1)
print(a)
# 중간에 삭제되서 [10,30]만 남음
del a[0]    # del을 사용해도 상관없음
print(a)

b=[10,20,30]
b.remove(10)
print(b)
# 만약에 리스트에 20이 중독으로 되어있을 경우 첫 번째 20을 삭제함


print("한 박자 쉬고")
c=[10,20,30,40,50]
print(c.index(30))

d=[50,40,30,20,10]
d.reverse()
print(d)


f=[3,2,5,7,1,8,10,20]
f.sort()
print(f)


print("두 박자 쉬고")

g=[10,20,30]
g.clear()
print(g)
# 빈 리스트만 뜸 []

ab=[10,20,30]
ab[len(ab):]='안녕하세요' # 문자는 그냥 넣어도 되지만 숫자는 무조건 [] 붙여야 함 문자열을 쓰면 '안','녕','하','세','요'가 나옴
print(ab)

ac=[10,20,30]
ac[len(ac):]=40,50
print(ac)

ad=[0,0,0,0,0]
af=ad
print(af)
# 리스트는 두 개 인 것 같지만 실제로는 리스트는 한 개임

af[1]=1
print(af)

# 완전히 두 개로 만드는 법

bb=[0,0,0,0,0,0,0]
cc=bb.copy()
#  이렇게해야 리스트가 두 개 됨
# cc에 리스트를 추가해도  bb에는 영향을 미치지 않음

aaa=[1,2,3]
aaa[0]="안녕하세요"
print(aaa)

