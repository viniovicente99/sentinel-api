# Sentinel API

API para ingestão e gerenciamento de eventos de segurança, com enriquecimento de dados via geolocalização de IP.

## Requisitos

* Docker
* Docker Compose

## Configuração

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd sentinel-api
```

2. Crie o arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=sentinel

DATABASE_URL=postgresql://seu_usuario:sua_senha@db:5432/sentinel
```

Substitua `seu_usuario` e `sua_senha` pelas suas credenciais.

## Execução

Suba os containers com:

```bash
docker-compose up --build
```

A API estará disponível em:

```
http://localhost:8000
```

## Parar o projeto

```bash
docker-compose down
```

## Observações

* O serviço `db` é um container PostgreSQL.
* O serviço `api` é a aplicação FastAPI.
* O nome do host do banco dentro do Docker é `db` (não use localhost).
* O arquivo `.env` não deve ser versionado.

## Estrutura

```
.
├── app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
```

## Endpoints

A documentação interativa está disponível em:

```
http://localhost:8000/docs
```
