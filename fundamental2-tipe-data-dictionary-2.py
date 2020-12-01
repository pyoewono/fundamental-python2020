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

print('\nData ini dikirmkan oleh server gojek, untuk memberikan info di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-12-01',
    'driver_list' : [
        {'nama' : 'Eko', 'jarak' : 10},
        {'nama': 'Dwi', 'jarak' : 30},
        {'nama' : 'Tri', 'jarak' : 100},
        {'nama' :'Catur' , 'jarak' : 150},
    ]
}
print(data_dari_server_gojek)
print()
print(f"Driver sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Tanggal hari ini {data_dari_server_gojek['tanggal']}")
print(f"\nDriver terdekat benama {data_dari_server_gojek['driver_list'][0]['nama']}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
print(f"\nDriver terjauh benama {data_dari_server_gojek['driver_list'][3]['nama']}")
print(f"Driver terjauh berjarak {data_dari_server_gojek['driver_list'][3]['jarak']} meter")