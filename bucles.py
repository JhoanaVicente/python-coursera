def sum_divisors(number):
    divisor = 1
    total = 0

    if number < 1:
        return 0

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1  # Movido fuera de la condición

    return total

def format_divisor_sum(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(str(i))
    return "+".join(divisors)

print(sum_divisors(0))  # Should print 0
print(sum_divisors(3))  # Should print 1
print(format_divisor_sum(36))  # Should print 1+2+3+4+6+9+12+18
print(format_divisor_sum(102))  # Should print 1+2+3+6+17+34+51


