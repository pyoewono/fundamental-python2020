"""
Tipe data dictionary sekedar menghubungkan KEY dan Value
KVP = Key Value Pair
dictionary = kamus
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'suami': 'husband', 'ayah': 'father', 'ibu': 'mother'}

print('Kamus Ind Eng')
print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('Data ini dikirmkan oleh server gojek, untuk memberikan info di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-12-01',
    'driver_list' : ['Eko','Dwi','Tri','Catur']
}
print(data_dari_server_gojek)
print(f"Driver sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Tanggal hari ini {data_dari_server_gojek['tanggal']}")