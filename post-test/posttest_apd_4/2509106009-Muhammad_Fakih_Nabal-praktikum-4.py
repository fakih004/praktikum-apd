username = "fakih"
password = "009"


produk = {
    1: ("roti tawar", 12000),
    2: ("sarimi isi 2", 5500),
    3: ("lemineral besar", 7000)
}

while True:  
    print("---------------------------------------")
    print("|   selamat datang di toko suka maju  |")
    print("---------------------------------------")

    status = input("apakah anda member? (iya/bukan): ")
    is_member = False

    if status == 'iya':
        kesempatan = 3
        while kesempatan > 0:
            print("---[ menu Login Member ]---")
            user = input("username: ")
            pw = input("password: ")

            if user == username and pw == password:
                print("login berhasil anda adalah member")
                is_member = True
                break
            else:
                kesempatan -= 1
                print(f"login gagal, sisa percobaan: {kesempatan}")

        if not is_member:
            print("anda gagal login 3 kali. Anda dianggap non-member")

    elif status != 'bukan':
        print("anda bukan member")

    keranjang = []
    total_belanja = 0

    while True:
        print("-----------------")
        print("| barang Jualan |")
        print("-----------------")
        for nomor, (nama, harga) in produk.items():
            print(f"{nomor}. {nama} - Rp{harga:,}")
        print("0. Checkout")

        pilih = input("pilih nomor barang (0 untuk checkout): ")

        if pilih == "0":
            break  
        elif pilih.isdigit() and int(pilih) in produk:
            nomor = int(pilih)
            nama, harga = produk[nomor]
            keranjang.append((nama, harga))
            total_belanja += harga
            print(f"{nama} berhasil ditambahkan ke keranjang!")
            print(f"total sementara: Rp{total_belanja:,}")
        else:
            print("Pilihan tidak valid!")

    print("-----------------")
    print("|   Struk Belanja   |")
    print("-----------------")

    if len(keranjang) == 0:
        print("anda tidak membeli barang")
    else:
        for item, harga in keranjang:
            print(f"- {item} : Rp{harga:,}")

        print(f"Total sebelum diskon : Rp{total_belanja:,}")

        if is_member:
            diskon = int(total_belanja * 0.15)
            total_setelah_diskon = total_belanja - diskon
            print(f"diskon (15%)         : Rp{diskon:,}")
            print(f"total setelah diskon : Rp{total_setelah_diskon:,}")
        else:
            print("Diskon               : Rp0")
            print(f"Total bayar          : Rp{total_belanja:,}")

    ulang = input("apakah ingin melakukan transaksi baru? (iya/tidak): ")
    if ulang != "iya":
        break
