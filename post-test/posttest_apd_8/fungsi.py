def hitung_status(tinggi, berat):
    beratIdeal = tinggi - 100
    if berat > beratIdeal:
        status = "Kelebihan berat badan"
    else:
        status = "Berat badan ideal"
    return beratIdeal, status


def keluar_program():
    print("Pendataan pasien selesai.")


def menu_dokter():
    print("\n=============================================")
    print("|           PENDATAAN PASIEN (CRUD)         |")
    print("=============================================")
    print("| 1. Tambah Data Pasien                     |")
    print("| 2. Lihat Data Pasien                      |")
    print("| 3. Ubah Data Pasien                       |")
    print("| 4. Hapus Data Pasien                      |")
    print("| 5. Keluar Program                         |")
    print("=============================================")


def menu_perawat():
    print("\n=============================================")
    print("|        LIHAT DATA PASIEN (perawat)        |")
    print("=============================================")
    print("| 1. Lihat Data Pasien                      |")
    print("| 2. Keluar Program                         |")
    print("=============================================")
