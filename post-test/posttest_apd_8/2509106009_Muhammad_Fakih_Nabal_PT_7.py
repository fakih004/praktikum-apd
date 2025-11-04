from fungsi import menu_dokter, menu_perawat, keluar_program
from user import menu_awal
from data import input_pasien
from pasien import create, read, update, delete

# input data pasien 
pasien_dict = input_pasien()

# login (dokter / perawat)
mode = menu_awal()

if mode == "dokter":
    while True:
        menu_dokter()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            create(pasien_dict)
        elif pilihan == "2":
            read(pasien_dict)
        elif pilihan == "3":
            update(pasien_dict)
        elif pilihan == "4":
            delete(pasien_dict)
        elif pilihan == "5":
            keluar_program()
            break
        else:
            print("Pilihan tidak valid")

elif mode == "perawat":
    while True:
        menu_perawat()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read(pasien_dict)
        elif pilihan == "2":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid.")
