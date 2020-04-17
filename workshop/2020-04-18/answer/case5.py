def guess(number):
    if number == 3:
        return "答對了!"
    else:
        return "答錯了！"

for index in range(3):
    number = int(input("請猜數字: "))
    result = guess(number)
    print(result)
