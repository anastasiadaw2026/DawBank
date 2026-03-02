from lib.cuenta_bancaria import CuentaBancaria


class DawBank:
    class ConstantesMenu:
        SALIDA: int = 8
        OPCION_UNO = 1
        OPCION_DOS = 2
        OPCION_TRES = 3
        OPCION_CUATRO = 4
        OPCION_CINCO = 5
        OPCION_SEIS = 6
        OPCION_SIETE = 7

    def main(self) -> None:
        opcion_elegida: int = 0
        ingreso: float = 0.0

        print("¡Bienvenido a DawBank!\n"
              "Primero, vamos a crear una cuenta.")
        cuenta = self.crear_cuenta()

        while opcion_elegida != DawBank.ConstantesMenu.SALIDA:
            self.imprimir_menu()
            opcion_elegida = int(input(': '))
            self.ejecutar_opcion_elegida(cuenta, opcion_elegida)


    def imprimir_menu(self) -> None:
        print("Elige una de las siguientes opciones introduciendo el número "
              "correspondiente a la opción deseada:\n"
              "1. Datos de la cuenta.\n"
              "2. IBAN.\n"
              "3. Titular.\n"
              "4. Saldo.\n"
              "5. Ingreso.\n"
              "6. Retirada.\n"
              "7. Movimientos.\n"
              "8. Salir. ")

    def imprimir_movimientos(self, movimientos: list) -> None:
        contador: int = 1
        print('Movimientos: ')
        if len(movimientos) == 0:
            print(" No tiene movimientos registrados")
        for movimiento in movimientos:
            if movimiento < 0:
                print(f"    {contador}. Retirada: {- movimiento}€")
            else:
                print(f"    {contador}. Ingreso: {movimiento}€")
            contador += 1

    def crear_cuenta(self) -> CuentaBancaria:
        iban_elegido: str = ''
        titular_elegido: str = ''
        iban_elegido = input('Introduce el IBAN: ')
        titular_elegido = input('Introduce el titular de la cuenta: ')
        cuenta1 = CuentaBancaria(iban_elegido, titular_elegido)
        if cuenta1.iban == '' or cuenta1.titular == '':
            print('Alguno de los datos ha sido introducido incorrectamente, '
                  'intentalo de nuevo')
            self.crear_cuenta()
        return cuenta1

    def ejecutar_opcion_elegida(self, cuenta: CuentaBancaria,
                                opcion_elegida: int) -> None:
        match opcion_elegida:
            case DawBank.ConstantesMenu.OPCION_UNO:
                print(f'IBAN: {cuenta.iban}\n'
                      f'Titular: {cuenta.titular}\n'
                      f'Saldo disponible: {round(cuenta.saldo, 2)}€')
            case 2:
                print(f'IBAN: {cuenta.iban}')
            case 3:
                print(f'Titular: {cuenta.titular}')
            case 4:
                print(f'Saldo disponible: {round(cuenta.saldo, 2)}€')
            case 5:
                ingreso = float(input('Introduce el ingreso: '))
                if cuenta.introducir_ingreso(ingreso):
                    print('Ingreso registrado.')
                else:
                    print('El ingreso que has introducido '
                          'es incorrecto.')
            case 6:
                retirada = float(input('Introduce la retirada: '))
                if cuenta.introducir_retirada(retirada):
                    print('Retirada registrada.')
                else:
                    print('La retirada que has introducido '
                          'es incorrecta.')
            case 7:
                self.imprimir_movimientos(cuenta.movimientos)
            case 8:
                print('¡Adios!')
            case _:
                print('Número introducido incorrectamente, intentalo de '
                      'nuevo.')

DawBank().main()