import json
from data import input_user, simpan_user

def register():
    users = input_user()
    print("\n=== REGISTRASI AKUN BARU ===")
    username = input("Masukkan username: ")

    if username in users:
        print("Username sudah ada")
        return

    password = input("Masukkan password: ")
    users[username] = password
    simpan_user(users)
    print("Akun berhasil dibuat")


def login():
    users = input_user()
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login berhasil")
        return True
    else:
        print("Username atau password salah")
        return False


def menu_awal():
    while True:
        print("=== MENU UTAMA ===")
        print("1. Login (Dokter)")
        print("2. Register")
        print("3. Masuk tanpa login (Perawat)")
        print("4. Keluar")

        pilih = input("Pilih menu: ")
        if pilih == "1":
            if login():
                return "dokter"
        elif pilih == "2":
            register()
        elif pilih == "3":
            print("Masuk sebagai perawat")
            return "perawat"
        elif pilih == "4":
            print("Keluar dari program")
            exit()
        else:
            print("Pilihan tidak valid")
