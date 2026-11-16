"""Valida caminhos locais e títulos duplicados nos documentos do perfil."""

import re
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parents[2]
errors = []
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
    for heading in set(headings):
        if headings.count(heading) > 1:
            errors.append(f"{path.relative_to(root)}: título repetido: {heading}")
    for link in re.findall(r"\[[^\]]*\]\(([^\s)]+)", text):
        if link.startswith(("https:", "http:", "mailto:", "#")):
            continue
        target = unquote(link.split("#")[0])
        if target and not (path.parent / target).exists():
            errors.append(f"{path.relative_to(root)}: caminho ausente: {target}")
if errors:
    raise SystemExit("\n".join(errors))
print("Documentos: caminhos locais válidos e títulos sem duplicidade.")
