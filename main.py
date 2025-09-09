from fastapi import FastAPI
from controller.controller import router as users_router
from core.config import settings
from core.logging import log

log.info("Iniciando a aplicação FastAPI...")

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="Uma API simples para leitura de usuários.",
)

app.include_router(users_router)

# Este bloco é opcional, mas útil para rodar a aplicação localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)