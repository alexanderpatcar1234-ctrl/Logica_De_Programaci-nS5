anio = int(input("Introduce un año: "))

if anio < 1582:
	print("No esta dentro del período del calendario Gregoriano")
elif anio % 4 != 0 :
    print(anio," es ","Año comun")
elif 0 != anio /100:
    print(anio," es ","Año biciesto")
elif 0 != anio /400:
    print(anio," es ","Año Comun")
else:
    print(anio," es ","Año Bisiesto")