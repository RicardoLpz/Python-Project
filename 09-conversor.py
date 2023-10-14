temperatura = input("Ingrese temperatura a convertir:")
escala = input("Es Farenheit(F) o Celcius (C)?:")
valorTemp = float(temperatura)
if escala == "C":
    conversion = (valorTemp * 9 / 5) + 32
elif escala == "F":
    conversion = (valorTemp - 32) * 5 / 9
else:
    print("escala incorrecta, intenta de nuevo")

print("resultado de operacion:", conversion)
