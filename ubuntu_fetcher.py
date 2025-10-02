import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Solicita a URL ao usuário
    url = input("Digite a URL da imagem que deseja baixar: ").strip()

    # Diretório onde as imagens serão guardadas
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Faz a requisição da imagem
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Levanta erro se status != 200

        # Extrair nome do arquivo da URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Caso a URL não tenha nome de arquivo
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Caminho final do arquivo
        file_path = os.path.join(save_dir, filename)

        # Salvar em modo binário
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Imagem salva com sucesso em: {file_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ Erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão. Verifique sua internet ou URL.")
    except requests.exceptions.Timeout:
        print("❌ O pedido expirou (timeout).")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    fetch_image()
