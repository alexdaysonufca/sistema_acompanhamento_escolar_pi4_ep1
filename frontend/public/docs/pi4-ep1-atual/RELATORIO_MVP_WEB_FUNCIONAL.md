<!-- markdownlint-disable -->

# Relatório de Homologação e Integração Contínua do MVP Web Funcional — TrAcEs (PI4 - EP1)

**Projeto:** TrAcEs — Trilha de Acompanhamento Estudantil  
**Entregável:** Entregável Parcial 1 (EP1) — Homologação do MVP Web em Esteira de Integração Contínua com GitHub Actions  
**Disciplina:** Projeto Integrado 4  
**Disciplina Integrada:** Integração de Sistemas  
**Instituição:** Universidade Federal do Cariri (UFCA)  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Estudantes:** Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz  
**Data:** 02/11/2026  
**Status da Entrega:** ✅ 100% HOMOLOGADO NO GITHUB ACTIONS (Pipeline CI Verde · 79 Testes Pytest Aprovados · Build Vite 100% · Relatório JUnit XML · Clean Architecture 4 Camadas · Monorepo Desacoplado)

---

## 1. Resumo Executivo da Entrega

O **TrAcEs (Trilha de Acompanhamento Estudantil)** é uma plataforma digital integrada de acompanhamento escolar projetada para aproximar famílias e escolas, simplificar a rotina pedagógica dos professores e prevenir a evasão escolar e o baixo rendimento por meio de alertas em tempo real.

No âmbito do **Entregável Parcial 1 (EP1) do Projeto Integrado 4 / Integração de Sistemas**, o MVP Web Funcional foi formalmente submetido, integrado e homologado dentro de uma esteira automatizada de **Integração Contínua (CI)** com o **GitHub Actions**. O software provou sua robustez e portabilidade ao executar de forma determinística em runners virtuais Linux (`ubuntu-24.04`), passando com 100% de sucesso por todas as etapas de compilação sintática, suíte de 79 testes automatizados com Pytest, checagem estática de tipos TypeScript e empacotamento otimizado com Vite 6.

---

## 2. Homologação Automatizada do MVP no Pipeline de CI

A validação contínua do sistema foi estruturada em dois jobs paralelos e desacoplados no arquivo [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml):

```text
RESULTADOS DA HOMOLOGAÇÃO NO GITHUB ACTIONS:
├── Job backend-ci (Python 3.12 / Ubuntu 24.04):
│   ├── Verificação de Sintaxe: OK (compileall sem alertas)
│   ├── Suíte de Testes Automatizados: 79 testes PASSED em ~4.2s
│   ├── Isolamento do SQLite: OK (fixtures com tmp_path)
│   └── Relatório JUnit XML: Persistido e publicado via Artifacts (pytest-results-report)
│
└── Job frontend-ci (Node.js 22.20.0 / Ubuntu 24.04):
    ├── Instalação de Dependências: OK (npm ci determinístico com package-lock.json)
    ├── Verificação Estática de Tipos: OK (tsc --noEmit com 0 erros de contrato)
    └── Build de Produção: OK (vite build empacotando 3.682 módulos sem warnings críticos)
```

---

## 3. Destaques das Funcionalidades do MVP Homologado

### 3.1 Módulo do Responsável Legal (Família)
- **Gestão de Múltiplos Dependentes:** Alternância instantânea entre os 3 dependentes cadastrados (*João Silva Oliveira* ID 1, *Ana Silva Oliveira* ID 2 e *Pedro Costa Santos* ID 3).
- **Dashboard de Alertas Preventivos:** Exibição de médias gerais, assiduidade e sinalizadores automáticos de risco de reprovação.
- **Boletim Escolar Oficial:** Tabela consolidada dos 4 bimestres com cálculo de aprovação e folha de estilos otimizada para impressão física (`@media print`).
- **Notas Detalhadas (100% Somente Leitura):** Consulta analítica de notas por avaliação, pesos e fórmula de média ponderada, com proteção estrita contra alterações por responsáveis.
- **Frequência e Calendário Completo dos Pais:** Grade de assiduidade de Fevereiro a Dezembro com categorização de faltas justificadas e grade semanal de aulas (07:00 às 22:00).
- **Mural de Avisos e Comunicados:** Comunicados institucionais com categorização por criticidade, remetente formal e confirmação instantânea de leitura (`✓ Lido`).

