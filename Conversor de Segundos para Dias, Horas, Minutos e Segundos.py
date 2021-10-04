segundos = int(input("Digite o número de segundos á ser convertido: "))
segundosDia = 86400
segundosHora = 3600
segundosMinuto = 60

dias = segundos // segundosDia
segundos %= segundosDia

horas = segundos // segundosHora
segundos %= segundosHora

minutos = segundos // segundosMinuto
segundos %= segundosMinuto

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")