def guess(number):
    if number == 5:
       return "答對了"

    if number < 10:
        return "太小了!"
    else:
        return "太大了！"

while True:
    number = int(input("請猜數字: "))
    result = guess(number)
    print(result)
