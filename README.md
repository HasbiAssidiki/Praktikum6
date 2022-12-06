# Praktikum6
## PROGRAM INPUT NILAI MAHASISWA MENGGUNAKAN SYNTAX FUNGSI 
## PENJELASAN PROGRAM
Fungsi secara singkat yakni meringkas sebuah program yang berulang-ulang dengan menggunakan syntaks def nama_fungsi(argument). def diartikan sebagai definisi.
1. Kita akan mendeklarasikan atau menginput sebuah variabel bertipe data dictionary kosong `data={}` yang nantinya akan kita inputkan sebuah data yang terdiri dari: nama, nim, nilai_tugas, nilai_uts, nilai_uas dan nilai_akhir.
2. Membuat fungsi
* Fungsi tambah(), untuk menambahkan data `def tambah()`
* Fungsi tampilkan(), untuk menampilkan data `def tampilkan()`
* Fungsi hapus(nama), untuk menghapus nama pada data `def hapus(nama)`
* Fungsi ubah(nama), untuk mengubah nama pada data `def ubah(nama)`
* Fungsi salah(), untuk inputan yang tidak sesuai perintah `def salah()`
3. Menggunakan Perulangan while (while loop)
`while True:`, dapat diartikan perulangan akan terus mengulang jika inputan benar dan masuk kedalam proses jika tidak maka perulangan berhenti atau lanjut ke proses selanjutnya. 
variabel *lanjut* kita gunakan untuk menginput perintah yang akan kita proses `lanjut=input(str('(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar))`, disini kita menggunakan statement if untuk memproses perintah yang di inginkan sesuai inputan pada variabel *lanjut*:
* `if lanjut.lower() == 'l':`

    `if data.items():`

      `tampilkan()`

    `else:`

      `salah()`

* `if lanjut.lower() == 't':`

    `tambah()`

* `if lanjut.lower() == 'h':`

    `nama = input(str('Nama\t: '))`

    `if nama in data.items():`

      `hapus(nama)`

    `else:`

      `salah()`

* `if lanjut.lower == 'u':`

    `nama = input(str('Nama\t: '))`

    `if nama in data.items():`

      `ubah(nama)`

    `else:`

      `salah()`

### CODE PROGRAM
```python
import os
data={}
def tambah():
    print(f"{'Tambah Data':^17}")
    print('='*17)
    nim = str(input('NIM\t\t: '))
    nama = str(input('Nama\t\t: '))
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
        print('Data yang ingin di hapus')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            hapus(nama)
        else:
            salah()
    elif lanjut.lower() == 'u':
        print('Data yang ingin di hapus')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            ubah(nama)
        else:
            salah()
    elif lanjut.lower() == 'k':
        break
    else :
        print('Pilih menu yang tersedia')
print('Program Selesai') 
```  

## Hasil Program  
### Tambah Data (T) & Lihat (L)  
![Screenshot (62)](https://user-images.githubusercontent.com/115614317/205920956-951d0f58-f553-4b15-814e-d4e37319d9fc.png)  
![Screenshot (71)](https://user-images.githubusercontent.com/115614317/205921021-771d697e-92ec-44bf-8a16-a929b52e6d04.png)  
![Screenshot (72)](https://user-images.githubusercontent.com/115614317/205921512-69ed7bfd-e0d1-4cd5-a739-8739ed65d413.png)  
### Ubah Data (u) & Lihat (L)  
![Screenshot (73)](https://user-images.githubusercontent.com/115614317/205922893-cd7425da-8d57-4d79-9b49-b6be433aa3f9.png)  
![Screenshot (74)](https://user-images.githubusercontent.com/115614317/205923156-69ba0a10-d95d-4d6c-aa21-243922c11c1a.png)  
### Hapus Data (H) & Lihat (L)  
![Screenshot (75)](https://user-images.githubusercontent.com/115614317/205923363-e35b1f52-70f1-416c-b61f-2dbaa9d479cd.png)  
![Screenshot (76)](https://user-images.githubusercontent.com/115614317/205923381-3dd99dda-f2a5-4a02-84dd-6a98912fb79a.png)  
