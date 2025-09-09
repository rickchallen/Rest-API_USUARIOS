from typing import List, Dict, Optional
from repository.user_repository import UserRepository
from core.logging import log

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_users(self, page: int, page_size: int, q: Optional[str], role: Optional[str], is_active: Optional[bool]) -> Dict:
        """
        Retorna uma lista de usuários paginada e filtrada.
        """
        users = self.user_repo.get_all_users()
        log.info(f"Aplicando filtros: q={q}, role={role}, is_active={is_active}")

        if q:
            q_lower = q.lower()
            users = [
                user for user in users
                if q_lower in user.get("name", "").lower() or q_lower in user.get("email", "").lower()
            ]

        if role:
            users = [user for user in users if user.get("role") == role]
        if is_active is not None:
            users = [user for user in users if user.get("is_active") == is_active]

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        paginated_users = users[start_index:end_index]

        return {
            "data": paginated_users,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total": len(users),
                "total_pages": (len(users) + page_size - 1) // page_size
            }
        }

    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        """
        Retorna um único usuário pelo ID.
        """
        log.info(f"Buscando usuário com ID: {user_id}")
        users = self.user_repo.get_all_users()
        for user in users:
            if user.get("id") == user_id:
                return user
        return None