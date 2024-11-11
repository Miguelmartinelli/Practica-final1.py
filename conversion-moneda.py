# Paso 1: Definir el valor actuar del euro y dolar con respecto al peso mexicano

tipo_cambio_eur_a_mxn = 23.70 #en un caso mas real se buscaria en una base de datos
tipo_cambio_usd_a_mxn = 20.75


#Paso 2: Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversio (EUR/USD): ")

#Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir:  "))


#Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente


# Paso 5 : Mostrar el resultado de la conversion al usuario

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else:
    print("No está disponible este tipo de conversion actualmente")