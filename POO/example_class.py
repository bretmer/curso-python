class Banco:
    def __init__(self, name, lastname, cui, account, amount):
        self.name = name
        self.lastname = lastname
        self.cui = cui
        self.account = account
        self.amount = amount
        self.transaction_history = []

    def deposit(self, amount):
        self.amount += amount
        self.transaction_history.append(f"Depositaste: s/.{amount}") 

    def remove_cash(self, amount):
        if amount > self.amount:
            return "No cuentas con saldo suficiente"
        self.amount -= amount
        self.transaction_history.append(f"Retiraste: s/.{amount}")  

    def status_account(self):
        response = f"""
        ------ BIENVENIDO AL BANCO "TEPINCHA Y ESTAFA" ------
        Cliente: {self.name}, {self.lastname}  NroCuenta: {self.account}.
        En estos momentos tienes un saldo de: s/.{self.amount},
        Historial de transacciones:
        """
        for transaction in self.transaction_history:
            response += f"{transaction}\n"
        response += "Fin del voucher:\n"
        response += "___________________________________________________________________"
        return response

# Example 
cliente_miguel = Banco("Miguelito", "Barraza", 784512963, 4545, 30)
cliente_miguel.deposit(200)
cliente_miguel.remove_cash(100)
print(cliente_miguel.status_account())
cliente_miguel.deposit(300)
cliente_miguel.remove_cash(30)
print(cliente_miguel.status_account())