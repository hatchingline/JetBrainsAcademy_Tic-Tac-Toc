prime_numbers = [num for num in range(2, 1001) if all(num % factor for factor in range(2, num))]
