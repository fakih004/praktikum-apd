nama = input('Nama Pasien          : ')
tinggi = input('Tinggi Badan         : ' )
bb = input('Berat Badan          : ' )
beratIdeal = (int(tinggi) - 100)
isKelebihan = int(bb) > beratIdeal
statusList = ("berat badan ideal","kelebihan berat badan")
status = (statusList[int(isKelebihan)])


print("""----------------------------------------------------
|              HASIL CEK BERAT BADAN               |
----------------------------------------------------""")
print(f"Nama Pasien          : {nama:<29}")
print(f"Tinggi Badan         : {tinggi:<30}")
print(f"Berat Badan          : {bb:<29}")
print('Berat Ideal          : '+ str(beratIdeal))
print(f"Status               : {status:<36}")
           