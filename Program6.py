import os
data={}
def tambah():
    print(f"{'Tambah Data':^17}")
    print('='*17)
    nama = str(input('Nama\t\t: '))
    nim = str(input('NIM\t\t: '))
    uts = int(input('Nilai UTS\t: '))
    uas = int(input('Nilai UAS\t: '))
    tugas = int(input('Nilai Tugas\t: '))
    akhir = round(float((tugas*0.3)+(uts*0.35)+(uas*0.35)),2)
    data[nama]=nim, uts, uas, tugas, akhir
def tampilkan():
    print(f"{'Daftar Data Mahasiswa':^82}")
    print('='*84)
    print(f"|{'NO':^4}|{'NIM':^20}|{'NAMA':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
    print('='*84)
    n = 0
    for a in data.items():
        n += 1
        print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"
        .format(a[1][0], a[0][:13], a[1][1], a[1][2], a[1][3], a[1][4], no = n))
    print('='*84)

def hapus(nama):
    print(f"{'Data Berhasil di Hapus':^17}")
    print('='*17)
    del data[nama]

def ubah(nama):
    print(f"{'Ubah Data':^17}")
    print('='*17)
    nim = str(input('NIM\t\t: ')) 
    uts = int(input('Nilai UTS\t: '))
    uas = int(input('Nilai UAS\t: '))
    tugas = int(input('Nilai Tugas\t: '))
    akhir = round(float((tugas*0.3)+(uts*0.35)+(uas*0.35)),2)
    data[nama] = nim, uts, uas, tugas, akhir

def salah():
    print(f"{'Daftar Data Mahasiswa':^82}")
    print('='*84)
    print(f"|{'NO':^4}|{'NIM':^20}|{'NAMA':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
    print('='*84)
    print(F"|{'Tidak ada data':^82}|")
    print('='*84)
      
while True:
    print()
    lanjut = str(input('MENU\n=======\n(L)ihat\n(T)ambah\n(U)bah\n(H)apus\n(K)eluar\n=======\nPilihan : '))
    os.system("cls")
    if lanjut.lower() == 'l':
        if data.items():
            tampilkan()
        else:
            salah()
    elif lanjut.lower() == 't':
            tambah()
    elif lanjut.lower() == 'h':
        print('Data yang ingin di Hapus')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            hapus(nama)
        else:
            salah()
    elif lanjut.lower() == 'u':
        print('Data yang ingin di Ubah')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            ubah(nama)
        else:
            salah()
    elif lanjut.lower() == 'k':
        break
    else :
        print('Pilih menu yang tersedia')