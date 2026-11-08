<!-- markdownlint-disable -->

# Entregável Parcial 1 (EP1) — Processo de Integração Contínua com GitHub Actions

**Projeto:** TrAcEs — Trilha de Acompanhamento Estudantil  
**Entregável:** Entregável Parcial 1 (EP1) — Configuração de Processo de Integração Contínua com GitHub Actions  
**Disciplina:** Projeto Integrado 4  
**Disciplina Integrada:** Integração de Sistemas  
**Instituição:** Universidade Federal do Cariri (UFCA)  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Estudantes:** Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz  
**Data:** 02/11/2026  
**Status do Projeto:** ✅ 100% CONCLUÍDO E HOMOLOGADO (Pipeline GitHub Actions Verde · 79 Testes Pytest Aprovados · Build Vite 100% · Relatório JUnit XML · Orquestrador Local · Componente Extensionista)

---

## 📦 1. O Que É o Entregável Parcial 1 (EP1) do PI4

O **Entregável Parcial 1 (EP1)** marca a consolidação profissional do projeto **TrAcEs**, integrando os requisitos da disciplina **Projeto Integrado 4** com a disciplina de **Integração de Sistemas**. O objetivo central foi transformar o MVP Web Funcional desenvolvido em etapas anteriores em um ecossistema com esteira de automação contínua de alta confiabilidade, governança de código e determinismo.

### 🌟 Pilares do EP1 Entregue

1. **Pipeline de Integração Contínua (GitHub Actions em `.github/workflows/ci.yml`):**
   - Workflow declarativo parametrizado para triggers em `push`, `pull_request` (branches `main` e `master`) e disparo manual via `workflow_dispatch`.
   - Política rigorosa de concorrência com cancelamento automático de builds obsoletos (`cancel-in-progress: true`).
   - Política de segurança por privilégios mínimos (`permissions: contents: read`).
2. **Automação do Backend (`backend-ci`):**
   - Runner `ubuntu-24.04` provisionado com Python 3.12.
   - Cache inteligente de pacotes gerenciado pelo GitHub (`cache: "pip"` indexado em `backend/requirements.txt`).
   - Validação prévia de sintaxe Python através de compilação de bytecode (`python -m compileall`).
   - Execução integral da suíte de **79 testes automatizados com Pytest** com isolamento transacional de banco de dados SQLite (`tmp_path_factory.mktemp`).
   - Geração e publicação do relatório persistente em formato JUnit XML (`reports/pytest-results.xml`) via `actions/upload-artifact@v6`.
3. **Automação do Frontend (`frontend-ci`):**
   - Runner `ubuntu-24.04` provisionado com Node.js 22.20.0 e cache nativo do NPM indexado em `frontend/package-lock.json`.
   - Instalação estritamente determinística através do comando `npm ci`.
   - Verificação estática rigorosa de contratos de tipo TypeScript sem emissão de arquivos intermediários (`npm run typecheck` via `tsc --noEmit`).
   - Empacotamento e compilação de produção via Vite 6 (`npm run build`), transformando 3.682 módulos sem erros de resolução.
4. **Orquestrador Local de CI ([`scripts/ci_local.py`](../../scripts/ci_local.py)):**
   - Utilitário multiplataforma (Windows/Linux/macOS) que replica exatamente as 4 tarefas de verificação da nuvem no ambiente de desenvolvimento local, garantindo que o desenvolvedor valide o código antes de qualquer `git push`.
5. **Componente Extensionista & Acessibilidade Conceitual:**
   - Seção didática no [`README.md`](../../README.md) voltada à comunidade acadêmica e externa da UFCA, explicando o que é CI através da metáfora acessível da "esteira automatizada de controle de qualidade".
6. **Matriz de 13 Evidências Reais de Execução:**
   - Capturas de tela em alta resolução (1440x900) comprovando o pipeline verde na nuvem, logs de execução dos jobs, upload do artefato XML, badge oficial e a divisão técnica de tarefas entre a dupla.

---

## 🗂️ 2. Catálogo da Documentação Técnica da Pasta (`docs/pi4-ep1-atual/`)

Todos os documentos deste diretório foram auditados e atualizados para refletir o estado de entrega do EP1:

| Documento | Descrição e Finalidade Técnica | Link Direto |
| :--- | :--- | :---: |
| **`EP1_INDICE.md`** | **Este documento:** Sumário executivo, catálogo e guia de navegação do EP1. | [Ver Arquivo](EP1_INDICE.md) |
| **`EP1_README.md`** | Guia mestre de instalação, execução, arquitetura de CI e componente extensionista. | [Ver Arquivo](EP1_README.md) |
| **`EP1_ARQUITETURA.md`** | Especificação técnica arquitetural de software e esteira de CI/CD com diagramas Mermaid. | [Ver Arquivo](EP1_ARQUITETURA.md) |
| **`DESCRICAO_DO_PROJETO_pi4-ep1.md`** | Inventário físico completo, árvore de diretórios e volumetria do EP1. | [Ver Arquivo](DESCRICAO_DO_PROJETO_pi4-ep1.md) |
| **`RELATORIO_ATENDIMENTO_REQUISITOS-pi4-ep1.md`** | Relatório de conformidade integral com os requisitos acadêmicos do EP1 do edital. | [Ver Arquivo](RELATORIO_ATENDIMENTO_REQUISITOS-pi4-ep1.md) |
| **`RELATORIO_MVP_WEB_FUNCIONAL.md`** | Relatório executivo de homologação e validação contínua do sistema TrAcEs. | [Ver Arquivo](RELATORIO_MVP_WEB_FUNCIONAL.md) |
| **`relatorio_tecnologias_frontend_projeto.md`** | Especificação do ecossistema Frontend e sua esteira de validação no CI. | [Ver Arquivo](relatorio_tecnologias_frontend_projeto.md) |
| **`relatorio-arquitetura-ep1-v1.txt`** | Síntese textual da arquitetura e do pipeline de CI em ASCII puro. | [Ver Arquivo](relatorio-arquitetura-ep1-v1.txt) |

---

## 📊 3. Métricas e Estatísticas Consolidadas do EP1

```text
MÉTRICAS DO SISTEMA E DO CI (EP1):
├── Status do Pipeline no GitHub Actions: PASSING (Success)
├── Jobs Paralelos Executados: 2 (backend-ci e frontend-ci)
├── Testes Automatizados no Pytest: 79 testes (100% de aprovação em ~4s)
├── Artefato de Testes Persistido: pytest-results.xml (JUnit XML)
├── Verificação de Tipos TypeScript: 0 erros estáticos (tsc --noEmit)
├── Módulos Transformados no Build Vite: 3.682 módulos
├── Evidências Visuais Reais Catalogadas: 13 capturas em alta resolução
├── Cobertura de Endpoints na API REST: 18 endpoints documentados no Swagger UI
├── Conformidade de Acessibilidade: WCAG 2.1 AA (Contraste 7:1)
└── Auditoria de Formatação Markdown: 0 erros de markdownlint
```
