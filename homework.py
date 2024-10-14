print("Layak Kerja Di Jepang")

nama = input("Masukan Nama:")
umur = int(input("Masukan Umur:"))
nama_orang_tua = input("Masukan Nama Orang Tua:")
tanggal_lahir = int(input(" MasukanTanggal Lahir:"))
pendidikan_terakhir = str(input("Masukan Pendidikan Terakhir:"))
pendidikan = ["SMA","SMK","D3"]

if umur>20 and pendidikan_terakhir in pendidikan :
    print("lolos ke jepang")
else:
    print("tidak lolos")

print("selamat berjuang")