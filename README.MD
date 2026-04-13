OBJETIVO :

Aplicar los conceptos fundamentales de POO en Python construyendo una simulación básica de cuentas bancarias con validación de datos, registro de transacciones y manejo de estados.

ESTRUCTURA DEL PROYECTO 

├── cuenta.py   # Clase CuentaBancaria con lógica de negocio
└── main.py     # Instancias de prueba y casos de validación

FUNCIONALIDADES 

Depósito y retiro de fondos con validación de tipo y valor.
Rechazo de operaciones con montos negativos, cero, string o booleanos.
Validación de fondos insuficientes en retiros.
Registro automático de cada transacción con timestamp.
Consulta de balance y historial de movimientos.

Conceptos de POO aplicados

Clases e instancias.
Método __init__ y __str__.
Encapsulamiento de lógica en métodos.
Método central reutilizable (registrar_transaccion).
Manejo de tipos y validaciones con isinstance.

python main.py

EJEMPLO DE SALIDA: 

cuenta1 = CuentaBancaria("001", "Albert Castro")
print(cuenta1.depositar(1000))
# {'Tipo': 'Deposito', 'Monto': 1000, 'Estado': 'valido', 'Mensaje': 'Deposito realizado correctamente', 'Balance': 1000, 'Timestamp': '...'}

print(cuenta1.retirar(99999))
# {'Tipo': 'Retiro', 'Monto': 99999, 'Estado': 'invalido', 'Mensaje': 'Fondos insuficientes', ...}

ESTADO DEL PROYECTO

Versión inicial de práctica. En desarrollo activo — próximas mejoras planeadas:

 Persistencia de transacciones en archivo CSV/JSON.
 Tests unitarios con pytest.
 Logging con módulo logging en lugar de returns directos.
 Transferencias entre cuentas.

Certificación relacionada
IBM Data Engineer Professional Certificate — Coursera
Módulo: Python for Data Science, AI & Development