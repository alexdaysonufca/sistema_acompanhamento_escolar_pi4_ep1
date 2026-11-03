<!-- markdownlint-disable -->

# Matriz Completa de Evidências Visuais — EP1 (PI4 / Integração de Sistemas)

Este diretório concentra o conjunto integral de capturas de tela e evidências que comprovam o funcionamento do pipeline de CI, a integridade técnica do sistema e a **atuação detalhada de cada membro da equipe discente** (Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz).

---

## 1. Evidências do Pipeline de CI no GitHub Actions

| Arquivo | Descrição da Evidência | Status |
| :--- | :--- | :---: |
| [`01-actions-workflow-aprovado.png`](01-actions-workflow-aprovado.png) | Visão geral da workflow `CI - TrAcEs` aprovada com status verde (*success*) e os dois jobs concluídos (`backend-ci` e `frontend-ci`). | ✅ |
| [`02-job-backend-pytest.png`](02-job-backend-pytest.png) | Execução detalhada do job `backend-ci` no GitHub Actions: checagem de sintaxe (`compileall`) e execução dos 79 testes automatizados com Pytest. | ✅ |
| [`03-artefato-pytest-results.png`](03-artefato-pytest-results.png) | Seção de artefatos da execução (*Run Summary*) confirmando a persistência e publicação do relatório `pytest-results-report` (`pytest-results.xml`). | ✅ |
| [`04-job-frontend-build.png`](04-job-frontend-build.png) | Execução detalhada do job `frontend-ci`: instalação limpa (`npm ci`), validação de tipos estáticos (`tsc --noEmit`) e build de produção com Vite. | ✅ |
| [`05-badge-passing.png`](05-badge-passing.png) | Badge dinâmico oficial do GitHub Actions renderizado como verde (`passing`) no topo do README do repositório público. | ✅ |
| [`06-actions-runs-list.png`](06-actions-runs-list.png) | Histórico de execuções do workflow no GitHub Actions atestando a estabilidade e aprovação contínua na branch `main`. | ✅ |

---

## 2. Evidências de Atuação dos Membros da Equipe e Autoria

| Arquivo | Descrição da Evidência | Responsável Principal | Status |
| :--- | :--- | :--- | :---: |
| [`07-autoria-commits-equipe.png`](07-autoria-commits-equipe.png) | Histórico de commits no GitHub demonstrando a colaboração e autoria distribuída entre Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz com commits semânticos padronizados. | Dupla | ✅ |
| [`08-divisao-responsabilidades-readme.png`](08-divisao-responsabilidades-readme.png) | Seção 8 do `README.md` renderizada no repositório GitHub com a tabela oficial de divisão de responsabilidades, arquitetura e atribuição de papéis. | Dupla | ✅ |
| [`09-backend-clean-arch-tests.png`](09-backend-clean-arch-tests.png) | Execução local da suíte completa de 79 testes unitários e de integração no Pytest com isolamento transacional SQLite e geração de XML. | Antonio Alex Dayson Tomaz | ✅ |
| [`10-backend-swagger-openapi.png`](10-backend-swagger-openapi.png) | Documentação interativa Swagger UI & OpenAPI 3.0.3 servida ao vivo pelo servidor HTTP multithreaded nativo em Python puro (`/docs`). | Antonio Alex Dayson Tomaz | ✅ |
| [`11-frontend-spa-interface.png`](11-frontend-spa-interface.png) | Interface gráfica em execução do SPA TrAcEs (React 18, Tailwind CSS v4, Vite) com contraste WCAG 2.1 AA (7:1) e componentes dinâmicos de acompanhamento escolar. | Maria Alexsandra Tomaz | ✅ |
| [`12-frontend-build-typecheck.png`](12-frontend-build-typecheck.png) | Verificação de tipos estáticos via TypeScript (`tsc --noEmit`) e compilação de produção com empacotamento otimizado de 3.682 módulos sem erros. | Maria Alexsandra Tomaz | ✅ |
| [`13-ci-local-orchestrator.png`](13-ci-local-orchestrator.png) | Execução do orquestrador local multiplataforma `scripts/ci_local.py`, demonstrando a reprodução das 4 etapas de CI antes do push. | Dupla | ✅ |

---

Todas as evidências encontram-se referenciadas nas Seções 7.4 e 8 do [`RELATORIO_FINAL_PI4_EP1.md`](../../RELATORIO_FINAL_PI4_EP1.md).
