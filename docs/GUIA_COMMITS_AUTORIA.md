<!-- markdownlint-disable -->

# Guia de Commits e Autoria — EP1 (Dayson e Alexsandra)

**Objetivo:** construir o histórico do Git de forma que o GitHub registre corretamente
**Antonio Alex Dayson Tomaz** e **Maria Alexsandra Tomaz** como autores das partes que
cada um desenvolveu no EP1.

> **Pré-condição:** repositório Git inicializado na branch `main` (o comando
> `git init -b main` cobre o caso de ainda não existir). Como o histórico parte do zero,
> não é necessário reescrever commits.

---

## 1. Como o GitHub identifica o autor

1. O GitHub usa o **nome e o e-mail gravados no commit** (`author`), não quem executou o `push`.
2. Para o commit aparecer com avatar e contar no gráfico de contribuições, o e-mail do commit
   precisa estar **adicionado e verificado** na conta GitHub da pessoa.
3. O `committer` é quem aplicou o commit; o GitHub exibe o `author` como autoria principal.
4. **Coautoria** é registrada com um trailer no corpo da mensagem:
   `Co-authored-by: Nome <email>` — o GitHub mostra os dois avatares no commit.
5. Nunca use e-mail genérico (`root@`, `admin@`) ou o e-mail de outra pessoa.

---

## 2. Pré-requisitos

- Conta GitHub de cada integrante.
- E-mail verificado em **GitHub → Settings → Emails**.
  - Se a conta usa "Keep my email addresses private", utilize o formato
    `<ID>+<usuario>@users.noreply.github.com` (o GitHub mostra o endereço em Settings → Emails).
- Git instalado (versão local verificada: `2.50.1.windows.1`).
- Um dos integrantes cria o repositório remoto e, se os dois forem fazer `push`,
  adiciona o outro em **Settings → Collaborators**.

---

## 3. Definir as identidades (PowerShell)

Execute na raiz do projeto. Use os e-mails **reais e verificados** no GitHub:

```powershell
$daysName  = "Antonio Alex Dayson Tomaz"
$daysEmail = "alex.dayson@aluno.ufca.edu.br"   # confirme se está verificado no GitHub
$alexName  = "Maria Alexsandra Tomaz"
$alexEmail = "alexsandra.tomaz@aluno.ufca.edu.br"   # confirme se está verificado no GitHub

# Conferir o que será gravado
Write-Output "$daysName <$daysEmail>"
Write-Output "$alexName <$alexEmail>"
```

> **Não altere o `git config --global`.** O guia usa `git -c user.name=... -c user.email=...`
> em cada commit, evitando que a identidade de um "vaze" para o commit do outro.

---

## 4. Inicializar o repositório

```powershell
git init -b main
git status --short
```

Confirme que arquivos gerados estão ignorados:

```powershell
git status --ignored --short |
  Select-String "node_modules|frontend/dist|reports|\.db|__pycache__"
```

> **Atenção:** não use `git add .` antes dos commits planejados — isso misturaria as autorias.

---

## 5. Mapa dos cinco commits

| Commit | Autor | Coautor | Escopo | Caminhos |
| :---: | :--- | :--- | :--- | :--- |
| **C1** | Dayson | Alexsandra | **Upload geral compartilhado**: estrutura, docs históricos e assets | `.gitignore`, `.markdownlint.json`, `pytest.ini`, `docs/pi2-ep2/`, `docs/pi2-ep3/`, `docs/pi3-ep1/`, `docs/pi3-ep2/`, `docs/pi3-ep3/`, `docs/swagger.html`, `docs/assets/` (exceto `ci/`) |
| **C2** | Alexsandra | — | Interface SPA, acessibilidade e protótipos | `frontend/` |
| **C3** | Dayson | — | CI, runner local e backend | `.github/`, `backend/`, `scripts/` |
| **C4** | Alexsandra | — | README e instruções de uso do CI | `README.md`, `docs/assets/ci/LEIA-ME-EVIDENCIAS.md` |
| **C5** | Dayson | — | Relatório, plano, guia de autoria e espelhos | `RELATORIO_FINAL_PI4_EP1.md`, `PLANO_DE_ACAO_PI4_EP1.md`, `docs/GUIA_COMMITS_AUTORIA.md`, `docs/RELATORIO_FINAL_PI4_EP1.md`, `docs/PLANO_DE_ACAO_PI4_EP1.md` |

