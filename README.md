# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo:** _preencher_
- **GitHub:** _preencher_

---

## 1️⃣ Visão Geral da Solução

**Projeto:** Cofre Eletrônico em ESP32 + MicroPython, simulado no Wokwi.

O sistema bloqueia uma trava (servo motor) até que o usuário digite uma senha de 4 dígitos em um teclado matricial. Um LCD I2C 16x2 mostra instruções e estados, dois LEDs (verde/vermelho) sinalizam abertura/bloqueio e um buzzer emite feedback sonoro de acerto, erro e alarme.

**Como o usuário interage:**

- Digita 4 dígitos no keypad.
- `*` cancela o que digitou e zera o buffer.
- `#` confirma a senha (PIN padrão: `1234`).
- Acertou: trava abre por 5 s, depois religa sozinha.
- Errou: feedback de erro e nova tentativa. Após **3 erros consecutivos**, o cofre entra em modo de **alarme** por 10 s (LED vermelho piscando + buzzer intermitente) e bloqueia novas tentativas.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O firmware está dividido em **três módulos próprios** com responsabilidades bem delimitadas, mais dois drivers reutilizados de domínio público para o LCD.

| Arquivo | Responsabilidade |
| --- | --- |
| [`src/main.py`](src/main.py) | Configuração de pinos, instanciação dos módulos e loop principal não-bloqueante. |
| [`src/keypad.py`](src/keypad.py) | Driver do teclado: varredura linha-a-linha **não-bloqueante** com debounce por estado (só reporta a tecla na transição "soltou → pressionou", evitando autorrepetição). |
| [`src/ui.py`](src/ui.py) | Camada de saída: LCD I2C, LEDs, buzzer (PWM) e servo (PWM 50 Hz). Expõe métodos de alto nível (`mostrar`, `set_led`, `beep_ligar`, `abrir_trava`). |
| [`src/vault.py`](src/vault.py) | Máquina de estados pura. Recebe teclas e ticks de tempo e chama a UI. Não toca em GPIO. |
| [`src/lcd_api.py`](src/lcd_api.py), [`src/i2c_lcd.py`](src/i2c_lcd.py) | Drivers HD44780 + PCF8574 (portados de [dhylands/python_lcd](https://github.com/dhylands/python_lcd), MIT). |

### Fluxo do `main.py`

```python
while True:
    tecla = teclado.scan()         # nao bloqueia
    if tecla:
        cofre.on_key(tecla)        # alimenta a maquina de estados
    cofre.tick(time.ticks_ms())    # evolui timeouts e alarme
    time.sleep_ms(20)              # unico ponto de pausa
```

### Diagrama de estados do cofre

```mermaid
stateDiagram-v2
    [*] --> LOCKED
    LOCKED --> ENTERING: digito
    ENTERING --> ENTERING: digito (ate 4)
    ENTERING --> LOCKED: tecla *
    ENTERING --> UNLOCKED: # e PIN ok
    ENTERING --> DENIED: # e PIN errado
    DENIED --> LOCKED: timeout 1s e tentativas menor que 3
    DENIED --> BLOCKED: 3 tentativas erradas
    BLOCKED --> LOCKED: timeout 10s
    UNLOCKED --> LOCKED: timeout 5s
```

### Pinout (ESP32 DevKit C V4)

| Função | GPIO |
| --- | --- |
| Keypad linhas (saída) | 13, 12, 14, 27 |
| Keypad colunas (entrada pull-up) | 26, 25, 33, 32 |
| LCD I2C SDA / SCL | 21 / 22 |
| Servo (PWM 50 Hz) | 18 |
| LED verde | 19 |
| LED vermelho | 23 |
| Buzzer (PWM) | 5 |

---

## 3️⃣ Componentes Utilizados na Simulação

Definidos em [`diagram.json`](diagram.json):

| Componente | Tipo Wokwi | Função |
| --- | --- | --- |
| Microcontrolador | `board-esp32-devkit-c-v4` | Roda o MicroPython e a lógica do cofre. |
| Teclado matricial 4x4 | `wokwi-membrane-keypad` | Entrada da senha. |
| LCD 16x2 com I2C | `wokwi-lcd1602` (atributo `pins: i2c`) | Exibe estado e instruções. |
| Servo SG90 | `wokwi-servo` | Trava física (0° fechado, 90° aberto). |
| LED verde | `wokwi-led` (`green`) | Indica cofre aberto. |
| LED vermelho | `wokwi-led` (`red`) | Indica cofre trancado e pisca em alarme. |
| Buzzer | `wokwi-buzzer` | Beeps de confirmação, erro e alarme. |
| 2 × resistor 220 Ω | `wokwi-resistor` | Limitação de corrente dos LEDs. |

**Convenção de cores dos fios** (para legibilidade no diagrama):

- Vermelho — alimentação (3V3 / VIN)
- Preto — GND
- Verde — SDA / linhas do keypad
- Azul — SCL / colunas do keypad
- Laranja — sinais PWM (servo, buzzer)
- Amarelo — saídas digitais para LEDs

---

## 4️⃣ Decisões Técnicas Relevantes

**Máquina de estados explícita.** Em vez de `if`s aninhados sobre flags, modelei cinco estados (`LOCKED`, `ENTERING`, `UNLOCKED`, `DENIED`, `BLOCKED`) com transições claras. Cada estado tem uma função `_enter_*` que aplica o efeito visual/sonoro e ações no `tick`. Isso elimina ambiguidades do tipo "estou digitando, mas o cofre está aberto?" e simplifica a verificação manual.

**Temporização não-bloqueante (`time.ticks_ms`).** Todos os timeouts (auto-relock 5 s, retorno após erro 1 s, bloqueio 10 s, alarme 250 ms on/off) usam `time.ticks_ms()` + `time.ticks_diff()`. O loop principal nunca dorme mais que 20 ms, então a UI permanece responsiva. Em sistemas embarcados, qualquer `sleep` longo é um cofre que ignora um `*` para cancelar — exatamente o que queremos evitar.

**Modularização em três arquivos próprios.** Separação clara entre **driver de hardware** (`keypad.py`, `ui.py`) e **lógica de negócio** (`vault.py`). A lógica não conhece pinos: recebe um objeto `ui` injetado. Trocar o LCD por OLED, por exemplo, mexeria apenas em `ui.py`.

**Debounce por transição no keypad.** Em vez de `sleep_ms(50)` após detectar tecla (bloqueante e perde toques rápidos), `scan()` só reporta a tecla quando ela acabou de ser pressionada — guardando a última leitura entre chamadas. Cada `scan()` retorna em microssegundos.

**LCD via I2C (PCF8574).** Em paralelo, o LCD ocuparia 6+ GPIOs. Pelo I2C, são apenas 2 (SDA/SCL) e ainda sobra barramento para futuros sensores. Por isso `wokwi-lcd1602` foi configurado com `pins: i2c` e usei os drivers consagrados `lcd_api.py` + `i2c_lcd.py` em vez de reimplementar protocolo.

**Pinout escolhido.** Todas as linhas/colunas do keypad ficam na fileira esquerda do ESP32 (GPIO 12-14, 25-27, 32-33), enquanto LCD, servo, LEDs e buzzer ficam à direita (GPIO 5, 18, 19, 21, 22, 23). Isso reduz o cruzamento de fios no diagrama.

**CI/CD com fluxo `develop` → `main`.** Um único workflow ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)) cobre os dois branches em build + simulação Wokwi (consistência de ambiente), mas o job `release` só roda em push para `main`: gera tag automática (`vYYYY.MM.DD-shortsha`) e publica `fs.bin` como artifact e GitHub Release. Pull requests para `develop` ou `main` rodam só o build/test, sem release.

