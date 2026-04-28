# Spec-Driven Development com GitHub Copilot

Use especificação como contexto de engenharia para orientar o GitHub Copilot do refinamento de requisitos até a implementação.

## Bem-vindo

- **Para quem é:** desenvolvedores, arquitetos, tech leads, educadores e equipes que querem usar GitHub Copilot com mais previsibilidade e consistência.
- **O que você vai aprender:** como aplicar Spec-Driven Development para reduzir ambiguidade, organizar decisões técnicas e melhorar a qualidade das entregas geradas com IA.
- **O que você vai construir:** uma API simples de gestão de tarefas em FastAPI, implementada a partir de artefatos de especificação já preparados no repositório.
- Pré-requisitos: conta no GitHub, acesso ao GitHub Copilot e noções básicas de leitura de código Python e APIs HTTP.

Neste material, a preparação do ambiente fica na raiz do repositório e a execução do hands-on fica em [workshop/README.md](workshop/README.md).

## O que este repositório contém

Este repositório foi organizado para separar claramente preparação e execução:

- [README.md](README.md): visão geral do projeto, contexto do workshop, pré-requisitos e setup do ambiente.
- [workshop/README.md](workshop/README.md): guia prático do hands-on com o fluxo de SDD.
- [.specs](.specs/): baseline dos artefatos de especificação usados como fonte de verdade.
- [app](app/): código da aplicação criado durante o hands-on.

## Contexto do Hands-on: Por que a spec já existe?

Este repositório simula um projeto em fase de refinamento, não um projeto completamente novo. Os arquivos em [.specs](.specs/) representam o **baseline mínimo** que emergiu de uma fase anterior de descoberta e escopo.

**Neste hands-on, a proposta não é gerar a spec do zero, mas sim:**
1. Refinar requisitos com Copilot (validar critérios de aceite, casos de borda, respostas de erro).
2. Quebrar design em tasks sequenciadas e rastreáveis.
3. Implementar seguindo a especificação como fonte de verdade.
4. Validar que código e spec permanecem alinhados.

## Estado inicial do repositório

Antes de iniciar o hands-on, a estrutura esperada do repositório é:

- [.specs](.specs/) com os artefatos-base (`spec.yaml`, `requirements.md`, `design.md`, `tasks.md`).
- [app/.gitkeep](app/.gitkeep), sem [app/main.py](app/main.py) ainda.
- [workshop/README.md](workshop/README.md).

Após preparar o ambiente e executar o fluxo do guia prático:

- `.specify/` é criada localmente (não versionada).
- `.github/` é criada com prompts e agentes Speckit para os comandos `/speckit.*`.
- [app/main.py](app/main.py) é criado durante a implementação da API em FastAPI.

## Por que usar SDD com GitHub Copilot?

Spec-Driven Development coloca clareza antes de velocidade. Em vez de pedir código diretamente para a IA com contexto incompleto, o fluxo começa com artefatos que deixam explícitos escopo, regras, critérios de aceite, decisões técnicas e sequência de implementação.

Com isso, o GitHub Copilot deixa de operar por inferência ampla e passa a trabalhar sobre um contexto mais restrito e verificável. O resultado prático é:

- Menos ambiguidade na interpretação do problema.
- Mais consistência entre diferentes pessoas gerando código a partir da mesma base.
- Melhor alinhamento entre requisitos, design, tasks e implementação.
- Menos retrabalho durante revisão e validação.
- Maior capacidade de ensinar, demonstrar e repetir o fluxo em equipe.

## Como preparar o ambiente

### 1. Criar uma cópia do repositório

Use este repositório como template ou faça um fork para sua conta, conforme o fluxo adotado na sua turma.

### 2. Abrir no GitHub Codespaces

Depois de criar sua cópia do repositório:

1. Abra o repositório recém-criado na sua conta (ex: `github.com/seu-usuario/spec-driven-development`).
2. Clique em `Code`.
3. Abra a aba `Codespaces`.
4. Crie um novo Codespace.

> **Importante:** evite criar o Codespace imediatamente após gerar o template. Primeiro abra o repositório criado e, só então, inicie o Codespace.

## Próximo passo

Com o Codespace aberto, siga para [workshop/README.md](workshop/README.md) para validar o ambiente e executar o hands-on.

## Recursos

- [Spec Kit Quickstart](https://github.github.com/spec-kit/quickstart.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [GitHub Copilot Chat Documentation](https://docs.github.com/en/copilot/github-copilot-chat)

&copy; 2026 GitHub &bull; [Código de Conduta](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