### 3.2 Módulo do Corpo Docente (Professor)
- **Seleção Dinâmica de Escopo:** Seletores interdependentes de Turma, Disciplina, Tipo de Registro (*Notas*, *Frequência*, *Avisos*), Bimestre/Visão (*1º BM*, *2º BM*, *3º BM*, *4º BM*, *Consolidado*) e Ano letivo.
- **Cinco Modos Especializados de Tabela:**
  1. *Modo Avaliação Específica:* Lançamento e edição de notas de 0.0 a 10.0 com validação visual imediata.
  2. *Modo Todas as Avaliações com Peso:* Formato padronizado **`Avaliação N (Peso: X.X)`**, cálculo de média ponderada e situação bimestral.
  3. *Modo Consolidado de Notas:* Médias dos 4 bimestres, média geral e situação final do aluno.
  4. *Modo Chamada Mensal Dinâmica:* Modal de horários e vigência, botão alternável `✓ Total` $\leftrightarrow$ `✖ Limpar`, suporte a campos em branco (`""`) e restauração automática via `useEffect`.
  5. *Modo Consolidado de Frequência:* Apuração consolidada com badges de situação (`✓ Aprovado por Frequência` para $\ge 75\%$ e `⚠️ Reprovado por Falta` para $< 75\%$).
- **Criação e Edição Dinâmica de Avaliações:** Botões `+ Adicionar Avaliação para a Turma` e `✏️ Editar Avaliação`, sincronizando com o SQLite via `PUT /api/teacher/assessments/{id}` e recalculando médias em tempo real.

### 3.3 Módulo do Desenvolvedor (Equipe Técnica)
- **1. Documentação da API:** Acesso direto ao Swagger UI Live via rota relativa (`/docs`) ou direta (`:8000/docs`).
- **2. Documentação Técnica:** Visualizador interativo na SPA que carrega e renderiza na íntegra os documentos técnicos do projeto com suporte a Mermaid, LaTeX e caixas de código com syntax highlighting.
- **3. Integrantes:** Apresentação acadêmica oficial dos discentes da UFCA (Antonio Alex Dayson Tomaz e Maria Alexsandra Tomaz).
- **4. Sobre:** Painel analítico detalhando a Clean Architecture, esteira de CI e componente extensionista.

---

## 4. Conformidade com Acessibilidade (WCAG 2.1 AA) e Usabilidade (Nielsen)

| Diretriz / Heurística | Implementação Concreta no TrAcEs |
| :--- | :--- |
| **WCAG 1.4.1 (Uso da Cor)** | **Codificação Semântica Tripla:** cor de alto contraste, ícone representativo (`✓`, `⚠️`, `✕`) e texto explícito. |
| **WCAG 1.4.3 / 1.4.11 (Contraste)** | Relação de contraste mínima de 4,5:1 para texto normal, 7:1 para modo Alto Contraste nativo e suporte a `prefers-contrast: more`. |
| **WCAG 2.4.1 (Bypass Blocks)** | *Skip Link* no topo da página direcionando o foco do teclado imediatamente para a tag `<main id="main-content">`. |
| **WCAG 2.4.7 (Focus Visible)** | Anéis de foco de 2px em cor azul de alto contraste visíveis em todos os elementos interativos. |
| **WCAG 4.1.2 (Name, Role, Value)** | Marcação semântica com ARIA attributes (`aria-expanded`, `aria-controls`, `aria-label`, `role="status"`). |
| **Nielsen #1 (Visibilidade do Status)** | Indicadores de carregamento, badges de situação pedagógica e toasts informativos instantâneos. |
| **Nielsen #5 (Prevenção de Erros)** | Modais de confirmação prévia antes de qualquer gravação permanente no banco de dados. |

---

## 5. Conclusão da Homologação

A integração e homologação do **MVP Web Funcional no GitHub Actions** atesta que o sistema TrAcEs atingiu nível de excelência em termos de estabilidade, qualidade de código e conformidade acadêmica com as disciplinas de Projeto Integrado 4 e Integração de Sistemas.
