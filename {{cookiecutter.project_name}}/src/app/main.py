import atexit
import os

from dotenv import load_dotenv
from openai import AzureOpenAI

from app import logger
from app.logging_config import setup_logging


def main():
    load_dotenv()

    setup_logging(config_file_path="resources/logging_config.json")

    logger.info("Cargando variables de entorno")
    endpoint = os.getenv(
        "AZURE_OPENAI_API_ENDPOINT",
        "https://ailabs-xiromed-east-us2-dev.openai.azure.com/",
    )
    deployment = os.getenv("AZURE_OPENAI_API_DEPLOYMENT_NAME", "gpt-4o-mini")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")

    logger.info(f"Inicializando cliente de Azure OpenAI con endpoint: {endpoint} y deployment: {deployment}")
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version=api_version,
    )

    # Registrar una función para cerrar el cliente antes de que termine el programa
    def close_client():
        logger.info("Cerrando el cliente de OpenAI")
        client.close()

    atexit.register(close_client)

    logger.info("Preparando el prompt para el chat")
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI assistant that helps people find information.",
                }
            ],
        }
    ]

    messages = chat_prompt

    logger.info(
        "Enviando solicitud a la API de Azure OpenAI",
        extra={"chat_prompt": chat_prompt},
    )
    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=messages,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False,
        )
        logger.info("Respuesta recibida correctamente")
    except Exception as e:
        logger.error(f"Error al llamar a la API de Azure OpenAI: {str(e)}")
        raise

    client.close()

    return completion


if __name__ == "__main__":
    main()
