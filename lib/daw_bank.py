from lib.cuenta_bancaria import CuentaBancaria

class DawBank:
    def main(self):
        pass

    def imprimir_menu(self):
        print("¡Bienvenido a DawBank!\n"
              "Elige una de las siguientes opciones introduciendo el número "
              "correspondiente a la opción deseada:\n"
              "1. Datos de la cuenta.\n"
              "2. IBAN.\n"
              "3. Titular.\n"
              "4. Saldo.\n"
              "5. Ingreso.\n"
              "6. Retirada.\n"
              "7. Movimientos.\n"
              "8. Salir. ")

    # def imprimir_movimientos(self):
    #     if len(CuentaBancaria.movimientos) == 0:
    #         print("No tiene movimientos registrados")
    #     contador: int = 1
    #     for movimiento in CuentaBancaria.movimientos:
    #         if movimiento < 0:
    #             print(f"{contador}. Retirada: {- movimiento}€")
    #         else:
    #             print(f"{contador}. Ingreso: {movimiento}€")
    #         contador += 1