# kiem tra so nguyen to
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num% 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("Nhập một số nguyên dương: "))

if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
