from datetime import datetime

class CuentaBancaria:

    def __init__(self, numero_cuenta, nombre_titular, balance=0):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
        self.transaccion = [] 

    def __str__(self):
        return f"Cuenta[{self.numero_cuenta}] - Titular: {self.nombre_titular} - Saldo: ${self.balance}"

    # FUNCIÓN CENTRAL (LA MÁS IMPORTANTE)
    def registrar_transaccion(self, tipo, monto, estado, mensaje):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

        transaccion = {
            "Tipo": tipo,
            "Monto": monto,
            "Estado": estado,
            "Mensaje": mensaje,
            "Balance": self.balance,
            "Timestamp": timestamp
        }

        self.transaccion.append(transaccion)

        return transaccion  

    # DEPÓSITO
    def depositar(self, cantidad):

        # 1. validar tipo
        if not isinstance(cantidad, (int, float) or isinstance(cantidad,bool)):
            return self.registrar_transaccion(
                "Deposito", cantidad, "invalido", "Tipo de dato incorrecto"
            )

        # 2. validar valor
        if cantidad <= 0:
            return self.registrar_transaccion(
                "Deposito", cantidad, "invalido", "Monto debe ser mayor a 0"
            )

        # 3. ejecutar
        self.balance = round(self.balance + cantidad, 2)

        return self.registrar_transaccion(
            "Deposito", cantidad, "valido", "Deposito realizado correctamente"
        )

    # RETIRO
    def retirar(self, cantidad):

        # 1. validar tipo
        if not isinstance(cantidad, (int, float) or isinstance(cantidad,bool)):
            return self.registrar_transaccion(
                "Retiro", cantidad, "invalido", "Tipo de dato incorrecto"
            )

        # 2. validar valor
        if cantidad <= 0:
            return self.registrar_transaccion(
                "Retiro", cantidad, "invalido", "Monto debe ser mayor a 0"
            )

        # 3. validar fondos
        if cantidad > self.balance:
            return self.registrar_transaccion(
                "Retiro", cantidad, "invalido", "Fondos insuficientes"
            )

        # 4. ejecutar
        self.balance = round(self.balance - cantidad, 2)

        return self.registrar_transaccion(
            "Retiro", cantidad, "valido", "Retiro realizado correctamente"
        )

    def comprobar_balance(self):
        return {"balance": self.balance}

    def ver_transacciones(self):
        return self.transaccion