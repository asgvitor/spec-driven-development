# Hands-on: Spec-Driven Development com GitHub Copilot

Este guia concentra apenas a execução prática do hands-on. A preparação do ambiente, criação do repositório e abertura no Codespaces ficam no [README.md](../README.md) da raiz.

## Preparar o ambiente

No terminal do Codespace, valide as ferramentas necessárias:

```bash
python --version
specify --help
```

Em seguida, inicialize o Spec Kit e a integração com o Copilot:

```bash
specify init . --script sh
specify integration install copilot
```

Esses comandos habilitam os comandos `/speckit.*` no Copilot Chat.
Durante essa etapa, é esperado que sejam criados artefatos como `.specify/`
(local) e `.github/` (prompts e agentes do Speckit).

## Objetivo do exercício

Neste hands-on, você vai usar artefatos de especificação como contexto direto para o GitHub Copilot. O foco não é produzir muito código, e sim mostrar como SDD melhora clareza, consistência e validação ao longo do desenvolvimento.

Ao final do exercício, você terá:

- refinado requisitos com apoio da IA;
- organizado a implementação em tasks pequenas e rastreáveis;
- implementado uma API simples em FastAPI guiada por spec;
- validado o código contra os artefatos definidos anteriormente.

## Fonte de verdade do exercício

Os arquivos em [.specs](../.specs/) são a base do hands-on:

- [../.specs/spec.yaml](../.specs/spec.yaml): escopo e proposta do sistema.
- [../.specs/requirements.md](../.specs/requirements.md): requisitos funcionais e critérios de aceite.
- [../.specs/design.md](../.specs/design.md): design técnico da solução.
- [../.specs/tasks.md](../.specs/tasks.md): ordem de execução da implementação.

O código da aplicação é criado em [../app/main.py](../app/main.py), não dentro desta pasta. A pasta `workshop/` existe apenas para organizar o guia do hands-on.

## Fluxo do hands-on

### 1. Refinar requisitos

Revise [../.specs/requirements.md](../.specs/requirements.md) com base em [../.specs/spec.yaml](../.specs/spec.yaml) para identificar critérios de aceite faltantes, casos de borda e respostas de erro.

Exemplo de prompt:

```text
/speckit.clarify Identifique critérios de aceite faltando em #.specs/requirements.md
e casos de borda para endpoints de tarefas.
```

### 2. Refinar tasks

Revise [../.specs/tasks.md](../.specs/tasks.md) usando [../.specs/design.md](../.specs/design.md) como referência. O objetivo é garantir ordem lógica, boa granularidade e critério de pronto claro.

Exemplo de prompt:

```text
/speckit.tasks Com base em #.specs/design.md, quebre em tasks pequenas,
com critério de pronto e ordem de implementação.
```

### 3. Implementar a solução

Implemente as tasks usando [../.specs/design.md](../.specs/design.md) e [../.specs/tasks.md](../.specs/tasks.md) como fonte de verdade. O arquivo-alvo é [../app/main.py](../app/main.py).

Exemplo de prompt:

```text
/speckit.implement Implemente a próxima task pendente em #.specs/tasks.md
usando #.specs/design.md como fonte de verdade.
```

Exemplos de tarefas práticas:

- Criar `app/main.py` com aplicação FastAPI e health check.
- Criar modelos Pydantic com base no design.
- Implementar armazenamento em memória.
- Implementar endpoints `POST /tasks`, `GET /tasks`, `PATCH /tasks/{id}` e `DELETE /tasks/{id}`.

### 4. Validar a aderência à spec

Revise [../app/main.py](../app/main.py) comparando com [../.specs/requirements.md](../.specs/requirements.md) e [../.specs/design.md](../.specs/design.md).

Exemplo de prompt:

```text
@workspace A implementação em #app/main.py corresponde ao design em #.specs/design.md?
Liste divergências objetivas.
```

Você também pode pedir uma revisão contra as tasks:

```text
@workspace Compare #.specs/tasks.md com #app/main.py e liste quais tasks ainda estão pendentes.
```

## Checkpoints sugeridos

- Os requisitos estão claros o suficiente para duas pessoas implementarem a mesma solução.
- As tasks seguem uma ordem que reduz retrabalho.
- O código em [../app/main.py](../app/main.py) reflete o design, não decisões improvisadas.
- A validação final mostra aderência entre requisitos, design, tasks e implementação.

## Material de apoio

- [../README.md](../README.md)