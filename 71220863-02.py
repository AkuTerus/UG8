buahlist = []
handle = open('buah.txt', "r")
for line in handle:
    buahlist.append(line.strip())
handle.close()
print('~~~~~~~~~~~ Buah yang tersedia ~~~~~~~~~~~')
handle=open('buah.txt','r')
for line in buahlist:
    print(line.strip())
handle.close()
hapus_buah = input('Masukan Buah yang mau di hapus : ')
if hapus_buah in buahlist:
        buahlist.remove(hapus_buah)
        print(f'Buah {hapus_buah} sudah terhapus')
else:
        print(f'{hapus_buah} tidak ada dalam file')
handle = open('buah.txt','w')
for line in buahlist:
    handle.write(line + '\n')
handle.close()