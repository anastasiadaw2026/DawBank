from lib.cuenta_bancaria import CuentaBancaria

class DawBank:
    def main(self):
        opcion_elegida: int = 0
        iban_elegido: str = ''
        titular_elegido: str = ''
        ingreso: float = 0.0

        print("¡Bienvenido a DawBank!\n"
              "Primero, vamos a crear una cuenta.")
        iban_elegido = input('Introduce el IBAN: ')
        titular_elegido = input('Introduce el titular de la cuenta: ')
        cuenta = CuentaBancaria(iban_elegido, titular_elegido)
        if cuenta.iban == '' or cuenta.titular == '':
            print('Alguno de lso datos ha sido introducido incorrectamente, '
                  'intentalo de nuevo')
            self.main()

        while opcion_elegida != 8:
            self.imprimir_menu()
            opcion_elegida = int(input(': '))
            match opcion_elegida:
                case 1:
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

    def imprimir_menu(self):
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

    def imprimir_movimientos(self, movimientos: list):
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
