#mport mod1 
#from mod1 import safe_sum
#print(mod1.sum1(1,2))
#print(mod1.safe_sum('hi','hello'))
#from mod1 import safe_sum, sum1
#from mod1 import safe_sum, sum1
#     모듈명 임포트할 경우에는 모듈명이 저장됨 

import mod2

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum_(1,2))
print('test.py에서 실행')

from mod2 import PI,Math,sum_
print(PI)
print(a.solv(2))
print(sum_(1,2))
print('test.py에서 실행')