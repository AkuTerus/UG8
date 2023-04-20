nama_file = 'nilai.txt'

handle=open(nama_file,'r')
a = 1
for line in handle:
    line = line.strip()
    if a <= 6:
        print(f'Nilai Tugas {a} : {line}')
    elif a == 7:
        print(f'Nilai Ujian Tengah Semester : {line}')
    elif a == 8:
        print(f'Nilai Ujian Akhir Semester : {line}')
    a = a+1
handle.close()
handle = open('nilai.txt','r')
bobot_nilai = [0.05, 0.05, 0.1, 0.05, 0.15, 0.1, 0.22, 0.28]
nilai = []
total = sum(bobot_nilai)
for line in handle:
    nilai.append(float(line))
if len(nilai) == len(bobot_nilai):
    total_nilai = sum([nilai[i]*bobot_nilai[i] for i in range(len(nilai))])
    nilai_akhir = total_nilai / total
    print(f'Nilai Akhir = {nilai_akhir}')
else:
    print(f'Data Salah')
handle.close()

