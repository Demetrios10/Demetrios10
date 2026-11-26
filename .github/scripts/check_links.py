"""Valida caminhos locais e títulos duplicados nos documentos do perfil."""

import re
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
HEADING_PATTERN = re.compile(r"^## (.+)$", re.MULTILINE)
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^\s)]+)")
EXTERNAL_PREFIXES = ("https:", "http:", "mailto:", "#")


def markdown_files(root: Path) -> Iterator[Path]:
    return (path for path in root.rglob("*.md") if ".git" not in path.parts)


def duplicated_headings(text: str) -> list[str]:
    counts = Counter(HEADING_PATTERN.findall(text))
    return [heading for heading, total in counts.items() if total > 1]


def missing_local_links(path: Path, text: str) -> list[str]:
    missing = []
    for link in LINK_PATTERN.findall(text):
        if link.startswith(EXTERNAL_PREFIXES):
            continue
        target = unquote(link.split("#")[0])
        if target and not (path.parent / target).exists():
            missing.append(target)
    return missing


def document_errors(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT)
    return [f"{name}: título repetido: {heading}" for heading in duplicated_headings(text)] + [
        f"{name}: caminho ausente: {target}" for target in missing_local_links(path, text)
    ]


def main() -> None:
    errors = [error for path in markdown_files(ROOT) for error in document_errors(path)]
    if errors:
        raise SystemExit("\n".join(errors))
    print("Documentos: caminhos locais válidos e títulos sem duplicidade.")


if __name__ == "__main__":
    main()
