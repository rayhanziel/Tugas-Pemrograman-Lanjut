# Part A
def print_square_values(n):
    for i in range(n):
        print(i ** 2)

# Contoh penggunaan untuk Part A
n = int(input("Masukkan nilai n: "))
print_square_values(n)

# Part B
def print_odd_squares(n):
    for i in range(n):
        if i % 2 != 0:
            print(i ** 2)

# Contoh penggunaan untuk Part B
n = int(input("Masukkan nilai n: "))
print_odd_squares(n)