> Apenas o C1 tem dois nomes (upload geral). Os demais têm autor único, conforme a divisão
> de responsabilidades registrada no relatório.

---

## 6. Executar os commits

### C1 — Upload geral compartilhado (estrutura, histórico e assets)

```powershell
git add .gitignore .markdownlint.json pytest.ini `
  docs/pi2-ep2 docs/pi2-ep3 docs/pi3-ep1 docs/pi3-ep2 docs/pi3-ep3 `
  docs/swagger.html docs/assets/alta-fidelidade `
  docs/assets/wireframe-baixa-fidelidade docs/assets/diagramas_arquitetura
git status --short
git -c user.name="$daysName" -c user.email="$daysEmail" commit `
  -m "chore: upload geral da estrutura, histórico e assets do projeto" `
  -m "Co-authored-by: Maria Alexsandra Tomaz <$alexEmail>"
```

### C2 — Alexsandra (UI/UX + protótipos)

```powershell
git add frontend
git status --short
git -c user.name="$alexName" -c user.email="$alexEmail" commit `
  -m "feat(ui): SPA TrAcEs acessível e assets de prototipação"
```

### C3 — Dayson (CI + backend)

```powershell
git add .github backend scripts
git status --short
git -c user.name="$daysName" -c user.email="$daysEmail" commit `
  -m "feat(ci): pipeline GitHub Actions, runner local e backend Clean Architecture"
```

### C4 — Alexsandra (README)

```powershell
git add README.md docs/assets/ci/LEIA-ME-EVIDENCIAS.md
git status --short
git -c user.name="$alexName" -c user.email="$alexEmail" commit `
  -m "docs(readme): instruções de CI, execução manual e componente extensionista"
```

### C5 — Dayson (relatório, plano, guia e espelhos)

```powershell
git add RELATORIO_FINAL_PI4_EP1.md PLANO_DE_ACAO_PI4_EP1.md `
  docs/GUIA_COMMITS_AUTORIA.md docs/RELATORIO_FINAL_PI4_EP1.md `
  docs/PLANO_DE_ACAO_PI4_EP1.md
git status --short
git -c user.name="$daysName" -c user.email="$daysEmail" commit `
  -m "docs(report): relatório final, plano de ação e matriz de evidências do EP1"
```

Ao final:

```powershell
git status --short   # deve ficar vazio
```

---

## 7. Verificar a autoria antes de publicar

```powershell
git log --graph --pretty=format:"%h | %an <%ae> | %s"
git shortlog -sne --all
git show --stat --pretty=fuller HEAD
```

Resultado esperado:

- **5 commits**;
- **2 autores** no `git shortlog` (Dayson e Alexsandra);
- cada commit contendo apenas os caminhos do seu escopo;
- trailer `Co-authored-by` visível **apenas no C1**, com `git show -s --format=%B`.

---

## 8. Criar o repositório remoto e publicar

1. No GitHub, crie um repositório **vazio** (sem README, `.gitignore` ou licença).
2. Conecte e envie:

```powershell
git remote add origin https://github.com/alexdaysonufca/sistema_acompanhamento_escolar_pi4_ep1.git
git remote -v
git push -u origin main
```

3. Se os dois forem fazer `push`, adicione o outro como colaborador em
   **Settings → Collaborators**.
4. GitHub CLI é opcional (não está instalado nesta máquina). Para instalar:
   `winget install --id GitHub.cli`, depois `gh auth login`.

> O `push` pode ser feito por apenas um integrante: a autoria dos commits **não muda**.
> Cada pessoa só precisa que o e-mail usado no commit esteja verificado na própria conta.

---

## 9. Conferir no GitHub

1. **Commits:** `https://github.com/<conta>/pi_4_ep_1/commits/main` — cada commit deve
   exibir o avatar do autor e, quando houver, o avatar do coautor.
