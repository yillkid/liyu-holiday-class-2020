def pass_check(student):
    if student["分數"] >= 60:
        return "及格"
    else:
        return "不及格"

s001 = {"name": "小花", "年級": "1年甲班", "分數":30}

result = pass_check(s001)
print(result)
