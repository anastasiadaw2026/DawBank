from lib.constantes import Constantes


class CuentaBancaria:
    def __init__(self, iban: str, titular: str):
        self._iban: str = 0 # poner aquí un comprobar iban def
        self._titular: str = titular
        self._saldo: float = 0.0
        self._movimientos: list[float] = []

    @property
    def iban(self):
        return self._iban

    @property
    def titular(self):
        return self._titular

    # cambios en el saldo y registro en los movimientos
    def introducir_ingreso(self, ingreso):
        if isinstance(float, ingreso) and ingreso > 0:
            self._saldo += ingreso
            if ingreso > Constantes.INGRESO_MAXIMO:
                print("AVISO: Notificar a hacienda.")
            self.comprobar_movimientos()
            self._movimientos.append(ingreso)
        else:
            print("Error: el ingreso introducido no es un valor numérico o "
                  "es un valor negativo, intentalo de nuevo.")

    def introducir_retirada(self, retirada):
        if isinstance(float, retirada) and retirada > 0:
            self._saldo -= retirada
            if self._saldo <= Constantes.SALDO_MINIMO:
                print("AVISO: Saldo negativo.")
            self.comprobar_movimientos()
            self._movimientos.append(- retirada)
        else:
            print("Error: la retirada introducida no es un valor "
                  "numérico o es un valor negativo, intentalo de nuevo.")

    def comprobar_movimientos(self):
        if len(self._movimientos) > Constantes.MAXIMO_MOVIMIENTOS:
            # borramos el historial después de realizar más de 100 movimientos
            self._movimientos = []

    def imprimir_movimientos(self):
        contador: int = 1
        for movimiento in self._movimientos:
            if movimiento < 0:
                print(f"{contador}. Retirada: {- movimiento}€")
            else:
                print(f"{contador}. Ingreso: {movimiento}€")
            contador += 1

cuenta = CuentaBancaria('123', 'abcabc abc abc')
print(cuenta.iban, cuenta.titular)
