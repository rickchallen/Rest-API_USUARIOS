from fastapi import APIRouter, HTTPException, Query
from service.user_service import UserService
from repository.user_repository import UserRepository
from models.user_model import UserListResponse, User, ErrorResponse
from core.logging import log
from typing import Optional

user_repo = UserRepository()
user_service = UserService(user_repo)

router = APIRouter()

@router.get(
    "/users",
    response_model=UserListResponse,
    responses={400: {"model": ErrorResponse}}
)
def list_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    q: Optional[str] = Query(None),
    role: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None)
):
    """
    Lista usuários com paginação e filtros.
    """
    log.info(f"GET /users - Parâmetros de consulta recebidos.")
    return user_service.get_users(
        page=page,
        page_size=page_size,
        q=q,
        role=role,
        is_active=is_active
    )

@router.get(
    "/users/{user_id}",
    response_model=User,
    responses={
        404: {"model": ErrorResponse},
    }
)
def get_user(user_id: int):
    """
    Obtém um usuário por ID.
    """
    log.info(f"GET /users/{user_id}")
    user = user_service.get_user_by_id(user_id)
    if not user:
        log.warning(f"Usuário com ID {user_id} não encontrado.")
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    
    log.info(f"Usuário com ID {user_id} encontrado.")
    return user