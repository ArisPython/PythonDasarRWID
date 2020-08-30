# konstruksi dasar python
# sequential = eksekusi berurutan
# print('hello world')
# print('by aris winandi')
# print('semarang')

#percabangan
# ingin_cepat = True
# if ingin_cepat:
#     print('jalan lurus aja')
# else:
#     print('belok ke kanan')


#perulangan
# jumlah_anak = 4
# for index_anak in range (1, jumlah_anak+1):
#     print(f'Halo anak #{index_anak}!')

#List (array)
# nama = ['sari','fahri','susi','andi','herman']
# nama.append('yudi') #append untuk menambahkan list
# print(nama[0])

#menampilkan data dari list
# for a in nama:
#     print(f'hay {a}')
# print('\n')

#menampilkan data dari list : cara ribet
# for a in range (0, len(nama)):
#     print(f'{a+1}.hay {nama[a]}')

#Dict
kamus={'anak':'son','ayah':'father','ibu':'mother','paman':'uncle'}
print(kamus['ayah'])
#output: father

server_gojek = {
    'tanggal':'2020-06-20',
    'driver_list': [
        {'nama':'eko','alamat':'semarang','jarak':'10'},
        {'nama':'aris','alamat':'tuban','jarak':'5'},
        {'nama':'yudha','alamat':'tangerang','jarak':'4'},
        {'nama':'bima','alamat':'jakarta','jarak':'7'},
        {'nama':'asrani','alamat':'surabaya','jarak':'6'}
    ]
}

print(f"driver disekitar sini{server_gojek['driver_list']}")
print(f"driver ke #4 adalah {server_gojek['driver_list'][4]}")
print(f"driver ke#2 adalah {server_gojek['driver_list'][2]}")
print(f"driver ke#0 adalah {server_gojek['driver_list'][0]}")
print(f"alamat driver {server_gojek['driver_list'][0]['nama']} adalah {server_gojek['driver_list'][0]['alamat']}")