def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return None

# Contoh penggunaan
vals1 = [101, 4, 12, 24]
print(pembagi_indeks1(vals1, 2))  # Output: 1

vals2 = [100, 66, 55, 64, 41, 35, 18, 64]
print(pembagi_indeks1(vals2, 5))  # Output: 2
