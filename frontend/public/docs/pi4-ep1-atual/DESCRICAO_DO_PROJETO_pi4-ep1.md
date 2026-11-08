<!-- markdownlint-disable -->

# Descrição do Projeto — TrAcEs (Inventário de CI/CD e Sistema EP1)

**Projeto:** TrAcEs — Trilha de Acompanhamento Estudantil  
**Entregável:** Entregável Parcial 1 (EP1) — Configuração de Processo de Integração Contínua com GitHub Actions  
**Disciplina:** Projeto Integrado 4  
**Disciplina Integrada:** Integração de Sistemas  
**Instituição:** Universidade Federal do Cariri (UFCA)  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Estudantes:** Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz  
**Data:** 02/11/2026  
**Status do Projeto:** ✅ 100% HOMOLOGADO E INTEGRADO NO GITHUB ACTIONS (Pipeline CI Verde · 79 Testes Pytest Aprovados · Build Vite Homologado · Relatório JUnit XML Persistido · Executor Local `ci_local.py`)

---

## 1. Visão Geral do Sistema e do Pipeline de Integração Contínua

O **TrAcEs (Trilha de Acompanhamento Escolar)** é uma aplicação Web completa desenvolvida para a gestão pedagógica e o estreitamento dos laços entre escolas públicas e famílias na região do Cariri cearense. No **Entregável Parcial 1 (EP1) do Projeto Integrado 4**, em sinergia com a disciplina **Integração de Sistemas**, o foco evolutivo foi a concepção, implementação e homologação de um pipeline profissional e resiliente de **Integração Contínua (CI)** utilizando o ecossistema do **GitHub Actions**.

### 🌟 Pilares Tecnológicos e de Automação

- **Infraestrutura de CI/CD:** GitHub Actions com runners gerenciados `ubuntu-24.04`, controle estrito de concorrência (`concurrency`), cancelamento preventivo de builds obsoletos e princípio de privilégios mínimos (`permissions: contents: read`).
- **Jobs Desacoplados:**
  - `backend-ci`: provisionamento do Python 3.12, cache nativo de dependências (`cache: "pip"` indexado em `backend/requirements.txt`), checagem sintática via `python -m compileall`, execução da suíte de 79 testes no Pytest com isolamento transacional de banco SQLite e exportação/upload do artefato JUnit XML (`reports/pytest-results.xml`).
  - `frontend-ci`: provisionamento do Node.js 22.20.0, cache nativo do NPM indexado em `frontend/package-lock.json`, instalação estrita e determinística com `npm ci`, checagem de tipos TypeScript sem emissão de código (`tsc --noEmit`) e compilação de produção otimizada com Vite 6 (`vite build`).
- **Orquestrador Local de CI:** Script multiplataforma [`scripts/ci_local.py`](../../scripts/ci_local.py) para validação determinística offline das 4 tarefas de CI antes de sincronizar com a nuvem.
- **Componente Extensionista:** Documentação acessível e didática inserida no [`README.md`](../../README.md), democratizando o conceito de CI para a comunidade acadêmica e externa.
- **Camadas de Software:** Clean Architecture em 4 Camadas no Backend (Python 3.12 puro), Single Page Application (React 18 + TypeScript 5 + Tailwind CSS v4) no Frontend e banco relacional embarcado SQLite 3.

---

## 2. Árvore Completa de Diretórios do Workspace (`pi_4_ep_1`)

