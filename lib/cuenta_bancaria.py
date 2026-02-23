from lib.constantes import Constantes
import re

class CuentaBancaria:
    def __init__(self, iban: str, titular: str):
        self._iban: str = self._comprobar_iban(iban)
        self._titular: str = titular
        self._saldo: float = 0.0
        self._movimientos: list[float] = []

    @property
    def iban(self):
        return self._iban

    @property
    def titular(self):
        return self._titular

    def _comprobar_iban(self, valor):
        patron = re.compile(r'[A-Z]{2}\d{22}')
        valor1 = valor.replace(' ', '')
        if len(valor1) == Constantes.LONGITUD_IBAN and patron.match(valor1):
            return valor
        else:
            return None

    def _comprobar_titular(self, valor):
        pass

    # cambios en el saldo y registro en los movimientos
    def introducir_ingreso(self, ingreso):
        if ingreso > 0 and isinstance(ingreso, float):
            self._saldo += ingreso
            if ingreso > Constantes.INGRESO_MAXIMO:
                print("AVISO: Notificar a hacienda.")
            self.comprobar_movimientos()
            self._movimientos.append(ingreso)
        else:
            print("Error: el ingreso introducido no es un valor numérico o "
                  "es un valor negativo, intentalo de nuevo.")

    def introducir_retirada(self, retirada):
        if retirada > 0 and isinstance(retirada, float):
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

    def imprimir_movimientos(self): # hacerlo en DawBank y hacerle un return
        # no un print mejor
        if len(self._movimientos) == 0:
            print("No tiene movimientos registrados")
        contador: int = 1
        for movimiento in self._movimientos:
            if movimiento < 0:
                print(f"{contador}. Retirada: {- movimiento}€")
            else:
                print(f"{contador}. Ingreso: {movimiento}€")
            contador += 1

cuenta = CuentaBancaria('ES1234567890123456789012345555', 'abcabc abc abc')
print(cuenta.iban, cuenta.titular)
cuenta.introducir_ingreso(90)
cuenta.imprimir_movimientos()