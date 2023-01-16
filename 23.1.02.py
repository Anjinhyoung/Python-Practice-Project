name='maria'
print('i am %s' % name)
# print('i am %s' %'name') 이것도 됨

print('i am %d old'%30)

agge=20

print('i am %d years  old' %agge)

# 실수는 %f

ooonth=3
day='April'

print('Today is %d %s'%(30,''))

print('hello, {0} {1} {2}'.format('world','Script',3.6))

print('hello, {a} {b} {c}'.format(a='world',b='Script',c=3.6))
# 문자열로 할 때 뒤에도 문자열로 해야 함

print("몇 박자를 쉬는 거야")

print('hello, {0} {0} {2}'.format('world','Script',3.6))

print('hello, {} {} {}'.format('world','Script',3.6))

language='python'
version=3.6

print(f'Hello, {language} {version}')
# 이거는 무조건 변수가 있어야 함

# 이 부분은 아직 이해가 안 됨

print('{0:03d}'.format(1))


print('{0:03.3f}'.format(150.37))

