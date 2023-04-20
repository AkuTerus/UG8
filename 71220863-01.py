carikata = input('Masukan kata yang di cari : ')
carikatalower = carikata.lower()
handle = open('romeojuliet.txt','r')
hitung = 0 
for line in handle:
    line = line.lower()
    hitung = hitung + line.count(carikatalower)
handle.close()
print(f'kata {carikata} jumlahnya = {hitung}')