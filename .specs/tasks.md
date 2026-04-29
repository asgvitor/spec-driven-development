# Tasks - Task Manager API

Gerado com base em `.specs/design.md` e clarificações de requisitos (`.specs/requirements.md`).

## Estrutura de Implementação

**Fases:**
1. **Setup** - Estrutura do projeto
2. **Foundational** - Infraestrutura compartilhada (modelos, storage)
3. **Features** - Por priority (F01→F05)
4. **Polish** - Testes e validações

---

## Phase 1: Setup

### Objetivo
Estruturar projeto FastAPI com estrutura base pronta para features.

**Critério de Pronto:** Projeto inicializado, dependências instaladas, servidor executa sem erro.

- [ ] T001 Criar estrutura de diretórios: app/, .specs/, com __init__.py em app/
- [ ] T002 Criar app/main.py com FastAPI app instance
- [ ] T003 [P] Instalar dependências: FastAPI, Uvicorn, Pydantic

---

## Phase 2: Foundational (Blocking Prerequisites)

### Objetivo
Estruturas e componentes compartilhados por todas as features.

**Critério de Pronto:** Modelos e storage disponíveis para todos os endpoints.

- [ ] T004 [P] Criar app/models.py com Pydantic: TaskCreate, TaskUpdate, Task
- [ ] T005 [P] Criar app/storage.py com storage em memória (tasks_db list)
- [ ] T006 Implementar ValidationError handler centralizando {"error": "msg", "code": "CODE"} em app/main.py

---

## Phase 3: Feature F01 - Health Check (must-have)

### User Story
Como usuário, posso validar saúde da API com GET / → HTTP 200, {"status": "ok"}.

**Critério de Pronto:** Endpoint GET / responde conforme spec. Testável isoladamente.

- [ ] T007 [US-F01] Implementar GET / em app/main.py retornando {"status": "ok"}, HTTP 200

---

## Phase 4: Feature F02 - Criar Tarefa (must-have)

### User Story
Como usuário, posso criar tarefa via POST /tasks com title obrigatório (não vazio).

**Critério de Pronto:** POST cria com UUID, title validado, status=pending, created_at. Trata 400 em validações.

- [ ] T008 [US-F02] Implementar POST /tasks com validação: title required, non-empty → 400
- [ ] T009 [P] [US-F02] Validar description opcional (null permitido)
- [ ] T010 [US-F02] Gerar UUID para cada tarefa criada em app/storage.py
- [ ] T011 [US-F02] Retornar Task completo (id, title, description, status=pending, created_at) em POST /tasks

---

## Phase 5: Feature F03 - Listar Tarefas (must-have)

### User Story
Como usuário, posso listar todas as tarefas com GET /tasks → retorna array, HTTP 200.

**Critério de Pronto:** GET /tasks retorna [] (vazio) ou [Task, ...]. Testável com storage vazio e com dados.

- [ ] T012 [US-F03] Implementar GET /tasks retornando array Tasks (vazio se nenhuma)

---

## Phase 6: Feature F04 - Atualizar Status (should-have)

### User Story
Como usuário, posso atualizar status (pending→in_progress→done) via PATCH /tasks/{id}.

**Critério de Pronto:** PATCH valida status enum, retorna 200 ou 404. Status imutável em POST.

- [ ] T013 [US-F04] Implementar PATCH /tasks/{id} com validação: status ∈ {pending, in_progress, done}
- [ ] T014 [P] [US-F04] Retornar 404 se ID não encontrado
- [ ] T015 [US-F04] Validar que POST não permite override de status (sempre pending)

---

## Phase 7: Feature F05 - Remover Tarefa (could-have)

### User Story
Como usuário, posso deletar tarefa via DELETE /tasks/{id} → 204 (encontrada) ou 404 (não existe).

**Critério de Pronto:** DELETE remove tarefa, retorna 204/404. Comportamento idempotente claro.

- [ ] T016 [P] [US-F05] Implementar DELETE /tasks/{id} com lógica: encontrada → remover, retornar 204
- [ ] T017 [US-F05] DELETE não encontrada: retornar 404 com {"error": "Task not found", "code": "NOT_FOUND"}

---

## Phase 8: Polish & Cross-Cutting

### Objetivo
Qualidade, testes e documentação.

**Critério de Pronto:** Testes passam, documentação atualizada.

- [ ] T018 [P] Criar app/test_main.py com testes unitários para todos endpoints
- [ ] T019 [P] Testar casos de borda: title vazio, ID inválido, status inválido
- [ ] T020 Validar mensagens de erro followem formato {"error": "...", "code": "..."} em todos endpoints
- [ ] T021 Documentar estrutura em README.md com exemplos cURL para todos endpoints

---

## Dependências de Completude (Ordem de Execução)

```
Phase 1: Setup (independente)
  ↓
Phase 2: Foundational (blocking T3-T7)
  ↓
Phase 3-7: Features (parallelizáveis por feature)
  ├─ T007 (F01) - independente
  ├─ T008-T011 (F02) - após T004, T005, T006
  ├─ T012 (F03) - após T004, T005
  ├─ T013-T015 (F04) - após T004, T005, T006
  ├─ T016-T017 (F05) - após T004, T005, T006
  ↓
Phase 8: Polish (após todas features)
```

## Parallelização por Feature

**Iteração 1 (MVP F01-F03 must-have):** T001-T012 sequencialmente
- Setup → Foundational → F01, F02, F03 (6 dias típicos)

**Iteração 2 (F04 should-have):** T013-T015 após Iteração 1
- F04 (2 dias)

**Iteração 3 (F05 could-have):** T016-T017 opcional
- F05 (1 dia)

**Iteração Final (Polish):** T018-T021 após todas features
- Testes e docs (2 dias)

---

## Convenção de Status

- [ ] não iniciado
- [~] em andamento
- [x] concluído

## Critérios Gerais de Pronto

- [ ] Código executa sem erro no Codespace
- [ ] Critérios de aceite por task atendidos
- [ ] Teste manual com cURL valida contract
- [ ] Task marcada concluída (checkbox)
