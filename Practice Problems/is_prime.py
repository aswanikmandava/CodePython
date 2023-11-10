def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2
    temp = num / 2
    print(f"{div} <= {temp} {div <= temp}")
    while div <= temp:
        if num % div == 0:
            return False
        div += 1

    return True

i = 2
while i < 20:
    print(f"{i} is prime? {is_prime(i)}")
    i += 1