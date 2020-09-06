# from geometri.fungsi_luas import fungsi_luas_segitiga as s3, fungsi_luas_segipanjang as s4

# print(f'luas segitiga adalah {s3(10,35)}')
# print(f'luas segiempat  adalah {s4(10,6)}')
from geometri.persegiPanjang import PersegiPanjang
from geometri.segiTiga import SegiTiga

print('menghitung persegi panjang')
p1 = PersegiPanjang(20, 30)  # p1 adalah object yang memanggil class PersegiPanjang()
print(p1.info())
print(p1.hitung_luas())

s1 = SegiTiga(10,20)
print(s1.info())
print(s1.hitung_luas())

