grass_reservado=[]
while True:
    print("Bienvenido al menu de grass sintetico")
    print("1. Horarios disponibles")
    print("2. Reservacion de grass")
    print("3. Pago por alquiler")
    print("4. Verificar el alquiler")
    opcion=int(input("ingrese una opcion del menu: "))
    if opcion == 1:
        grass_reservado.append(input('''Estos son los horarios disponible
        1. Lunes
         7:00 - 8:00
         9:00 - 10:00
        2. Martes
         4:00 - 5:00
         7:00 - 8:00
        3. viernes
         5:00 - 6:00
         8:00 - 9:00
              '''))
    elif opcion == 2:
        reservacion_grass=grass_reservado.pop(int(input("ingrese el indice de los horarios disponibles: ")) -1)
        print(f"ha reservado el grass {reservacion_grass}")
    elif opcion == 3:
        pago_alquiler:int=35
        print(f"el pago por el alquiler del grass es de s/{pago_alquiler}")
    elif opcion == 4:
        print("su reservacion de grass")
        for i in enumerate(grass_reservado,1):
            print(f"{reservacion_grass} y el pago del alquiler es s/.{pago_alquiler}")



