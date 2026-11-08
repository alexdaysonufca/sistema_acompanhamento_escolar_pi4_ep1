<!-- markdownlint-disable -->

# Relatório de Atendimento aos Requisitos — TrAcEs (PI4 - EP1)

**Projeto:** TrAcEs — Trilha de Acompanhamento Estudantil  
**Entregável:** Entregável Parcial 1 (EP1) — Configuração de Processo de Integração Contínua com GitHub Actions  
**Disciplina:** Projeto Integrado 4  
**Disciplina Integrada:** Integração de Sistemas  
**Instituição:** Universidade Federal do Cariri (UFCA)  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Estudantes:** Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz  
**Data:** 02/11/2026  
**Status de Atendimento:** ✅ 100% DOS REQUISITOS ATENDIDOS E COMPROVADOS (Pipeline CI Verde no GitHub Actions · 79 Testes Pytest Aprovados · Build Vite 100% · Relatório JUnit XML Persistido · 13 Evidências Reais)

---

## 1. Introdução e Compreensão do Escopo do EP1

A equipe discente compreendeu que o **Entregável Parcial 1 (EP1)** da disciplina **Projeto Integrado 4**, em integração com **Integração de Sistemas**, marca a transição da etapa de desenvolvimento e prototipagem isolada para a consolidação de práticas profissionais de **DevOps** e **Integração Contínua (CI - *Continuous Integration*)**.

O objetivo central foi implementar um fluxo automatizado e auditável na nuvem através do **GitHub Actions**, capaz de inspecionar a integridade sintática, executar a suíte de testes de backend com isolamento de banco de dados, verificar estaticamente os tipos TypeScript do frontend e validar o empacotamento para produção a cada nova alteração enviada ao repositório (`push` ou `pull_request`).

---

## 2. Matriz de Rastreabilidade e Atendimento aos Requisitos do EP1

A tabela a seguir demonstra a correspondência biunívoca entre os requisitos exigidos no edital do EP1 e a implementação realizada no projeto TrAcEs:

