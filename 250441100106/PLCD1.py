nama = "crysoli tiara simanjuntak"
NIM = 250441100106

print ("nama saya adalah " + nama + " NIM saya adalah " + str (NIM))
tugas = float(input("masukkan nilai tugas : "))
uts = float(input("masukkan nilai uts : "))
uas = float(input("masukkan nilai uas : "))

nilai_tugas = 0.30
nilai_uts = 0.30
nilai_uas = 0.40

nilai_akhir = (tugas * nilai_tugas) + (uts * nilai_uts) + (uas * nilai_uas)

print(" nilai akhirnya adalah", nilai_akhir)