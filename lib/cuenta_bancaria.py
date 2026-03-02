import re

class CuentaBancaria:
    class Constantes:
        MAXIMO_MOVIMIENTOS = 100
        SALDO_MINIMO = -50
        INGRESO_MAXIMO = 3000
    def __init__(self, iban: str, titular: str):
        self._iban: str = self._comprobar_iban(iban)
        self._titular: str = self._comprobar_titular(titular)
        self._saldo: float = 0.0
        self._movimientos: list[float] = []

    @property
    def iban(self):
        return self._iban

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def movimientos(self):
        return self._movimientos

    def _comprobar_iban(self, valor: str) -> str:
        patron = re.compile(r'^[A-Z]{2}\d{22}$')
        valor1 = valor.replace(' ', '')
        if patron.match(valor1):
            return valor
        else:
            return ''

    def _comprobar_titular(self, valor: str) -> str:
        patron = re.compile(r'^[A-ZÉÍÁÓÚ][a-zñáéíóú]+[ ]['
                            r'A-Za-zÁÉÍÓÚÑáéíóúñ^\s]+$')
        if patron.match(valor):
            return valor
        else:
            return ''

    def _aniadir_movimiento(self, movimiento: float) -> None:
        if (len(self._movimientos) >
                CuentaBancaria.Constantes.MAXIMO_MOVIMIENTOS):
            self._movimientos = []
        self._movimientos += [movimiento]

    def introducir_ingreso(self, ingreso: float) -> bool:
        if ingreso > 0 and isinstance(ingreso, float):
            self._saldo += ingreso
            if ingreso > CuentaBancaria.Constantes.INGRESO_MAXIMO:
                print("AVISO: Notificar a hacienda.")
            self._aniadir_movimiento(ingreso)
            return True
        return False

    def introducir_retirada(self, retirada: float) -> bool:
        if retirada > 0 and isinstance(retirada, float):
            self._saldo -= retirada
            if self._saldo <= CuentaBancaria.Constantes.SALDO_MINIMO:
                print("AVISO: Saldo negativo.")
            self._aniadir_movimiento(-retirada)
            return True
        return False
