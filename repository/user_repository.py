import json
from typing import List, Dict
from core.config import settings
from core.logging import log

class UserRepository:
    def __init__(self):
        self.file_path = settings.MOCK_USERS_FILE_PATH

    def get_all_users(self) -> List[Dict]:
        """
        Lê o arquivo mock-users.json e retorna a lista de usuários.
        """
        log.info(f"Tentando ler o arquivo de mock: {self.file_path}")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                log.info(f"Dados do arquivo lidos com sucesso. Total de {len(data)} usuários.")
                return data
        except FileNotFoundError:
            log.error(f"Arquivo não encontrado: {self.file_path}")
            return []
        except json.JSONDecodeError:
            log.error(f"Erro ao decodificar JSON do arquivo: {self.file_path}")
            return []