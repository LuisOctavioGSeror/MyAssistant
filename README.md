# MyAssistant

Assistente de voz com interface grafica (PyQt5) que:

- reconhece fala pelo microfone;
- envia o texto para um agente LLM (LlamaIndex + Groq/Ollama);
- executa ferramentas como texto-para-fala, notas, e-mail, Spotify, data/hora e cotacoes de cripto.

## Principais recursos

- UI desktop com botao para iniciar reconhecimento de voz;
- visualizador de audio em tempo real;
- agente com ferramentas para automacao de tarefas;
- suporte a variaveis de ambiente via `.env`.

## Estrutura resumida

- `main/`: inicializacao da aplicacao e config;
- `ui/`: janela principal e componentes visuais;
- `recognition_of_speech/`: reconhecimento de fala;
- `agents/`: agentes LLM e ferramentas;
- `features/`: integracoes e funcoes de negocio;
- `speak/`: conversao de texto para audio.

## Requisitos

- Python 3.10+ (recomendado 3.11)
- `pip`
- acesso a internet para servicos externos (Groq, ElevenLabs, Spotify, CoinMarketCap)

## Variaveis de ambiente

1. Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

2. Preencha no `.env`:

```env
ELEVENLABS_API_KEY=
GROQ_API_KEY=
COINMARKETCAP_API=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

## Dados locais esperados

O projeto usa a pasta `data/notes/`.

- Exemplo de lista de e-mails: `data/notes/e-mails.example.txt`
- Crie o arquivo real:

```bash
cp data/notes/e-mails.example.txt data/notes/e-mails.txt
```

## Como rodar localmente

### Ubuntu / Zorin / distros Debian-based

1. Instale dependencias de sistema:

```bash
sudo apt update
sudo apt install -y python3-venv python3-dev portaudio19-dev
```

2. Crie e ative ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale dependencias Python:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Execute:

```bash
python -m main.app
```

### Windows (PowerShell)

1. Crie ambiente virtual:

```powershell
py -m venv .venv
```

2. Ative:

```powershell
.venv\Scripts\Activate.ps1
```

3. Instale dependencias:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Execute:

```powershell
python -m main.app
```

> Se houver erro ao instalar `PyAudio`, instale o Build Tools do Visual Studio C++ e tente novamente.

### macOS

1. Instale Python 3 (se necessario) e PortAudio:

```bash
brew install python portaudio
```

2. Crie e ative ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Execute:

```bash
python -m main.app
```

## Troubleshooting rapido

- **Microfone nao reconhece voz**
  - Verifique permissao do microfone no SO.
  - No Linux, ajuste o indice do microfone em `recognition_of_speech/recognizer.py` (atualmente `sr.Microphone(1)`).

- **Erro com PyAudio**
  - Linux: confirme `portaudio19-dev` instalado.
  - macOS: confirme `portaudio` via Homebrew.
  - Windows: pode exigir Visual C++ Build Tools.

- **Falha em servicos externos**
  - Confirme chaves do `.env`.
  - Teste conexao com internet.

## Observacoes

- Este projeto esta em fase inicial/prototipo.
- Nao suba seu `.env` para o repositorio.
