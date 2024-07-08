def mystery(n, m):
  p = 0
  e = 0
  while m > 0:
    p = p + n
    m = m - 1
    print(p, m)  # Menampilkan nilai p dan m pada setiap iterasi
  return p

hasil = mystery(4, 3)
print(hasil)