2. **Se algum commit aparecer sem avatar:** o e-mail não está vinculado à conta.
   Adicione/verifique o e-mail em **Settings → Emails**; o GitHub costuma vincular
   commits antigos retroativamente. Se não vincular, use a seção 10.
3. **Actions:** a aba *Actions* deve mostrar a execução `CI - TrAcEs` disparada pelo `push`,
   com `backend-ci` e `frontend-ci` aprovados.
4. **Artefato:** baixe `pytest-results-report` no *Run Summary*.
5. **Badge:** o selo no README deve passar a exibir `passing`.
6. **Evidências:** capture os seis prints previstos na Seção 7.4 do relatório e salve em
   `docs/assets/ci/`.

---

## 10. Se algum commit sair com autoria errada

**Último commit:**

```powershell
git commit --amend --author="Maria Alexsandra Tomaz <email>" --no-edit
```

**Vários commits (ainda não publicados):**

```powershell
git rebase -i --root
# marque o commit como "edit", rode:
git commit --amend --author="Nome <email>" --no-edit
git rebase --continue
```

**Normalizar nomes/e-mails antigos (opcional):** crie um `.mailmap` na raiz:

```text
Antonio Alex Dayson Tomaz <email-atual> <email-antigo>
Maria Alexsandra Tomaz <email-atual> <email-antigo>
```

> `.mailmap` muda apenas a exibição; não altera a vinculação da conta.
> Reescrever histórico já publicado exige `push --force` e deve ser evitado após a entrega.

---

## 11. Fluxo recomendado daqui para frente

- Cada integrante trabalha no próprio clone e em uma branch (`feat/...`, `docs/...`).
- Abre *Pull Request*; o CI precisa passar; o colega revisa e faz o merge.
- Em trabalho conjunto, use `Co-authored-by:` no corpo do commit.
- Mantenha `git config --local user.name/user.email` configurado em cada clone para não
  misturar identidades.
- (Opcional) Ative *branch protection* exigindo os jobs `backend-ci` e `frontend-ci`.

---

## 12. Checklist final

- [ ] E-mails verificados nas duas contas GitHub.
- [ ] `git init -b main` executado.
- [x] C1 (upload geral, Dayson + Alexsandra) criado.
- [x] C2 (Alexsandra) criado.
- [x] C3 (Dayson) criado.
- [x] C4 (Alexsandra) criado.
- [x] C5 (Dayson) criado.
- [x] `git log` mostra os dois autores e o trailer de coautoria apenas no C1.
- [x] `git status` limpo.
- [x] Repositório remoto criado e `push` realizado.
- [x] Avatares corretos na página de commits.
- [x] Execução do workflow aprovada e artefato baixado.
- [ ] Prints salvos em `docs/assets/ci/` e inseridos no relatório.

---

## 13. Resultado da Execução

- **Repositório oficial:** `https://github.com/alexdaysonufca/sistema_acompanhamento_escolar_pi4_ep1`
- **Commits publicados:** 5 — C1 (upload geral, Dayson + Alexsandra), C2 (UI, Alexsandra), C3 (CI/backend, Dayson), C4 (README, Alexsandra) e C5 (relatório/plano, Dayson).
- **Contas vinculadas:** `alexdaysonufca` e `alexsandratomazufca`.
- **Pipeline:** aprovado na aba *Actions*, com `backend-ci` e `frontend-ci` verdes.
- **Concluído:** prints da aba *Actions* anexados e catálogo de evidências em `docs/assets/ci/`.
- **Opcional:** configuração de *branch protection*.
