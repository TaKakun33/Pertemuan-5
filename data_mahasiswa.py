def MHS1(NIM,Nama,Tgl):
    return [NIM,Nama,Tgl]

def MHS3(Kode_Matkul,Nama_Matkul):
    return [Kode_Matkul,Nama_Matkul]

def MHS2(NIM,Kode_Matkul,Nilai):
    return [NIM,Kode_Matkul,Nilai]

def kode_matkul(MHS):
    return MHS[1]

def nilai(MHS):
    return MHS[2]

def hitungRangeNilai(M1,M2):
    nilai_max = ((nilai(M1) + nilai(M2)) + abs(nilai(M1) - nilai(M2)))/2
    nilai_min = ((nilai(M1) + nilai(M2)) - abs(nilai(M1) - nilai(M2)))/2
    range = nilai_max - nilai_min
    return [kode_matkul(M1), nilai_max, nilai_min, range]

print(hitungRangeNilai(MHS2(1234343,123,90), MHS2(1234343,123,60)))