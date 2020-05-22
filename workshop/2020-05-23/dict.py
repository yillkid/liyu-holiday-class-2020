from students import *

def pass_check(student):
    if student["分數"] >= 60:
        return "及格"
    else:
        return "不及格"

# 在這裡設定分數?

result = pass_check(s001)
print(result)
