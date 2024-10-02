# crear una clase banco
# sus atrutos seran nombre, apellidos, dni, numero de cuenta, y saldo inicial
# como metodos podremos hacer depositar, retirar dinero, y ver estado de cuenta

class Banco:
    def __init__(self,nombre,apellidos,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo_inicial
    
    def depositar(self,cantidad):
        self.saldo += cantidad
        print(f"depositaste: {cantidad}. saldo_actual: {self.saldo}")

    def retirar(self,cantidad_retirar):
        self.saldo -= cantidad_retirar
        print(f"retiraste: {cantidad_retirar}. saldo_actual: {self.saldo}")

    def estado_cuenta(self):
       print(f"estado de cuenta de: {self.nombre} {self.apellidos}")
       print(f"numero de cuenta: {self.numero_cuenta}")
       print(f"saldo: {self.saldo}")



luna=Banco("luna","lince",79384756,1989843878,20)
luna.depositar(200)
luna.retirar(100)
luna.estado_cuenta()

# crear una clase agencia con sus atributos nombre, apellido del pasajero, dni, numero de asiento y fecha de viaje
# sus metodos seran ingresar origen, ingresar destino, cancelar y ver estado de pasaje

class Agencia:
    def __init__(self,nombre,apellido,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje

    def ingresar_origen(self,origen):
        self.origen =origen
        print(f"su origen es: {self.origen}")

    def ingresar_destino(self,destino):
        self.destino=destino
        print(f"su destino es: {self.destino}")

    def cancelar_viaje(self):
        self.viaje_cancelado = True
        print("su viaje ha sido cancelado")
    
    def estado_pasaje(self):
        print(f"estado de pasaje del cliente: {self.nombre} {self.apellido}")
        print(f"numero de asiento: {self.numero_asiento}")
        print(f"fecha de viaje: {self.fecha_viaje}")
        print(f"su origen es: {self.origen}")
        print(f"su destino es: {self.destino}")

juan=Agencia("juan","salaz",74532874,19,"20-12-2024")
juan.ingresar_origen("puquio")
juan.ingresar_destino("lima")
juan.estado_pasaje()
juan.cancelar_viaje()