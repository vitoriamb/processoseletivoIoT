"""Camada de saida do cofre: LCD I2C 16x2, LEDs, buzzer e servo.

Encapsula todo o hardware de saida atras de uma interface de alto nivel.
A maquina de estados (`vault.py`) so' chama metodos como `mostrar`,
`set_led`, `beep_ligar` e `abrir_trava` -- nao toca em pinos diretamente.
"""

from machine import Pin, I2C, PWM

from i2c_lcd import I2cLcd


# Servo SG90: 50 Hz com pulso de 0.5 ms (0 graus) a 2.5 ms (180 graus).
# Para o duty 10-bit do MicroPython no ESP32:
#   duty = (pulso_ms / 20) * 1023
# Aqui usamos 0 graus (trava fechada) e 90 graus (trava aberta).
_SERVO_DUTY_FECHADO = 26   # ~0.5 ms
_SERVO_DUTY_ABERTO = 77    # ~1.5 ms


class UI:
    LCD_ADDR = 0x27

    def __init__(self, lcd_sda, lcd_scl, led_verde, led_vermelho, buzzer, servo_pwm):
        i2c = I2C(0, sda=Pin(lcd_sda), scl=Pin(lcd_scl), freq=400_000)
        self._lcd = I2cLcd(i2c, self.LCD_ADDR, 2, 16)

        self._led_v = Pin(led_verde, Pin.OUT, value=0)
        self._led_r = Pin(led_vermelho, Pin.OUT, value=0)

        self._buzzer = PWM(Pin(buzzer), freq=2000, duty=0)
        self._servo = PWM(Pin(servo_pwm), freq=50, duty=_SERVO_DUTY_FECHADO)

    def mostrar(self, linha1="", linha2=""):
        """Reescreve as duas linhas do LCD truncando em 16 colunas."""
        self._lcd.clear()
        self._lcd.move_to(0, 0)
        self._lcd.putstr(linha1[:16])
        if linha2:
            self._lcd.move_to(0, 1)
            self._lcd.putstr(linha2[:16])

    def set_led(self, cor):
        """`cor` deve ser 'verde', 'vermelho' ou 'nenhum'."""
        self._led_v.value(1 if cor == "verde" else 0)
        self._led_r.value(1 if cor == "vermelho" else 0)

    def piscar_vermelho(self, ligado):
        self._led_r.value(1 if ligado else 0)

    def beep_ligar(self, freq):
        self._buzzer.freq(freq)
        self._buzzer.duty(512)

    def silenciar(self):
        self._buzzer.duty(0)

    def abrir_trava(self, abrir):
        self._servo.duty(_SERVO_DUTY_ABERTO if abrir else _SERVO_DUTY_FECHADO)
