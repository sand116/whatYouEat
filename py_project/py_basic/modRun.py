# 모듈 사용
# from mod import PI, sum, A
# print(__name__)
# import mod.PI
# print(PI)


from a.b.mod import PI

from a.b import mod
print(mod.PI)

#별칭 주기
from a.b import mod as m
print(m.PI)
# print(mod.PI) - 에러 남

import a.b.mod as m2
print(m2.PI)

# python 3.x에서 자동 지원해주는 것
#2.x에서는 안 먹힘 
# a>b>__init__.py안에 __all__=['mode']내용을 기술해야 *적용된다 
from a.b import *
print(mod.PI)




##############

##############################
#ab>__init__.py 모듈 가져오기
import a.b as bx #__init__파일은 패키지를 만들기위한 파일이기 때문에 b와 동일
print(bx.sumEx(3,4))

from a.b import sumEx
print(sumEx(5,6))

from a import *
print(Name)
