print('''
Assalomu alaykum!
 Siz Madaminov Shohjahon tomonidan
 yozilgan, birinchi kichkina dastur
 "Kalkuliator"dan foydalanyabsiz.
 
 Sizni Dasturimizda mavjud bo`lgan Matematik amallar 
 belgilari bilan tanishtirib o`taman.
 
 "+" Qo`shish amali belgisi.
 "-" Ayirish amali belgisi.
 "*" Ko`paytirish amali belgisi.
 "/" Bo`lish amali belgisi.
 "**" Sonning darajasini xisoblab beruvchi amal belgisi.
 "v" Sonning oddiy ildizdan chiqarish amali belgisi.
 "w" Sonning kubini chiqarish amali belgisi.
''')
while True:
    som = float(input('Birinchi sonni kiriting!: '))
    amal = input('Amalni kiriting!: ')
    son1 = float(input('Ikkinch sonni kiriting!: '))
    v = (som ** (1/2))
    w = (pow(som, son1))


    if amal == '+':
        print(f'Javob: ' + str(som + son1))
    elif amal == '-':
         print(f'Javob: ' + str(som - son1))
    elif amal == '*':
       print(f'Javob: ' + str(som * son1))
    elif amal == '/':
        print('Javob: ' + str(som / son1))
    elif amal == '**':
        print(f'Javob: ' + str(som ** son1))
    elif amal == 'v':
        print('Javob: ' + str( v ))
    elif amal == 'w':
        print('Javob: ' + str(w))
    else:
      print('\nSizning misolingizda xatolik bor. '
        '\nIltimos tekshirib qaytadan urinib ko`ring! '
        '\nFoydalanish uchun kodni qayta ishga tushuring! ')

