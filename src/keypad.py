"""Driver de keypad matricial 4x4 com varredura nao-bloqueante.

A funcao `scan()` deve ser chamada repetidamente no loop principal.
Ela retorna a tecla pressionada apenas no instante da transicao
"liberada -> pressionada", evitando autorrepeticao e fazendo
debounce sem nenhum sleep bloqueante.
"""

from machine import Pin


KEYS = (
    ("1", "2", "3", "A"),
    ("4", "5", "6", "B"),
    ("7", "8", "9", "C"),
    ("*", "0", "#", "D"),
)


class Keypad:
    def __init__(self, linhas, colunas):
        # Linhas: saidas em nivel alto no idle. Levamos uma a uma para 0
        # durante a varredura.
        self._linhas = [Pin(p, Pin.OUT, value=1) for p in linhas]
        # Colunas: entradas com pull-up. Quando uma tecla e' pressionada,
        # ela conecta a coluna correspondente a' linha em LOW.
        self._colunas = [Pin(p, Pin.IN, Pin.PULL_UP) for p in colunas]
        self._ultima = None

    def scan(self):
        """Retorna a tecla recem-pressionada (str) ou None."""
        atual = self._ler_atual()

        # Reporta apenas em transicao para evitar repeticoes.
        if atual is not None and atual != self._ultima:
            self._ultima = atual
            return atual
        if atual is None:
            self._ultima = None
        return None

    def _ler_atual(self):
        for i, linha in enumerate(self._linhas):
            linha.value(0)
            for j, coluna in enumerate(self._colunas):
                if coluna.value() == 0:
                    linha.value(1)
                    return KEYS[i][j]
            linha.value(1)
        return None
