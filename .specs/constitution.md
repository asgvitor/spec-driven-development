# Constituição SDD com Speckit

## Princípios Centrais

### I. Stack e Escopo Obrigatórios
O projeto DEVE ser implementado em Python 3.11 usando FastAPI. O escopo DEVE ser
uma API HTTP para gestão de tarefas pessoais. Mudanças de stack, adição de
frontend dedicado ou troca de framework backend não são permitidas sem emenda
formal desta constituição.

### II. Dados Somente em Memória
Os dados DEVEM ser mantidos exclusivamente em memória de processo (ex.: listas e
dicionários Python). Reiniciar a aplicação DEVE limpar o estado. Persistência em
arquivo, cache externo ou qualquer camada de armazenamento permanente não é
permitida nesta fase.

### III. Sem Autenticação e Sem Banco de Dados
O projeto DEVE permanecer sem autenticação, autorização, gestão de sessões e sem
dependência de banco de dados. Bibliotecas de ORM, migrações e infraestrutura de
credenciais NÃO DEVEM ser introduzidas.

### IV. Contrato HTTP Correto e Consistente
Cada endpoint DEVE retornar status HTTP coerente com o resultado da operação,
incluindo respostas de erro previsíveis e payloads claros. Como regra geral:
sucesso de leitura/atualização com 200, criação com 201, exclusão sem corpo com
204, entrada inválida com 400/422 e recurso inexistente com 404.

### V. Código Didático para Iniciantes
O código DEVE priorizar legibilidade: nomes explícitos, funções curtas,
responsabilidades simples e organização direta. Abstrações desnecessárias,
metaprogramação e padrões avançados sem ganho claro DEVEM ser evitados. Tipagem e
comentários curtos são incentivados quando melhorarem entendimento.

## Restrições Técnicas e de Qualidade

- Dependências DEVEM ser mínimas e justificadas.
- Modelos de entrada e saída DEVEM usar validação explícita do FastAPI/Pydantic.
- Erros de regra de negócio DEVEM ser tratados de forma uniforme e previsível.
- O projeto DEVERIA manter cobertura de testes para fluxos principais e casos de
  erro esperados.

## Fluxo de Desenvolvimento e Revisão

- Toda alteração de comportamento DEVE manter alinhamento com
  .specs/spec.yaml, .specs/requirements.md e .specs/design.md.
- Implementação DEVE seguir ordem de tarefas em .specs/tasks.md, com entregas
  incrementais e verificáveis.
- Revisões de código DEVEM checar conformidade com esta constituição,
  especialmente escopo técnico, simplicidade e contrato HTTP.

## Governança

Esta constituição prevalece sobre preferências locais e exemplos temporários.
Emendas DEVEM registrar motivação, impacto e versão semântica resultante.

Política de versão:
- MAJOR para mudanças incompatíveis de princípios ou remoção de garantias.
- MINOR para novos princípios, seções ou expansão normativa material.
- PATCH para clarificações editoriais sem alterar o significado normativo.

Conformidade DEVE ser revisada em cada PR e revalidada ao final de cada etapa
do fluxo Speckit.

**Versão**: 1.0.0 | **Ratificada em**: 2026-04-20 | **Última Emenda**: 2026-04-20
