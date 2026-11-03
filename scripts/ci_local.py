#!/usr/bin/env python3
"""
Executor local do pipeline de Integração Contínua do TrAcEs.

Reproduz, no computador do desenvolvedor, as mesmas verificações executadas
pelo workflow .github/workflows/ci.yml, permitindo validar a automação a
qualquer momento (sem depender de push ou do GitHub Actions).

Etapas executadas:
    1. Backend: verificação de sintaxe com compileall
    2. Backend: suíte de testes com Pytest + relatório JUnit XML
    3. Frontend: instalação determinística (npm ci, quando necessário)
    4. Frontend: verificação de tipos (tsc --noEmit)
    5. Frontend: build de produção (vite build)

Uso:
    python scripts/ci_local.py
    python scripts/ci_local.py --install         # força npm ci
    python scripts/ci_local.py --backend-only
    python scripts/ci_local.py --frontend-only
    python scripts/ci_local.py --no-build        # pula o build do frontend
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
REPORTS = ROOT / "reports"


def configure_stdout() -> None:
    """Garante UTF-8 no console do Windows."""
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure:
        try:
            reconfigure(encoding="utf-8")
        except OSError:
            pass


def run_step(label: str, command: list[str], cwd: Path) -> bool:
    """Executa um comando e devolve True em caso de sucesso."""
    printable = " ".join(command)
    print(f"\n[CI-LOCAL] {label}")
    print(f"[CI-LOCAL] $ {printable}  (cwd: {cwd})")
    try:
        completed = subprocess.run(command, cwd=cwd)
    except FileNotFoundError:
        print(f"[CI-LOCAL] FALHOU: executável não encontrado para '{command[0]}'.")
        return False
    except KeyboardInterrupt:
        print("\n[CI-LOCAL] Interrompido pelo usuário.")
        raise SystemExit(130)

    if completed.returncode == 0:
        print(f"[CI-LOCAL] OK: {label}")
        return True

    print(f"[CI-LOCAL] FALHOU: {label} (código {completed.returncode})")
    return False


def npm_command() -> str | None:
    """Localiza o npm no PATH (npm.cmd no Windows)."""
    return shutil.which("npm") or shutil.which("npm.cmd")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Executa localmente as verificações do GitHub Actions."
    )
    parser.add_argument("--install", action="store_true", help="Executa npm ci antes das verificações do frontend.")
    parser.add_argument("--backend-only", action="store_true", help="Executa apenas o job de backend.")
    parser.add_argument("--frontend-only", action="store_true", help="Executa apenas o job de frontend.")
    parser.add_argument("--no-build", action="store_true", help="Executa typecheck, mas não o build do frontend.")
    args = parser.parse_args()

    configure_stdout()
    REPORTS.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, bool]] = []

    if not args.frontend_only:
        results.append(
            (
                "Backend: verificação de sintaxe (compileall)",
                run_step(
                    "Backend: verificação de sintaxe (compileall)",
                    [sys.executable, "-m", "compileall", "-q", "backend/src", "backend/main.py"],
                    ROOT,
                ),
            )
        )
        results.append(
            (
                "Backend: testes automatizados (pytest)",
                run_step(
                    "Backend: testes automatizados (pytest)",
                    [
                        sys.executable,
                        "-m",
                        "pytest",
                        "-v",
                        "--junitxml=reports/pytest-results.xml",
                    ],
                    ROOT,
                ),
            )
        )

    if not args.backend_only:
        npm = npm_command()
        if not npm:
            print("[CI-LOCAL] FALHOU: npm não encontrado no PATH. Instale o Node.js 22.x.")
            results.append(("Frontend: npm disponível", False))
        else:
            node_modules = FRONTEND / "node_modules"
            if args.install or not node_modules.exists():
                reason = "npm ci (solicitado)" if args.install else "npm ci (node_modules ausente)"
                results.append(
                    (
                        f"Frontend: {reason}",
                        run_step(f"Frontend: {reason}", [npm, "ci"], FRONTEND),
                    )
                )
            else:
                print("\n[CI-LOCAL] Frontend: node_modules presente; npm ci não será executado (use --install para forçar).")

            results.append(
                (
                    "Frontend: verificação de tipos (tsc --noEmit)",
                    run_step("Frontend: verificação de tipos (tsc --noEmit)", [npm, "run", "typecheck"], FRONTEND),
                )
            )

            if not args.no_build:
                results.append(
                    (
                        "Frontend: build de produção (vite build)",
                        run_step("Frontend: build de produção (vite build)", [npm, "run", "build"], FRONTEND),
                    )
                )

    print("\n" + "=" * 68)
    print("RESUMO DA EXECUÇÃO LOCAL DO CI")
    print("=" * 68)
    for label, ok in results:
        print(f"  [{'OK' if ok else 'FALHOU'}] {label}")

    failures = sum(1 for _, ok in results if not ok)
    print("-" * 68)
    if failures:
        print(f"Resultado: {failures} etapa(s) com falha de {len(results)} verificada(s).")
        return 1

    print(f"Resultado: todas as {len(results)} etapas foram concluídas com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
