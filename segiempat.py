# Nama File   = Segiempat.py
# Deskripsi   = Membuat tipe bentukan segiempat berseta konstruktor dan selekror  
# Nama        = akmal kafli anan
# Tanggal     = 28 September 2024

# =================================================================================================================================================================
# Definisi type
# type Point: <x:real, y:real>
#   {<x,y> adalah sebuah point dengan x adalah absis dan y adalah ordinat}

# Definisi Dan Spesifikasi Konstruktor
# Make-point: 2real --> point
#   {Make_point(X,Y) membentuk point dari x dan y dengan x sebagai absis dan y sebagai ordinat}
# Realisasi
def Make_point(X,Y):
    return [X,Y]

# Definisi Dan Spesifikasi Selector
# absis: point --> real
#   {absis(P) memberikan absis dari point P}
# 
# ordinat: point --> real
#   {ordinat(P) memberikan ordinat dari point P}
# Realisasi
def absis(P):
    return P[0]

def ordinat(P):
    return P[1]


# =================================================================================================================================================================
# Definisi type
# type Segiempat: <P1:Point, P2:Point, P3:Point, P4:Point>
#   {<P1,P2,P3,P4> adalah sebuah Segiempat dengan 4 Point}

# Definisi Dan Spesifikasi Konstruktor
# Make-Segiempat: 4Point --> Segiempat
#   {Make_Segiempat(P1,P2,P3,P4) membentuk Segiempat dari 4 buah point}
# Realisasi
def Make_Segiempat(P1,P2,P3,P4):
    return [P1,P2,P3,P4]

# Definisi Dan Spesifikasi Selector
# Point1: Segiempat --> Point
#   {Point1(S) memberikan Point-1 dari Segiempat S}
# 
# Point2: Segiempat --> Point
#   {Point2(S) memberikan Point-2 dari Segiempat S}
# 
# Point3: Segiempat --> Point
#   {Point3(S) memberikan Point-3 dari Segiempat S}
# 
# Point4: Segiempat --> Point
#   {Point4(S) memberikan Point-4 dari Segiempat S}
# Realisasi
def Point1(S):
    return S[0]

def Point2(S):
    return S[1]

def Point3(S):
    return S[2]

def Point4(S):
    return S[3]

# Definisi dan Spesifikasi operator terhadap Point
# Jarak: 2point --> real
#   {Jarak(P1,P2) menghitung jarak dari kedua point}
# 
# Gradien: 2point --> real
#   {Gradien(P1,P2) menghitung Gradien dari kedua point}

# Realisasi
def Jarak(P1,P2):
    return (((absis(P1) - absis(P2))** 2) + ((ordinat(P1) - ordinat(P2))** 2))**0.5

def Gradien(P1,P2):
    return (ordinat(P2) - ordinat(P1)) / (absis(P2) - absis(P1))

# Definisi dan Spesifikasi operator terhadap segiempat
# AreaBujurSangkar: segiempat --> real
#   {AreaBujurSangkar(S) menghitung luas area dari bujur sangkar}

# Realisasi
def AreaBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) * Jarak(Point3(S), Point4(S))

# Definisi dan Spesifikasi Predikat
# isBujurSangkar: Segiempat --> Boolean
#   {isBujurSangkar(S) meencari tau apakah segiempat tersebut merupakan Bujur sangkar}
# 
# isJarjargenjang: Segiempat --> Boolean
#   {isJarjargenjang(S) meencari tau apakah segiempat tersebut merupakan jajar genjang}

# Realisasi

def isBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) * Jarak(Point3(S), Point4(S)) == Jarak(Point1(S), Point3(S)) * Jarak(Point2(S), Point4(S))

def isJarjargenjang(S):
    P1 = Point1(S)
    P2 = Point2(S)
    P3 = Point3(S)
    P4 = Point4(S)
    return Gradien(P1, P2) == Gradien(P3, P4) and Gradien(P1, P4) == Gradien(P2, P3) and Jarak(P1, P2) == Jarak(P3, P4) and Jarak(P1, P4) == Jarak(P2, P3)


# Aplikasi 
print(AreaBujurSangkar(Make_Segiempat( Make_point(1, 3), Make_point(2, 3), Make_point(1, 2), Make_point(2, 2))))

print(isBujurSangkar(Make_Segiempat(Make_point(1, 3), Make_point(2, 3), Make_point(1, 2), Make_point(2, 2))))
print(isJarjargenjang(Make_Segiempat(Make_point(1, 1), Make_point(4, 1), Make_point(6, 4), Make_point(3, 4))))