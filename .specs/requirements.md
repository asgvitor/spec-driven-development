# Requirements (baseline mínimo)

Refinar na Etapa 1 com base em .specs/spec.yaml usando /speckit.clarify (opcional: /speckit.checklist).

## Visão Geral

API REST para gerenciamento de tarefas com armazenamento em memória.

## Requisitos Funcionais

- RF01: GET / retorna {"status": "ok"} com HTTP 200.
- RF02: POST /tasks cria tarefa com id, title, description opcional, **status sempre `pending` (imutável na criação)**, e created_at. **Title é obrigatório e não vazio; retorna 400 se ausente ou vazio.**
- RF03: GET /tasks lista tarefas retorna array (vazio se nenhuma existe) com HTTP 200.
- RF04: PATCH /tasks/{id} atualiza status (pending, in_progress, done) com PATCH, retorna 200 ou 404.
- RF05: DELETE /tasks/{id} remove tarefa, retorna 204 se encontrada, retorna 404 se não existe.

## Requisitos Não Funcionais

- RNF01: API responde em JSON.
- RNF02: Erros retornam estrutura `{"error": "message", "code": "ERROR_CODE"}` com HTTP apropriado (400, 404, etc.).
- RNF03: Código legível para fins didáticos.

## Modelo de Dados

- id: string (uuid)
- title: string
- description: string | null
- status: pending | in_progress | done
- created_at: datetime

## Fora do escopo

- Banco de dados
- Autenticação e autorização
- Paginação

## Clarifications

### Session 2026-04-29

- Q: Como validar o campo `title` ao criar uma tarefa? → A: Requer `title` não vazio e retorna `400` se estiver ausente ou vazio.
- Q: Qual formato padrão para respostas de erro? → A: `{"error": "message", "code": "ERROR_CODE"}` com HTTP apropriado (400, 404, etc.).
- Q: Comportamento de DELETE para tarefa não existente? → A: Retorna 404 se tarefa não existe (falha explícita protege contra duplicação).
- Q: Formato de resposta em GET /tasks quando sem tarefas? → A: Retorna `[]` (array vazio) com HTTP 200.
- Q: Status inicial em POST e permissões de mudança? → A: POST cria com status `pending` apenas (imutável na criação); PATCH permite mudanças posteriores.





