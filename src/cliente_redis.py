import os
from dataclasses import dataclass
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ConfiguraciónRedis:
    url: str

def obtener_configuración() -> ConfiguraciónRedis:
    """
    Lee la configuración de Redis desde las variables de entorno.
    Retorna una instancia inmutable de `ConfiguraciónRedis` con la URL.
    Usa `REDIS_URL` o el valor por defecto `redis://localhost:6379/0`.
    """
    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    return ConfiguraciónRedis(url=url)

def obtener_conexion() -> Redis:
    """
    Crea y devuelve una conexión `Redis` usando la configuración.
    Realiza un `ping()` para verificar la conexión antes de retornarla.
    Lanza excepciones de `redis` si no se puede conectar.
    """
    config = obtener_configuración()
    conexion = Redis.from_url(config.url, decode_responses=True)
    conexion.ping()
    return conexion