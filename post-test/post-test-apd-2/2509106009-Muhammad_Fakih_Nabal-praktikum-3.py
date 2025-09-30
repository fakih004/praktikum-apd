username = "fakih"
password = "009"

print("---------------------------------------")
print("|   Selamat datang di toko suka maju  |")
print("---------------------------------------")


status = input("apakah anda member? (iya/bukan): ")

is_member = False
if status == "iya":
    print("---[ Menu Login Member ]---")
    user = input("username: ")
    pw = input("password: ")

    if user == username and pw == password:
        print("login berhasil")
        is_member = True
    else:
        print("login gagal, anda bukan member")
        

print("-----------------")
print("| barang jualan |")
print("-----------------")
print("1. roti tawar - Rp12,000")
print("2. sarimi isi 2 - Rp5,500")
print("3. lemineral besar - Rp7,000")

pilih = int(input("Pilih nomor barang: "))


total_belanja = 0

if pilih == 1:
    total_belanja = 12000
    print("Anda membeli: roti tawar - Rp12,000")
elif pilih == 2:
    total_belanja = 5500
    print("Anda membeli: sarimi isi 2 - Rp5,500")
elif pilih == 3:
    total_belanja = 7000
    print("Anda membeli: lemineral besar - Rp7,000")
else:
    print("Pilihan tidak valid!")


print("-----------------")
print("| struk belanja |")
print("-----------------")
print(f"Total sebelum diskon : Rp{total_belanja:,}")

if is_member:
    diskon = int(total_belanja * 0.15)
    total_setelah_diskon = total_belanja - diskon
    print(f"Diskon (15%)         : Rp{diskon:,}")
    print(f"Total setelah diskon : Rp{total_setelah_diskon:,}")
else:
    print("Diskon               : Rp0")
    print(f"Total bayar          : Rp{total_belanja:,}")
