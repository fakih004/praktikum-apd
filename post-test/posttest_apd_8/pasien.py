import json
from fungsi import hitung_status
from data import simpan_pasien

def create(pasien_dict):
    try:
        nama = input("Nama Pasien   : ")
        tinggi = int(input("Tinggi Badan  : "))
        bb = int(input("Berat Badan   : "))
    except ValueError:
        print("Tinggi dan berat badan harus berupa angka")
        return

    print("Masukkan penyakit satu per satu (ketik 'selesai' jika sudah):")
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

    simpan_pasien(pasien_dict)
    print(f"Data pasien '{nama}' berhasil ditambahkan")


def read(pasien_dict):
    print("=== DATA PASIEN ===")
    if not pasien_dict:
        print("Belum ada pasien.")
    else:
        nomor = 1
        for nama in pasien_dict:
            data = pasien_dict[nama]
            print(f"\n[{nomor}] Nama: {nama}")
            print("Tinggi :", data["tinggi"])
            print("Berat  :", data["berat"])
            print("Ideal  :", data["ideal"])
            print("Status :", data["status"])
            print("Penyakit:")
            for p in data["penyakit"]:
                print(" -", p)
            nomor += 1
    print("-----------------------------------")


def update(pasien_dict):
    if not pasien_dict:
        print("Belum ada data pasien.")
        return

    print("=== DAFTAR PASIEN ===")
    nama_list = list(pasien_dict.keys())
    nomor = 1
    for nama in nama_list:
        print(f"{nomor}. {nama}")
        nomor += 1

    try:
        pilih_nomor = int(input("Pilih nomor pasien yang ingin diubah: ")) - 1
        if pilih_nomor < 0 or pilih_nomor >= len(nama_list):
            print("Nomor tidak valid.")
            return

        nama = nama_list[pilih_nomor]
        data = pasien_dict[nama]

        print(f"Mengubah data pasien: {nama}")
        nama_baru = input("Nama baru   : ") or nama
        tinggi_baru = input("Tinggi baru : ")
        berat_baru = input("Berat baru  : ")

        if tinggi_baru:
            tinggi_baru = int(tinggi_baru)
        else:
            tinggi_baru = data["tinggi"]

        if berat_baru:
            berat_baru = int(berat_baru)
        else:
            berat_baru = data["berat"]

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
        del pasien_dict[nama]
        pasien_dict[nama_baru] = {
            "tinggi": tinggi_baru,
            "berat": berat_baru,
            "ideal": beratIdeal,
            "status": status,
            "penyakit": penyakit_baru
        }

        simpan_pasien(pasien_dict)
        print("Data pasien berhasil diperbarui")

    except ValueError:
        print("Input tidak valid, masukkan angka")


def delete(pasien_dict):
    if not pasien_dict:
        print("Belum ada data pasien.")
        return

    print("=== DAFTAR PASIEN ===")
    nama_list = list(pasien_dict.keys())
    nomor = 1
    for nama in nama_list:
        print(f"{nomor}. {nama}")
        nomor += 1

    try:
        pilih_nomor = int(input("Pilih nomor pasien yang ingin dihapus: ")) - 1
        if pilih_nomor < 0 or pilih_nomor >= len(nama_list):
            print("Nomor tidak valid")
            return

        nama = nama_list[pilih_nomor]
        del pasien_dict[nama]
        delete(pasien_dict)
        print(f"Data pasien '{nama}' berhasil dihapus")

        
    except ValueError:
        print("Input tidak valid, masukkan angka")
