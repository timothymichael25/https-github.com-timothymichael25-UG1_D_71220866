print ("---------Nilai Ke 1-------")
a = int(input("Nilai Harian: "))
b = int(input("Nilai UTS: "))
c = int(input("Nilai UAS: "))

print ("-------Nilai Ke 2---------")
a1 = int(input("Nilai Harian: "))
b2 = int(input("Nilai UTS: "))
c3 = int(input("Nilai UAS: "))

#Menghitung Nilai Akhir sesuai dengan Bobot
nilai =  (30/100 * tugas) + (30/100 * uts) +  (40/100 * uas)
 
#Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 60:
    grade = 'B'
elif nilai > 40:
    grade = 'C'
elif nilai > 20:
    grade = 'D'
else:
    grade = 'E'