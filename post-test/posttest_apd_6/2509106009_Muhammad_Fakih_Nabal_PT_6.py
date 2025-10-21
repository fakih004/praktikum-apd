pasien_dict = {}
def hitung_status(tinggi, berat):
    beratIdeal = tinggi - 100
    if berat > beratIdeal:
        status = "Kelebihan berat badan"
    else:
        status = "Berat badan ideal"
    return beratIdeal, status

def login_dokter():
    username_dokter = "fakih"
    password_dokter = "009"
    print("=== SILAHKAN LOGIN  ===")
    username = input("Username: ")
    password = input("Password: ")
    if username == username_dokter and password == password_dokter:
        print("login berhasil")
        return True
    else:
        print("login gagal")
        return False

is_dokter = login_dokter()

while True:
    print("\n=============================================")
    print("|           PENDATAAN PASIEN (CRUD)         |")
    print("=============================================")

    if is_dokter:
        print("| 1. Tambah Data Pasien                     |")
        print("| 2. Lihat Data Pasien                      |")
        print("| 3. Ubah Data Pasien                       |")
        print("| 4. Hapus Data Pasien                      |")
        print("| 5. Keluar Program                         |")
    else:
        print("| 1. Tambah Data Pasien                     |")
        print("| 2. Lihat Data Pasien                      |")
        print("| 3. Hapus Data Pasien                      |")
        print("| 4. Keluar Program                         |")
    print("=============================================")

    pilihan = input("pilih menu: ")


    if pilihan == "1":
        nama = input("nama Pasien   : ")
        tinggi = int(input("tinggi Badan  : "))
        bb = int(input("berat Badan   : "))
        print("masukkan penyakit satu per satu ketik 'selesai' jika sudah")
        penyakit_list = []
        while True:
            penyakit = input("Penyakit: ")
            if penyakit.lower() == "selesai":
                break
            penyakit_list.append(penyakit)

        beratIdeal, status = hitung_status(tinggi, bb)
        pasien_dict[nama] = {
            "tinggi": tinggi,
            "berat": bb,
            "ideal": beratIdeal,
            "status": status,
            "penyakit": penyakit_list
        }

        print(f"data pasien '{nama}' berhasil ditambahkan")

    elif pilihan == "2":
        print("\n-----------------------------------")
        print("|           DATA PASIEN           |")
        print("-----------------------------------")

        if not pasien_dict:
            print("belum ada pasien")
        else:
            nomor = 1
            for nama in pasien_dict:
                data = pasien_dict[nama]
                print(f"\n[{nomor}] {nama}")
                print("Tinggi Badan :", data["tinggi"])
                print("Berat Badan  :", data["berat"])
                print("Berat Ideal  :", data["ideal"])
                print("Status       :", data["status"])
                print("Penyakit     :")
                for py in data["penyakit"]:
                    print(" -", py)
                print("-----------------------------------")
                nomor = nomor + 1

    elif pilihan == "3" and is_dokter:
        if not pasien_dict:
            print("belum ada data untuk diubah")
        else:
            print("DAFTAR PASIEN:")
            nama_list = list(pasien_dict.keys())
            nomor = 1
            for nama in nama_list:
                print(str(nomor) + ". " + nama)
                nomor = nomor + 1
            ubah = int(input("masukkan nomor pasien yang ingin diubah: ")) - 1
            if 0 <= ubah < len(nama_list):
                nama_pilih = nama_list[ubah]
                data = pasien_dict[nama_pilih]
                print("masukkan data baru (kosongkan jika tidak ingin diubah):")
                nama_baru = input("Nama baru   : ")
                if nama_baru == "":
                    nama_baru = nama_pilih
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
                print("Masukkan penyakit baru satu per satu (ketik 'selesai' jika tidak ingin menambah):")
                penyakit_baru = []
                while True:
                    p = input("Penyakit: ")
                    if p.lower() == "selesai":
                        break
                    penyakit_baru.append(p)
                if not penyakit_baru:
                    penyakit_baru = data["penyakit"]
                beratIdeal, status = hitung_status(tinggi_baru, berat_baru)
                del pasien_dict[nama_pilih] 
                pasien_dict[nama_baru] = {
                    "tinggi": tinggi_baru,
                    "berat": berat_baru,
                    "ideal": beratIdeal,
                    "status": status,
                    "penyakit": penyakit_baru
                }
                print("data pasien berhasil diperbarui")
            else:
                print("nomor tidak valid")

    elif (pilihan == "4" and is_dokter) or (pilihan == "3" and not is_dokter):
        if not pasien_dict:
            print("tidak ada data pasien")
        else:
            print("DAFTAR PASIEN:")
            nama_list = list(pasien_dict.keys())
            nomor = 1
            for nama in nama_list:
                print(str(nomor) + ". " + nama)
                nomor = nomor + 1
            hapus = int(input("masukkan nomor pasien yang ingin dihapus: ")) - 1
            if 0 <= hapus < len(nama_list):
                nama_hapus = nama_list[hapus]
                del pasien_dict[nama_hapus]
                print(f"data pasien '{nama_hapus}' berhasil dihapus")
            else:
                print("nomor tidak valid.")
    elif (pilihan == "5" and is_dokter) or (pilihan == "4" and not is_dokter):
        print("pendataan pasien selesai")
        break
    else:
        print("pilihan tidak valid Silakan coba lagi")
