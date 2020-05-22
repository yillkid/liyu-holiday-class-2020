from students import *

def pass_check(student):
    if student["分數"] >= 60:
        return "及格"
    else:
        return "不及格"

s001["分數"] = 60
result = pass_check(s001)
print(result)