| Requisito do EP1 | Especificação do Edital | Como Foi Atendido no TrAcEs | Evidências no Repositório | Status |
| :--- | :--- | :--- | :--- | :---: |
| **REQ-01: Workflow YAML Funcional** | Configuração do arquivo de workflow `.yml` funcional no diretório `.github/workflows/`. | Criação do arquivo [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) parametrizado com triggers para `main`/`master`, cancelamento de concorrência, runners `ubuntu-24.04` e jobs desacoplados. | Arquivo `.github/workflows/ci.yml` e print [`01-actions-workflow-aprovado.png`](../assets/ci/01-actions-workflow-aprovado.png) | ✅ Atendido |
| **REQ-02: Tarefas Automatizadas** | Ao menos uma tarefa automatizada (build, lint ou teste automatizado). | Implementação de **quatro tarefas complementares**: (1) verificação sintática Python com `compileall`; (2) suíte de 79 testes do backend com Pytest, isolamento SQLite e relatório JUnit XML; (3) verificação de tipos do frontend com `tsc --noEmit`; (4) instalação limpa (`npm ci`) e compilação de produção com Vite (`npm run build`). | Logs dos jobs `backend-ci` e `frontend-ci` e prints [`02-job-backend-pytest.png`](../assets/ci/02-job-backend-pytest.png) e [`04-job-frontend-build.png`](../assets/ci/04-job-frontend-build.png) | ✅ Atendido |
| **REQ-03: README Explicativo de CI** | README com instruções detalhadas sobre a configuração e o objetivo do CI. | Atualização do [`README.md`](../../README.md) principal com badge dinâmico do workflow, diagrama Mermaid do pipeline, guia de execução local e justificativas técnicas. | Seção 1 do `README.md` e print [`05-badge-passing.png`](../assets/ci/05-badge-passing.png) | ✅ Atendido |
| **REQ-04: Componente Extensionista** | Seção explicando o que é CI e por que ela é importante para quem está aprendendo a programar. | Inclusão da Seção 2 no `README.md` utilizando a metáfora didática da "esteira automatizada de controle de qualidade", em linguagem acessível para discentes e comunidade externa. | Seção 2 do `README.md` (`[Componente Extensionista]`) | ✅ Atendido |
| **REQ-05: Demonstração e Evidências** | Demonstrar o GitHub Actions funcionando com evidências visuais e registros reais. | Publicação do pipeline no repositório remoto [`alexdaysonufca/sistema_acompanhamento_escolar_pi4_ep1`](https://github.com/alexdaysonufca/sistema_acompanhamento_escolar_pi4_ep1) (Run ID `41567075098`) e catalogação de 13 evidências em alta resolução. | Diretório [`docs/assets/ci/`](../assets/ci/) com 13 capturas e [`LEIA-ME-EVIDENCIAS.md`](../assets/ci/LEIA-ME-EVIDENCIAS.md) | ✅ Atendido |
| **REQ-06: Governança e Autoria da Equipe** | Divisão transparente de responsabilidades, histórico de commits e reflexão individual. | Divisão de tarefas entre Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz, commits semânticos alternados no Git, avaliação reflexiva e declaração de uso transparente de IA (Gemini 3.8 Flash). | Seção 8 do [`RELATORIO_FINAL_PI4_EP1.md`](../../RELATORIO_FINAL_PI4_EP1.md) e prints [`07-autoria-commits-equipe.png`](../assets/ci/07-autoria-commits-equipe.png) e [`08-divisao-responsabilidades-readme.png`](../assets/ci/08-divisao-responsabilidades-readme.png) | ✅ Atendido |

---

## 3. Detalhamento Técnico das Evidências de Atendimento

### 3.1 Arquitetura do Workflow Declarativo (REQ-01)
- O arquivo `.github/workflows/ci.yml` adota práticas de segurança recomendadas pela OpenSSF:
  - `permissions: contents: read`: impede permissões de escrita indevidas em tokens de CI.
  - `concurrency`: grupo parametrizado por branch com `cancel-in-progress: true`, poupando minutos de execução na nuvem.
  - `timeout-minutes: 15`: previne travamentos silenciosos de jobs.

### 3.2 Automação de Testes e Compilação (REQ-02)
- **Backend:**
  - Checagem sintática preliminar via `python -m compileall -q backend/src backend/main.py`.
  - Execução dos 79 testes unitários e de integração no Pytest com 100% de sucesso em ~4 segundos.
  - Preservação do banco de dados físico de produção através do uso de fixtures com `tmp_path_factory.mktemp`.
  - Persistência estruturada do relatório JUnit XML (`reports/pytest-results.xml`) via `actions/upload-artifact@v6`.
- **Frontend:**
  - Instalação determinística via `npm ci` baseada no lockfile versionado `package-lock.json`.
  - Checagem estática de tipos via `tsc --noEmit` (`npm run typecheck`), prevenindo divergências de contratos de dados em tempo de compilação.
  - Empacotamento de produção com Vite 6 (`npm run build`), transformando 3.682 módulos sem erros de resolução.

### 3.3 Orquestração Local Reproduzível (REQ-03)
- O script [`scripts/ci_local.py`](../../scripts/ci_local.py) replica localmente de forma idêntica os 4 estágios executados na nuvem, permitindo que a dupla discente teste o código offline em ambientes Windows ou Linux antes de realizar qualquer `git push`.

### 3.4 Componente Extensionista e Impacto Social (REQ-04)
- Redação pedagógica que aproxima conceitos avançados de Engenharia de Software da realidade de discentes de períodos iniciais da UFCA e da comunidade externa do Cariri, democratizando o conhecimento sobre automação de software.

### 3.5 Matriz de Evidências Reais (REQ-05)
- Foram geradas e incorporadas 13 capturas de tela reais em alta definição (1440x900) comprovando o status verde na nuvem, execução dos jobs, artefatos XML, histórico de commits e documentação interativa OpenAPI/Swagger UI.

---

## 4. Conclusão da Avaliação

O projeto **TrAcEs** obteve **100% de conformidade** com os requisitos do Entregável Parcial 1 (EP1). A infraestrutura de Integração Contínua implementada garante a sustentabilidade, manutenibilidade e confiabilidade técnica para as entregas parciais subsequentes do Projeto Integrado 4.