---

## 5️⃣ Resultados Obtidos

### Comportamento na simulação Wokwi

- **Boot:** o serial mostra `Cofre iniciado`, o LCD exibe `Cofre Trancado / Digite a senha:` e o LED vermelho fica aceso.
- **Digitação:** ao pressionar dígitos, o LCD mostra `Senha:` na linha 1 e uma máscara `*___`, `**__`, `***_`, `****` na linha 2.
- **Acerto (`1234#`):** servo gira para 90°, LED verde acende, beep curto agudo, LCD `Cofre Aberto / Bem-vindo!`. Após 5 s, religa automaticamente.
- **Erro (`9999#`):** beep grave, LCD `Senha Incorreta / Tentativa N/3`, retorna para tela inicial em 1 s.
- **Cancelamento (`*`):** zera o buffer e volta ao estado inicial a qualquer momento durante a digitação.
- **Bloqueio (3 erros seguidos):** LCD `BLOQUEADO! / Aguarde 10s`, LED vermelho piscando a cada 250 ms com buzzer intermitente. Teclas são ignoradas. Após 10 s, contador zera e cofre volta a aceitar tentativas.

### Resultado no GitHub Actions

- Push em `develop` ou `main` (ou PR): build da imagem Docker → geração do `fs.bin` → simulação Wokwi com `expect_text: 'Cofre iniciado'` → upload do `fs.bin` como artifact.
- Push em `main`: além disso, cria a tag automática e publica o release com o `fs.bin`.

### Atendimento aos requisitos do desafio

- Estrutura mínima (`src/`, `wokwi.toml`, `diagram.json`, `README.md`) presente.
- Simulação Wokwi roda sem erro.
- Pipeline GitHub Actions verde nos dois branches.
- README como relatório técnico completo.

---

## 6️⃣ Comentários Adicionais

### Limitações conhecidas

- **PIN em texto claro** no `main.py`. Em produção, viria de NVS protegido (`esp32.NVS`) ou de um secure element.
- **Sem persistência de tentativas:** reset zera o contador. Um atacante real poderia usar power-cycling como bypass — solução seria salvar o contador no NVS.
- **Comparação não constant-time:** `self._buffer == self._pin_correto` vaza tempo. Para um cofre de baixo risco é aceitável; em alto risco usaria `hmac.compare_digest`.
- **Sem watchdog:** uma exceção não tratada deixa o cofre travado. `machine.WDT` resolveria.
- **Servo sem realimentação de posição:** se o motor falhar, o firmware não percebe.

### Melhorias com mais tempo

- Modo "trocar PIN" protegido pelo PIN atual (estado adicional `CHANGE_PIN`).
- Log de tentativas com timestamp em arquivo no LittleFS.
- Sensor PIR para detectar tentativa de violação enquanto trancado.
- Configuração via `boot.py` separando segredos do código de aplicação.

### Aprendizados

- **Disciplina de não-bloqueante:** todo `sleep` longo é uma falha de UX em embarcado.
- **Separar driver de lógica** facilita teste manual e troca de componentes.
- **Conventional Commits + branches `develop`/`main`** deixam clara a fronteira entre "em desenvolvimento" e "pronto para release".

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
