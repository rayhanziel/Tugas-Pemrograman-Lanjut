import re

with open('Matrix.txt', 'r') as file:
    baris = file.readlines()

baris_pertama = baris[0].strip().split()
n = int(baris_pertama[0])
m = int(baris_pertama[1])

matriks = [baris[i+1].strip() for i in range(n)]

hasil_teks = ""
for i in range(m):
    for j in range(n):
        if i < len(matriks[j]):
            hasil_teks += matriks[j][i]

pola = r'(?<=[\w])[^\w]+(?=[\w])'
hasil_teks = re.sub(pola, ' ', hasil_teks)

print(hasil_teks)