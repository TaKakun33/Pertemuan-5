# Nama File   = Garis.py
# Deskripsi   = Membuat tipe bentukan garis berseta konstruktor dan selekror sama menentukan panjang garis dan apakah garis ssejajar 
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
# ordinat: point --> real
#   {ordinat(P) memberikan ordinat dari point P}
# Realisasi
def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

# =================================================================================================================================================================
# Definisi type
# type Garis: <P1:point, P2:point>
#   {<P1,P2> adalah sebuah garis dengan P1 adalah Point1 dan P2 adalah Point2}

# Definisi Dan Spesifikasi Konstruktor
# Make-Garis: 2point --> Garis
#   {Make_Garis(P1,P2) membentuk Garis dari P1 dan P2 dengan P1 sebagai point-1 dan P2 sebagai point-2}
# Realisasi
def Make_Garis(P1,P2):
    return [P1,P2]

# Definisi Dan Spesifikasi Selector
# Point1: Garis --> Point
#   {Point1(G) memberikan Point-1 dari Garis G}
# 
# Point2: Garis --> Point
#   {Point2(G) memberikan Point-2 dari Garis G}
# Realisasi
def Point1(G):
    return G[0]

def Point2(G):
    return G[1]

# Definisi dan Spesifikasi Operator/Fungsi Lain terhadap garis
# Issejajar: Garis --> real
#   {panjang_garis(G) menghitung panjang garis dari point-1 ke point-2}
# Realisasi
def panjang_garis(G):
    panjang_x = absis(Point2(G)) - absis(Point1(G))
    panjang_y = ordinat(Point2(G)) - ordinat(Point1(G))
    return ((panjang_x ** 2) + (panjang_y ** 2))**0.5

# Definisi dan Spesifikasi Predikat
# Issejajar: Garis --> Boolean
#   {IsSejajar(G1,G2) benar jika G1 sama dengan G2}
# Realisasi
def IsSejajar(G1,G2):
    m1 = (ordinat(Point2(G1)) - ordinat(Point1(G1))) / (absis(Point2(G1)) - absis(Point1(G1)))
    m2 = (ordinat(Point2(G2)) - ordinat(Point1(G2))) / (absis(Point2(G2)) - absis(Point1(G2)))
    return m1 == m2


# Aplikasi 
print(IsSejajar(Make_Garis(Make_point(0,0), Make_point(2,3)), Make_Garis(Make_point(-2,5), Make_point(0,-2))))
print(IsSejajar(Make_Garis(Make_point(0,0), Make_point(2,3)), Make_Garis(Make_point(0,0), Make_point(-2,-3))))

print(panjang_garis(Make_Garis(Make_point(2,2), Make_point(5,2))))
