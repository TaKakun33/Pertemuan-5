# Nama File   = Garis.py
# Deskripsi   = Membuat tipe bentukan garis berseta konstruktor dan selekror sama menentukan panjang garis dan apakah garissejajar 
# Nama        = akmal kafli anan
# Tanggal     = 28 September 2024

# Definisi type
# type Point: <x:integer, y:integer>
#   {<x,y> adalah sebuah point dengan x adalah absis dan y adalah oordinat}

# Definisi Dan Spesifikasi Konstruktor
# Make-point: 2real --> point
#   {Make_point(X,Y) membentuk point dari x dan y dengan x sebagai absis dan y sebagai oordinat}
# Realisasi
def Make_point(X,Y):
    return [X,Y]

# Definisi Dan Spesifikasi Selector
# absis: point --> integer
#   {absis(P) memberikan absis dari point P}
# Realisasi
def absis(P):
    return P[0]

# oordinat: point --> integer
#   {oordinat(P) memberikan oordinat dari point P}
# Realisasi
def oordinat(P):
    return P[1]


# Definisi type
# type Garis: <P1:point, P2:point>
#   {<P1,P2> adalah sebuah garis dengan P1 adalah Point1 dan P2 adalah Point2}

# Definisi Dan Spesifikasi Konstruktor
# Make-Garis: 2point --> Garis
#   {Make_Garis(X,Y) membentuk Garis dari P1 dan P2 dengan P1 sebagai point-1 dan P2 sebagai point-2}
# Realisasi
def Make_Garis(P1,P2):
    return [P1,P2]

# Definisi Dan Spesifikasi Selector
# absis: Garis --> Point
#   {Point1(G) memberikan Point-1 dari Garis G}
# Realisasi
def Point1(G):
    return G[0]

# absis: Garis --> Point
#   {Point2(G) memberikan Point-2 dari Garis G}
# Realisasi
def Point2(G):
    return G[1]

# Definisi dan Spesifikasi Operator/Fungsi Lain terhadap garis
# Issejajar: Garis --> real
#   {panjang_garis(G) menghitung panjang garis dari point-1 ke point-2}
# Realisasi
def panjang_garis(G):
    panjang_x = absis(Point2(G)) - absis(Point1(G))
    panjang_y = oordinat(Point2(G)) - oordinat(Point1(G))
    return ((panjang_x ** 2) + (panjang_y ** 2))**0.5


# Definisi type
# type Segiempat: <G1:Garis, G2:Garis, G3:Garis, G4:Garis>
#   {<G1,G2,G3,G4> adalah sebuah Segiempat dengan 4 garis}

# Definisi Dan Spesifikasi Konstruktor
# Make-Segiempat: 4Garis --> Segiempat
#   {Make_Segiempat(G1,G2,G3,G4) membentuk Segiempat dari 4 buah garis yaitu G1, G2, G3, G4}
# Realisasi
def Make_Segiempat(G1,G2,G3,G4):
    return [G1,G2,G3,G4]

# Definisi Dan Spesifikasi Selector
# GARIS1: Segiempat --> Garis
#   {Garis1(G) memberikan Garis-1 dari Segiempat G}
# Realisasi
def Garis1(G):
    return G[0]

# Garis2: Segiempat --> Garis
#   {Garis2(G) memberikan Garis-2 dari Segiempat G}
# Realisasi
def Garis2(G):
    return G[1]

# GARIS3: Segiempat --> Garis
#   {Garis3(G) memberikan Garis-1 dari Segiempat G}
# Realisasi
def Garis3(G):
    return G[2]

# Garis4: Segiempat --> Garis
#   {Garis4(G) memberikan Garis-2 dari Segiempat G}
# Realisasi
def Garis4(G):
    return G[3]

# Definisi dan Spesifikasi Predikat
# isBujurSangkar: Segiempat --> Boolean
#   {panjang_garis(G) menghitung panjang garis dari point-1 ke point-2}
# Realisasi
def isBujueSangkar(S):
    P_Garis_1 = panjang_garis(Garis1(S))
    P_Garis_2 = panjang_garis(Garis2(S))
    P_Garis_3 = panjang_garis(Garis3(S))
    P_Garis_4 = panjang_garis(Garis4(S))
    return P_Garis_1 == P_Garis_2 == P_Garis_3 == P_Garis_4

def isJarjargenjang(S):
    P_Garis_1 = panjang_garis(Garis1(S))
    P_Garis_2 = panjang_garis(Garis2(S))
    P_Garis_3 = panjang_garis(Garis3(S))
    P_Garis_4 = panjang_garis(Garis4(S))
    return P_Garis_1 == P_Garis_2 or P_Garis_1 == P_Garis_3 or P_Garis_1 == P_Garis_3 or P_Garis_2 == P_Garis_3 or P_Garis_2 == P_Garis_4 or  P_Garis_3 == P_Garis_4

# Aplikasi 
print(isBujueSangkar(Make_Segiempat(Make_Garis(Make_point(2,2), Make_point(5,2)),Make_Garis(Make_point(2,2), Make_point(5,2)), Make_Garis(Make_point(2,2), Make_point(5,2)), Make_Garis(Make_point(2,2), Make_point(5,2)))))
print(isJarjargenjang(Make_Segiempat(Make_Garis(Make_point(2,2), Make_point(5,2)),Make_Garis(Make_point(2,2), Make_point(5,2)), Make_Garis(Make_point(2,2), Make_point(5,2)), Make_Garis(Make_point(2,2), Make_point(5,2)))))