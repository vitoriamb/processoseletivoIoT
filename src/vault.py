"""Maquina de estados do cofre eletronico.

Cinco estados:
    LOCKED    - aguardando a primeira tecla; trava fechada.
    ENTERING  - usuario digitando o PIN; mostra mascara.
    UNLOCKED  - PIN correto; trava aberta com auto-relock.
    DENIED    - PIN incorreto; feedback rapido antes de voltar a LOCKED
                (ou ir para BLOCKED se atingiu o limite de tentativas).
    BLOCKED   - 3 falhas consecutivas; alarme com LED vermelho piscando
                e buzzer intermitente, por BLOCKED_TIMEOUT_MS.

A classe nao bloqueia. `on_key(tecla)` reage a uma tecla recem-digitada
e `tick(now_ms)` deve ser chamada continuamente para evoluir timeouts e
o padrao de alarme. Toda contagem de tempo usa `time.ticks_ms()`/
`ticks_diff()` para tolerar overflow do clock.
"""

import time


class State:
    LOCKED = 0
    ENTERING = 1
    UNLOCKED = 2
    DENIED = 3
    BLOCKED = 4


class Vault:
    PIN_LEN = 4
    MAX_TENTATIVAS = 3

    UNLOCK_TIMEOUT_MS = 5000
    DENIED_TIMEOUT_MS = 1000
    BLOCKED_TIMEOUT_MS = 10000
    ALARM_BLINK_MS = 250

    BEEP_OK_FREQ = 1500
    BEEP_OK_MS = 300
    BEEP_ERRO_FREQ = 400
    BEEP_ERRO_MS = 800

    def __init__(self, pin_correto, ui):
        self._pin_correto = pin_correto
        self._ui = ui
        self._state = State.LOCKED
        self._buffer = ""
        self._tentativas = 0
        self._t_entrada = 0
        self._t_alarme = 0
        self._beep_off_at = 0
        self._led_alarme = False
        self._enter_locked()

    def on_key(self, tecla):
        # Em DENIED ou BLOCKED ignoramos teclas para evitar bypass por
        # spam. Em UNLOCKED tambem -- aguarde o auto-relock.
        if self._state in (State.DENIED, State.BLOCKED, State.UNLOCKED):
            return

        if tecla == "*":
            # Cancela e volta ao estado inicial.
            self._enter_locked()
            return

        if tecla == "#":
            self._verificar()
            return

        if tecla.isdigit() and len(self._buffer) < self.PIN_LEN:
            self._buffer += tecla
            self._enter_entering()

    def tick(self, now_ms):
        # Beep com fim agendado: desliga sozinho.
        if self._beep_off_at and time.ticks_diff(now_ms, self._beep_off_at) >= 0:
            self._ui.silenciar()
            self._beep_off_at = 0

        if self._state == State.UNLOCKED:
            if time.ticks_diff(now_ms, self._t_entrada) >= self.UNLOCK_TIMEOUT_MS:
                self._enter_locked()

        elif self._state == State.DENIED:
            if time.ticks_diff(now_ms, self._t_entrada) >= self.DENIED_TIMEOUT_MS:
                if self._tentativas >= self.MAX_TENTATIVAS:
                    self._enter_blocked(now_ms)
                else:
                    self._enter_locked()

        elif self._state == State.BLOCKED:
            if time.ticks_diff(now_ms, self._t_entrada) >= self.BLOCKED_TIMEOUT_MS:
                self._tentativas = 0
                self._enter_locked()
            elif time.ticks_diff(now_ms, self._t_alarme) >= self.ALARM_BLINK_MS:
                # Alterna LED e beep para padrao de alarme.
                self._t_alarme = now_ms
                self._led_alarme = not self._led_alarme
                self._ui.piscar_vermelho(self._led_alarme)
                if self._led_alarme:
                    self._ui.beep_ligar(self.BEEP_ERRO_FREQ)
                else:
                    self._ui.silenciar()

    def _verificar(self):
        if self._buffer == self._pin_correto:
            self._enter_unlocked()
        else:
            self._tentativas += 1
            self._enter_denied()

    def _agendar_beep(self, freq, duracao_ms):
        self._ui.beep_ligar(freq)
        self._beep_off_at = time.ticks_add(time.ticks_ms(), duracao_ms)

    def _enter_locked(self):
        self._state = State.LOCKED
        self._buffer = ""
        self._ui.silenciar()
        self._beep_off_at = 0
        self._ui.abrir_trava(False)
        self._ui.set_led("vermelho")
        self._ui.mostrar("Cofre Trancado", "Digite a senha:")
        print("Estado: LOCKED")

    def _enter_entering(self):
        self._state = State.ENTERING
        mascara = "*" * len(self._buffer) + "_" * (self.PIN_LEN - len(self._buffer))
        self._ui.mostrar("Senha:", mascara)

    def _enter_unlocked(self):
        self._state = State.UNLOCKED
        self._tentativas = 0
        self._t_entrada = time.ticks_ms()
        self._ui.set_led("verde")
        self._ui.abrir_trava(True)
        self._agendar_beep(self.BEEP_OK_FREQ, self.BEEP_OK_MS)
        self._ui.mostrar("Cofre Aberto", "Bem-vindo!")
        print("Estado: UNLOCKED")

    def _enter_denied(self):
        self._state = State.DENIED
        self._buffer = ""
        self._t_entrada = time.ticks_ms()
        self._ui.set_led("vermelho")
        self._ui.abrir_trava(False)
        self._agendar_beep(self.BEEP_ERRO_FREQ, self.BEEP_ERRO_MS)
        self._ui.mostrar(
            "Senha Incorreta",
            "Tentativa {}/{}".format(self._tentativas, self.MAX_TENTATIVAS),
        )
        print("Estado: DENIED tentativa={}".format(self._tentativas))

    def _enter_blocked(self, now_ms):
        self._state = State.BLOCKED
        self._t_entrada = now_ms
        self._t_alarme = now_ms
        self._led_alarme = True
        self._ui.set_led("vermelho")
        self._ui.abrir_trava(False)
        self._ui.beep_ligar(self.BEEP_ERRO_FREQ)
        self._ui.mostrar("BLOQUEADO!", "Aguarde 10s")
        print("Estado: BLOCKED")
