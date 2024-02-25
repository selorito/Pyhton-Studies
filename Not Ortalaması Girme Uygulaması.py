Ort=0
Y1=int(input('1.Sınav Notu.:'))
Y2=int(input('2.Sınav Notu.:'))
ort=(Y1+Y2)/2
print('Ortalamanız:',ort)

if ort>65:
 print('Karahanlı seninle gurur duyuyor')
 
elif ort==65:
 print('Karahanlı Sadakatini Tebrik Ediyor')
else:
    print('Karahanlı senin kalemini kırdı')
