<!-- markdownlint-disable -->


# TrAcEs - Protótipo Web de Alta Fidelidade

Este repositório contém o código-fonte da interface web SPA (*Single Page Application*) do projeto **TrAcEs — Trilha de Acompanhamento Escolar**, desenvolvida com React 18, Vite 6, Tailwind CSS v4, TypeScript e Radix UI / Shadcn UI.

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
- **Node.js**: Versão 18.0.0 ou superior.
- **Gerenciador de Pacotes**: `npm` (incluso no Node.js) ou `pnpm`.

---

## 🚀 Como Executar o Frontend

Siga os passos abaixo a partir do terminal de comando:

### 1. Entrar na Pasta do Frontend

A partir da raiz do monorepo (`pi_4_ep_1/`):

```bash
cd frontend
```

### 2. Instalar as Dependências

O repositório versiona `package-lock.json` e o pipeline de CI usa **exclusivamente NPM**.
Para reproduzir o comportamento do CI:

```bash
npm ci
```

> Evite `pnpm install` neste projeto: a existência de `pnpm-workspace.yaml` é um resquício
> do scaffold original e geraria um segundo lockfile, quebrando a reprodutibilidade.

### 3. Iniciar o Servidor de Desenvolvimento (Dev Server)

```bash
# Usando NPM:
npm run dev

# Ou usando PNPM:
pnpm dev
```

Após executar o comando, o Vite iniciará a aplicação localmente. Acesse o endereço no seu navegador:
👉 **[http://localhost:5173/](http://localhost:5173/)**

---

## 🛠️ Outros Comandos Úteis

### Verificar Tipos (Typecheck)

Para validar os contratos de tipo sem gerar arquivos (mesma etapa executada no CI):

```bash
npm run typecheck
```

### Compilar para Produção (Build)

Para verificar ou gerar os arquivos de produção estáticos na pasta `dist/`:

```bash
npm run build
```

> Para rodar typecheck e build juntos, além dos testes do backend, use na raiz do monorepo:
> `python scripts/ci_local.py --frontend-only`

---

## ♿ Recursos de Acessibilidade Integrados

Ao navegar no frontend, você pode utilizar a **Barra de Acessibilidade Global** no topo da página para:
- Ativar o tema de **Alto Contraste**.
- Aumentar (`Fonte: A+`) ou diminuir (`Fonte: A-`) o tamanho dos textos.
- Utilizar **Skip Links** (`Ir para o conteúdo`, `Ir para menu`) via navegação por teclado (`Tab`).

  