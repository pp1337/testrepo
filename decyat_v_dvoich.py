decyat = int(input("введите число: "))
result = ""

while decyat > 0:
    result = str(decyat % 2) + result
    decyat = decyat // 2

print(result)