```text
pi_4_ep_1/
├── .github/                                   # GOVERNANÇA E AUTOMAÇÃO DE CI/CD
│   └── workflows/
│       └── ci.yml                             # Pipeline GitHub Actions (jobs backend-ci e frontend-ci)
│
├── .gitignore                                 # Configuração de arquivos ignorados no versionamento
├── .markdownlint.json                         # Regras de auditoria de formatação e estilo Markdown
├── .markdownlintignore                       # Arquivos isentos de linting (node_modules, etc.)
├── pytest.ini                                 # Configuração unificada do Pytest (pythonpath = backend)
├── README.md                                  # Guia oficial com Badges, Diagrama Mermaid e Componente Extensionista
├── RELATORIO_FINAL_PI4_EP1.md                 # Relatório técnico completo de atendimento aos requisitos do EP1
├── RELATORIO_FINAL_PI4_EP1.docx               # Relatório final convertido em Word (formatação ABNT, fonte Arial)
│
├── backend/                                   # BACKEND CLEAN ARCHITECTURE (PYTHON 3.12 PURO)
│   ├── main.py                                # Ponto de entrada do backend REST / CLI
│   ├── requirements.txt                       # Dependências do backend (pytest, etc.)
│   │
│   ├── scripts/                               # SCRIPTS DE TESTE E VALIDAÇÃO AO VIVO
│   │   ├── run_swagger_live_tests.py          # Relatório interativo de operações Swagger
│   │   ├── test_crud_demonstracao.py          # Demonstração completa das operações CRUD
│   │   ├── test_swagger_api_live.py           # Validador de 100% dos endpoints HTTP ao vivo
│   │   └── test_swagger_db_persistence.py     # Verificador de consistência física no SQLite
│   │
│   ├── src/                                   # CÓDIGO-FONTE DO BACKEND (4 CAMADAS)
│   │   ├── domain/                            # Camada de Domínio & Regras de Negócio Puras
│   │   │   ├── models.py                      # Entidades (Student, Teacher, Parent, etc.) e Enums
│   │   │   └── __init__.py
│   │   ├── application/                       # Camada de Aplicação & Casos de Uso
│   │   │   ├── services.py                    # ServicosDoAluno e ServicosSecretaria
│   │   │   └── __init__.py
│   │   ├── infrastructure/                    # Camada de Infraestrutura e Persistência
│   │   │   ├── database.py                    # DatabaseManager e 7 Repositórios SQL desacoplados
│   │   │   ├── schema.sql                     # DDL SQLite: 12 tabelas físicas e 11 índices
│   │   │   └── __init__.py
│   │   └── presentation/                      # Camada de Apresentação e API REST
│   │       ├── server.py                      # Servidor HTTP multithreaded nativo (18 rotas)
│   │       ├── controllers.py                 # Controladores REST com tratamento de erro
│   │       ├── openapi_spec.py                # Especificação OpenAPI 3.0.3 e Swagger UI Live (/docs)
│   │       ├── serializers.py                 # Serialização customizada para JSON
│   │       └── seed_data.py                   # Carga de dados pedagógicos iniciais
│   │
│   └── tests/                                 # SUÍTE DE TESTES AUTOMATIZADOS (79 TESTES)
│       ├── conftest.py                        # Fixtures do Pytest com isolamento temporário SQLite
│       ├── unit/                              # Testes unitários de domínio e validação (40 testes)
│       │   ├── test_cpf_validation.py         # Algoritmo de validação de CPFs
│       │   ├── test_entities.py               # Invariantes e regras das entidades
│       │   └── test_passing_grade.py          # Regra de aprovação e médias bimestrais
│       └── integration/                       # Testes de integração de contratos e persistência (39 testes)
│           ├── test_api_endpoints.py          # Cobertura dos endpoints REST
│           ├── test_2nd_bimester_launch.py    # Lançamento e recálculo dinâmico
│           ├── test_4_bimesters_launch.py     # Fechamento anual dos 4 bimestres
│           ├── test_integrity.py              # Integridade referencial do SQLite
│           └── test_manual_repositories.py    # CRUD transacional nos repositórios SQL
│
├── frontend/                                  # FRONTEND CLIENTE SPA (REACT 18 + VITE 6 + TS)
│   ├── index.html                             # Entrypoint HTML5 semântico
│   ├── package.json                           # Manifesto de dependências e scripts (typecheck, build)
│   ├── package-lock.json                      # Trava determinística de dependências para o npm ci
│   ├── vite.config.ts                         # Configuração do Vite com proxy reverso e build otimizado
│   ├── default_shadcn_theme.css               # Variáveis de estilo e temas acessíveis
│   ├── src/                                   # Código-fonte React 18 e TypeScript 5
│   │   ├── main.tsx                           # Ponto de montagem React
│   │   ├── app/                               # Telas dinâmicas e componentes acessíveis
│   │   ├── services/                          # Cliente HTTP assíncrono tipado
│   │   ├── types/                             # Contratos estáticos TypeScript da API
│   │   └── styles/                            # Tokens Tailwind e modo Alto Contraste (WCAG 2.1 AA)
│   └── public/                                # Ativos estáticos públicos e imagens vetoriais
│
├── reports/                                   # RELATÓRIOS PERSISTIDOS DE CI
│   └── pytest-results.xml                     # Relatório JUnit XML gerado pelo Pytest
│
├── scripts/                                   # SCRIPTS DE ORQUESTRAÇÃO E AUTOMAÇÃO
│   └── ci_local.py                            # Executor local multiplataforma do pipeline de CI
│
└── docs/                                      # DOCUMENTAÇÃO TÉCNICA E ACADÊMICA DO PROJETO
    ├── assets/
    │   └── ci/                                # Matriz de 13 capturas reais de evidências do CI
    │       ├── 01-actions-workflow-aprovado.png
    │       ├── 02-job-backend-pytest.png
    │       ├── 03-artefato-pytest-results.png
    │       ├── 04-job-frontend-build.png
    │       ├── 05-badge-passing.png
    │       ├── 06-actions-runs-list.png
    │       ├── 07-autoria-commits-equipe.png
    │       ├── 08-divisao-responsabilidades-readme.png
    │       ├── 09-backend-clean-arch-tests.png
    │       ├── 10-backend-swagger-openapi.png
    │       ├── 11-frontend-spa-interface.png
    │       ├── 12-frontend-build-typecheck.png
    │       ├── 13-ci-local-orchestrator.png
    │       └── LEIA-ME-EVIDENCIAS.md          # Catálogo e descrição detalhada das evidências
    └── pi4-ep1-atual/                         # Documentação técnica consolidada do EP1
        ├── EP1_INDICE.md                      # Sumário executivo e guia de navegação
        ├── EP1_README.md                      # Manual completo de CI e execução do software
        ├── EP1_ARQUITETURA.md                 # Arquitetura de software e arquitetura de CI
        ├── DESCRICAO_DO_PROJETO_pi4-ep1.md    # Este inventário técnico e volumetria
        ├── RELATORIO_ATENDIMENTO_REQUISITOS-pi4-ep1.md # Matriz de atendimento do edital
        ├── RELATORIO_MVP_WEB_FUNCIONAL.md     # Relatório de homologação no pipeline de CI
        ├── relatorio_tecnologias_frontend_projeto.md # Tecnologias do Frontend e esteira de CI
        └── relatorio-arquitetura-ep1-v1.txt   # Síntese textual da arquitetura e CI em ASCII
```

