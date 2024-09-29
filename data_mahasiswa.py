# Nama File   = Tanggal.py
# Deskripsi   = Membuat tipe bentukan Tanggal berseta konstruktor dan selekror 
# Nama        = akmal kafli anan
# Tanggal     = 28 September 2024

# Definisi type
# type Date: <d:integer[1..31], m:integer[1..12], y:integer > 0>
#   {<d,m,y> adalah tanggal d bulan m tahun y}
# 
# type MHS1: <NIM:string, Nama:string, Tanggal_lahir: Date >
#   {<NIM,Nama,Tgl> adalah sebuah data mahsiswa yang tediri dari NIM, Nama dan Tanggal_lahir}
# 
# type MHS2: <NIM:string, Kode_Matkul:string, Nilai:real>
#   {<NIM,Kode_Matkul,Nilai> adalah sebuah data mahsiswa yang tediri dari NIM, Kode_Matkul dan Nilai}
# 
# type MHS3: <Kode_Matkul:string, Nama_Matkul:string>
#   {<Kode_Matkul,Nilai> adalah sebuah data mahsiswa yang tediri dari Kode_Matkul dan Nama_Matkul}

# Definisi Dan Spesifikasi Konstruktor
# make_MHS2: string, string, real --> MHS2
#   {make_MHS2(NIM,Kode_Matkul,Nilai) membentuk MHS2 yang mana NIM meupakan string yang dimiliki setiap mahsiswa, Kode_matkul merupakan string yang dimiliki setiap matkul dan nilai merupakan nilai masasiswa dengan tpe real}
# Realisasi
def make_MHS2(NIM,Kode_Matkul,Nilai):
    return [NIM,Kode_Matkul,Nilai]

# Definisi Dan Spesifikasi Selector
# NIM: MHS2 --> string
#   {NIM(MHS) memberikan NIM dari MHS2}
# 
# kode_matkul: MHS2 --> string
#   {kode_matkul(MHS) memberikan kode_matkul dari MHS2}
# 
# kode_matkul: MHS2 --> real
#   {kode_matkul(MHS) memberikan nilai dari MHS2}

# Realisasi
def NIM(MHS):
    return MHS[0]

def kode_matkul(MHS):
    return MHS[1]

def Nilai(MHS):
    return MHS[2]

def hitungRangeNilai(M1,M2):
    nilai_max = ((Nilai(M1) + Nilai(M2)) + abs(Nilai(M1) - Nilai(M2)))/2
    nilai_min = ((Nilai(M1) + Nilai(M2)) - abs(Nilai(M1) - Nilai(M2)))/2
    range = nilai_max - nilai_min
    return [kode_matkul(M1), nilai_max, nilai_min, range]

print(hitungRangeNilai(make_MHS2(1234343,123,90), make_MHS2(1234343,123,60)))