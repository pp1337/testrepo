bin_str = input("Введите число:")
decyat_num = 0
length = len(bin_str)

for i, char in enumerate(bin_str):
    digit = int(char)
    razryad = length - i - 1
    decyat_num += digit * (2 ** razryad)

print(decyat_num)