pasien_list = []

def hitung_status(tinggi, berat):
    beratIdeal = tinggi - 100
    if berat > beratIdeal:
        status = "Kelebihan berat badan"
    else:
        status = "Berat badan ideal"
    return beratIdeal, status

while True:
    print("""
=============================================
|           PENDATAAN PASIEN (CRUD)         |
=============================================
""")

    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        # Create
        nama = input("Nama Pasien   : ")
        tinggi = int(input("Tinggi Badan  : "))
        bb = int(input("Berat Badan   : "))
        print("Masukkan penyakit satu per satu. Ketik 'selesai' jika sudah.")
        penyakit_list = []
        while True:
            penyakit = input("Penyakit: ")
            if penyakit.lower() == "selesai":
                break
            penyakit_list.append(penyakit)
        beratIdeal, status = hitung_status(tinggi, bb)
        pasien = {
            "nama": nama,
            "tinggi": tinggi,
            "berat": bb,
            "ideal": beratIdeal,
            "status": status,
            "penyakit": penyakit_list
        }
        pasien_list.append(pasien)
        print(f"\nData pasien '{nama}' berhasil ditambahkan!\n")

    elif pilihan == "2":
        # Read
        print("\n-----------------------------------")
        print("|           DATA PASIEN           |")
        print("-----------------------------------")
        if len(pasien_list) == 0:
            print("Belum ada pasien")
        else:
            nomor = 1
            for p in pasien_list:
                print(f"\n[{nomor}]")
                print("Nama Pasien  :", p["nama"])
                print("Tinggi Badan :", p["tinggi"])
                print("Berat Badan  :", p["berat"])
                print("Berat Ideal  :", p["ideal"])
                print("Status       :", p["status"])
                print("Penyakit     :")
                for py in p["penyakit"]:
                    print(" -", py)
                print("-----------------------------------")
                nomor = nomor + 1

    elif pilihan == "3":
        # Update
        if len(pasien_list) == 0:
            print("Belum ada data untuk diubah")
        else:
            nomor = 1
            for p in pasien_list:
                print(str(nomor) + ". " + p["nama"])
                nomor = nomor + 1
            ubah = int(input("Masukkan nomor pasien yang ingin diubah: ")) - 1
            if ubah >= 0 and ubah < len(pasien_list):
                data = pasien_list[ubah]
                print("\nMasukkan data baru (kosongkan jika tidak ingin diubah):")
                nama_baru = input("Nama baru   : ")
                if nama_baru == "":
                    nama_baru = data["nama"]
                tinggi_baru = input("Tinggi baru : ")
                if tinggi_baru == "":
                    tinggi_baru = data["tinggi"]
                else:
                    tinggi_baru = int(tinggi_baru)
                berat_baru = input("Berat baru  : ")
                if berat_baru == "":
                    berat_baru = data["berat"]
                else:
                    berat_baru = int(berat_baru)
                print("Masukkan penyakit baru satu persatu, ketik 'selesai' jika tidak ingin menambah")
                penyakit_baru = []
                while True:
                    p = input("Penyakit: ")
                    if p.lower() == "selesai":
                        break
                    penyakit_baru.append(p)
                if len(penyakit_baru) == 0:
                    penyakit_baru = data["penyakit"]
                beratIdeal, status = hitung_status(tinggi_baru, berat_baru)
                pasien_list[ubah] = {
                    "nama": nama_baru,
                    "tinggi": tinggi_baru,
                    "berat": berat_baru,
                    "ideal": beratIdeal,
                    "status": status,
                    "penyakit": penyakit_baru
                }
                print("\nData berhasil diperbarui")
            else:
                print("Nomor tidak valid")

    elif pilihan == "4":
# Delete
        if len(pasien_list) == 0:
            print("Tidak ada data pasien")
        else:
            nomor = 1
            for p in pasien_list:
                print(str(nomor) + ". " + p["nama"])
                nomor = nomor + 1
            hapus = int(input("Masukkan nomor pasien yang ingin dihapus: ")) - 1
            if hapus >= 0 and hapus < len(pasien_list):
                nama_hapus = pasien_list[hapus]["nama"]
                del pasien_list[hapus]
                print(f"Data pasien '{nama_hapus}' berhasil dihapus")
            else:
                print("Nomor tidak valid")

    elif pilihan == "5":
        print("Pendataan pasien selesai")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi")
