
-----

### **README.md**

# API de Usuários

Este projeto implementa a segunda questão do desafio de Back-end, conforme as instruções do arquivo `desafio backend junior.pdf`. Trata-se de uma API de leitura de usuários construída em Python com o framework FastAPI.

A API utiliza o arquivo `mock-users.json` como fonte de dados e segue as boas práticas de organização em camadas (`controllers`, `services`, `repositories`, `models`, `core`) e padrões de resposta (paginação, envelope de erro).

## Como Executar

Siga os passos abaixo para configurar e rodar a aplicação localmente.

### Pré-requisitos

  * Python 3.8+
  * `pip` (gerenciador de pacotes do Python)

### 1\. Instalar Dependências

No terminal, navegue até a pasta raiz do projeto (onde estão as pastas `src`, `mock-users.json`, `.env`, `requirements.txt`, etc.) e execute:

```bash
pip install -r requirements.txt
```

### 2\. Rodar o Servidor

Execute a aplicação com o Uvicorn. O parâmetro `--reload` reinicia o servidor automaticamente a cada alteração no código. É **essencial** usar `--host 0.0.0.0` para permitir que outros dispositivos na sua rede acessem a API.

```bash
uvicorn src.main:app --host 0.0.0.0 --reload
```

Após a execução, o terminal deverá exibir uma mensagem similar a:
`INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`

A API estará acessível em:

  * `http://localhost:8000` (para acessar da própria máquina)
  * `http://127.0.0.1:8000` (para acessar da própria máquina)
  * `http://SEU_IP_LOCAL:8000` (para acessar de outros dispositivos na mesma rede, como seu celular). Substitua `SEU_IP_LOCAL` pelo IP da sua máquina (ex: `http://192.168.1.100:8000`).

## Exemplos de Teste

Você pode testar os endpoints da API de duas formas: usando a documentação interativa do Swagger UI ou através da ferramenta de linha de comando `curl`.

### Testando pela Documentação do Swagger UI

1.  Abra seu navegador e acesse: `http://localhost:8000/docs`
2.  Clique nos endpoints (`GET /users` e `GET /users/{id}`) para expandir.
3.  Clique em **"Try it out"**.
4.  Preencha os parâmetros de consulta (`q`, `role`, `is_active`, `page`, `page_size`) ou o `user_id` conforme necessário.
5.  Clique em **"Execute"** para ver a resposta.

### Testando com `curl` (Linha de Comando)

**Observação:** Para estes exemplos, `localhost` e `127.0.0.1` funcionam para testes na própria máquina. Para testes do celular, substitua por `SEU_IP_LOCAL:8000`.

#### Listar todos os usuários

Endpoint `GET /users` com paginação padrão (`page=1`, `page_size=10`) e sem filtros.

```bash
# Acesso local
curl "http://localhost:8000/users"

# Acesso via IP da máquina (se estiver testando de outro dispositivo na rede)
# curl "http://SEU_IP_LOCAL:8000/users"
```

#### Buscar usuários por nome ou e-mail

Endpoint `GET /users` com o filtro de busca `q`. A busca é feita por nome e e-mail.

```bash
# Acesso local
curl "http://localhost:8000/users?q=Felipe"
curl "http://localhost:8000/users?q=contoso.dev"

# Acesso via IP da máquina
# curl "http://SEU_IP_LOCAL:8000/users?q=Felipe"
```

#### Listar usuários com filtros e paginação

Combine os filtros `role` e `is_active` com os parâmetros de paginação `page` e `page_size`.

```bash
# Acesso local
curl "http://localhost:8000/users?role=manager"
curl "http://localhost:8000/users?is_active=true"
curl "http://localhost:8000/users?role=admin&is_active=false"
curl "http://localhost:8000/users?page=2&page_size=5"

# Acesso via IP da máquina
# curl "http://SEU_IP_LOCAL:8000/users?role=manager"
```

#### Obter um usuário por ID

Endpoint `GET /users/{id}` para buscar um único usuário pelo seu ID.

```bash
# Acesso local
curl "http://localhost:8000/users/2"

# Acesso via IP da máquina
# curl "http://SEU_IP_LOCAL:8000/users/2"
```

Se o usuário não for encontrado, a API retornará o código de status HTTP `404` com um corpo de erro padronizado.

-----