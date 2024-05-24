horarios_disponibles=[ " 5:00 - 6:00 PM", " 7:00 - 8:00 PM", " 8:00 - 9:00 PM"," 11:00 - 12:00 PM"]
reservacion:list=[]
while True:
    print("Bienvenido al menu de grass sintetico")
    print("1. Horarios disponibles")
    print("2. Reservacion de grass")
    print("3. pago por la reserva del grass")
    print("4. Verificar el alquiler")
    print("5. salir")
    opcion=int(input("ingrese una opcion del menu grass sintetico: "))
    if opcion == 1:
        for i, horarios_disponibles in enumerate(horarios_disponibles,1):
            print(f"{i}. {horarios_disponibles}")
    elif opcion == 2:
        indice=int(input("ingrese el indice del horario que desea reservar: "))
        if indice<1 or indice > len(horarios_disponibles):
            print("El horario no es valido")
        else:
            horario=horarios_disponibles.pop(indice -1)
            reservacion.append(horario)
            print(f"el horario {horario} se ha reservado con exito")
    elif opcion == 3:
        if not reservacion:
            print("no tiene reservas actuales")
        else:
            indice=int(input("ingrese el indice del horario que va a pagar: "))
            costo_alquiler=30
            pago_alquiler=horarios_disponibles.append(int(input("El pago es de/30 por el alquiler...  ingresa el monto: ")))
            if pago_alquiler==costo_alquiler:
                print("su pago ha sido correcto")
            else:
                print("el pago no es el correcto")
    elif opcion == 4:
        for i,in enumerate(reservacion):
            print(f"la reservacion {reservacion} ha sido cancelado con {pago_alquiler} correctamente")
    elif opcion == 5:
        break
    else:
        print("codigo invalido. Intenta de nuevo")
        
        
