Sınav1=int(input('1.Sınav Notunuz.:'))
Sınav2=int(input('2.Sınav Notunuz.:'))
Sınav3=int(input('3.Sınav Notunuz.:'))

ortalama=(Sınav1+Sınav2+Sınav3)/3

print(int(ortalama))

#Geçtiniz,Şartlı Geçtiniz,Kaldınız

if ortalama >=50:
 print('Geçtiniz')

elif ortalama >=40:
 print('Şartlı Geçtiniz')

else:
 print('Kaldınız')


