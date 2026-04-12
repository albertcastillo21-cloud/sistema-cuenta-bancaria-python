from cuenta import CuentaBancaria
"""
Creamos las instacias de la clase
para agregarle argumentos, para 
hacer prueba de la Clase y comprobar
que esta funcionando correctamente.

"""
cuenta1 = CuentaBancaria("001", "Albert Castro",) 
cuenta2 = CuentaBancaria("002", "Fenella Peña",)
cuenta3 = CuentaBancaria("003", "Aurora Castillo",)
cuenta4 = CuentaBancaria("005", "Luis Hernandez", )

# === DEPOSITOS ===

# Hacemos deposito de un monto de dinero a cada cuenta.

print(cuenta1.depositar(1000))
print(cuenta2.depositar(2000))
print(cuenta3.depositar(-500))
print(cuenta4.depositar(3000))
# Hacemos un retiro de dos cuentas y en una cuenta comprobamos la validacion de los datos.

print(cuenta1.retirar(1000)) # Retiro de forma correcta.
print(cuenta3.retirar(-500)) # Retiro de forma negativa para comprobar que no haga ningun cambio en el balance de la cuenta.
print(cuenta2.retirar("500")) # Retiro en string para demostrar que no acepta string y lanza un mensaje que 
print(cuenta4.retirar(99999)) #Retiro de un monto mucho mayor al que hay en la cuenta.

# === VALIDACIONES ===

# Comprobar balance de cada cuenta, demostrando que todo funciono correctamente.

print(cuenta1.comprobar_balance())
print(cuenta2.comprobar_balance())
print(cuenta4.comprobar_balance())
print(cuenta3.comprobar_balance())

#Vemos el historial de transacion de la cuenta requeridad.

print(cuenta2.ver_transacciones())









