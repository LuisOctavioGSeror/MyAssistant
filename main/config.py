from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Exemplo de como acessar uma variável de ambiente
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
coinmarketcap_api = os.getenv("COINMARKETCAP_API")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
# Se necessário, configurar outras partes do sistema aqui
# ...

