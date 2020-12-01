print('\ntipe data list/array/daftar')
anak = ['Eko','Dwi','Tri','Catur']
print(anak)
anak.append('Panca')
print(anak)

print('\nSapa Anak ke dua')
print(f'Hai {anak[1]}')
print('Hai', anak[1])

print('\nSapa Semua Anak')
for n in anak:
    print(f'Hai {n}!')

print('\nSapa Semua Anak ribet')
for a in range(0,len(anak)):
    print(f'{a+1}. Hai {anak[a]}')

print(['Eko','Dwi','Tri','Catur'][2])