---

## 3. Inventário Físico e Volumetria de Código (PI4-EP1)

```text
VOLUMETRIA DO CÓDIGO-FONTE E ARTEFATOS DE CI (EP1):
├── Pipeline GitHub Actions (.github/workflows/ci.yml): ~90 linhas de configuração declarativa
├── Orquestrador Local de CI (scripts/ci_local.py): ~140 linhas de automação multiplataforma
├── Backend Python (backend/src/ e backend/scripts/): ~3.800 linhas de código limpo
├── Frontend TypeScript/React (frontend/src/): ~4.200 linhas de componentes e lógica SPA
├── Suíte de Testes Automatizados (backend/tests/): ~1.850 linhas (79 testes com JUnit XML)
├── Documentação Técnica e Acadêmica (docs/ e raiz): ~3.500 linhas de documentação e relatórios
├── Matriz de Evidências Visuais (docs/assets/ci/): 13 capturas de alta definição (1440x900)
└── Banco de Dados (SQLite 3): 12 tabelas normalizadas, 11 índices de alta performance
```

---

## 4. Conclusão do Inventário

O inventário do repositório comprova que o sistema **TrAcEs (EP1 - PI4 / Integração de Sistemas)** atingiu plena maturidade em seu ciclo de vida. A base de código está plenamente integrada a um fluxo de automação contínua na nuvem, garantindo governança, determinismo e alta confiabilidade para as fases subsequentes da trilha acadêmica.
