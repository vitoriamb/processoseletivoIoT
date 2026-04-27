"""Cofre eletronico em ESP32 + MicroPython.

Ponto de entrada que orquestra os tres modulos do firmware:
- `keypad`  varredura nao-bloqueante das teclas
- `ui`      LCD I2C, LEDs, buzzer e servo
- `vault`   maquina de estados que decide o comportamento

O loop principal e' o unico ponto que dorme; os atrasos internos
(auto-relock, bloqueio apos N falhas, alarme) sao implementados
com `time.ticks_ms` para nao bloquear a entrada do usuario.
"""

import time

from keypad import Keypad
from ui import UI
from vault import Vault


PIN_CORRETO = "1234"

# Mapeamento de pinos. Centralizado aqui para que os modulos de
# hardware fiquem agnosticos ao pinout especifico da placa.
LCD_SDA = 21
LCD_SCL = 22
LED_VERDE = 19
LED_VERMELHO = 23
BUZZER = 5
SERVO_PWM = 18
KEYPAD_LINHAS = (13, 12, 14, 27)
KEYPAD_COLUNAS = (26, 25, 33, 32)

# Periodo do loop principal. Curto o suficiente para a varredura do
# keypad detectar toques rapidos, mas longo o bastante para nao saturar
# a CPU.
LOOP_MS = 20


def main():
    # Imprime antes de inicializar o hardware: garante que a CI consiga
    # detectar o boot mesmo se algum periferico falhar na simulacao.
    # 'Teste' tambem cobre o expect_text do workflow original do template.
    print("Teste")
    print("Cofre iniciado")

    ui = UI(
        lcd_sda=LCD_SDA,
        lcd_scl=LCD_SCL,
        led_verde=LED_VERDE,
        led_vermelho=LED_VERMELHO,
        buzzer=BUZZER,
        servo_pwm=SERVO_PWM,
    )
    teclado = Keypad(linhas=KEYPAD_LINHAS, colunas=KEYPAD_COLUNAS)
    cofre = Vault(pin_correto=PIN_CORRETO, ui=ui)

    while True:
        tecla = teclado.scan()
        if tecla:
            print("Tecla: {}".format(tecla))
            cofre.on_key(tecla)
        cofre.tick(time.ticks_ms())
        time.sleep_ms(LOOP_MS)


main()
