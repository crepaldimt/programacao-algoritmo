ladoa = float(input('Indique o tamanho do lado A: '))
ladob = float(input('Indique o tamanho do lado B: '))
ladoc = float(input('Indique o tamanho do lado C: '))

tria = ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa

if tria:
    print('É triângulo!')


    if ladoa==ladob==ladoc:
        print('É equilátero!')
    elif ladoa==ladob or ladob==ladoc or ladoa==ladoc:
        print ('É isósceles!')
    else:
        print ('É escaleno!')
else:
 print('Não é triângulo :(')


