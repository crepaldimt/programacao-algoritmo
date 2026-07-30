dias = float(input('Digite os dias: '))
hr = float(input('Digite as horas: '))
mi = float(input('Digite os minutos: '))
sg = float(input('Digite os segundos: '))

mseg = mi*60
hseg = hr*3600
dseg = dias*86400

print(f'O total é {dseg+hseg+mseg+sg}.')
