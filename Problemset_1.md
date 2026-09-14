a: On branch main
Your branch is up to date with 'origin/main'.

## Durch `uv` erzeugte Dateien

### `pyproject.toml`

Diese Datei enthält die Konfiguration des Python-Projekts. Sie definiert unter anderem:

- den Projektnamen `simulation-von-quantenschaltungen`,
- die Version `0.1.0`,
- die Python-Anforderung `>=3.9`,
- die derzeit leere Liste der Abhängigkeiten,
- sowie das Build-System `uv_build`.

### `src/simulation_von_quantenschaltungen/__init__.py`

Diese Datei kennzeichnet das Verzeichnis als Python-Paket. Sie enthält außerdem die Funktion `hello()`, die den Text `Hello from simulation-von-quantenschaltungen!` zurückgibt.

### `.python-version`

In dieser Datei steht `3.9`. Dadurch wird festgelegt, dass für das Projekt Python 3.9 verwendet werden soll.

## 1.4d) Weitere Python-Werkzeuge und Ruff-Konfiguration

Für die Codequalität wurden Ruff und Mypy ausprobiert. Ruff übernimmt sowohl
Linting als auch Formatierung. In `pyproject.toml` sind dafür die NPY-Regeln
für NumPy-Code, Python 3.9 als Zielversion, eine maximale Zeilenlänge von 88
Zeichen und die Ausschlüsse `.venv` und `local` konfiguriert. Außerdem verwendet
Ruff doppelte Anführungszeichen und Tabulatoren zur Einrückung.

Mit `uvx ruff check` werden mögliche Fehler und Verstöße gegen die aktivierten
Regeln gefunden. `uvx ruff format --check` prüft, ob die Dateien korrekt
formatiert sind. Mypy ergänzt Ruff durch statische Typprüfung. Dadurch wurde zum
Beispiel erkannt, dass `greet(42)` nicht zur Signatur `greet(name: str)` passt.
Nach der Änderung zu `greet("Einstein")` war die Typprüfung erfolgreich.

Als besonders nützlich wurde `pre-commit` gefunden. Die konfigurierten Hooks
führen YAML-Prüfung, Bereinigung von Zeilenenden, Black und Mypy automatisch
vor einem Commit aus. Mit `uvx pre-commit run --all-files` können alle Dateien
manuell geprüft werden. Die Ergebnisse und Erfahrungen mit diesen Werkzeugen
werden mit den anderen Studierenden besprochen.

### Weitere nützliche Konfigurationen

Zusätzlich können Ruff-Regelgruppen gezielt aktiviert werden:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "NPY", "B", "UP"]
ignore = ["E501"]
fixable = ["ALL"]

[tool.ruff.lint.isort]
known-first-party = ["simulation_von_quantenschaltungen"]
```

Dabei prüfen `E` und `F` Stilregeln und häufige Fehler, `I` sortiert Importe,
`B` findet mögliche Bugs und `UP` empfiehlt modernere Python-Syntax. Mit
`fixable = ["ALL"]` darf Ruff automatisch behebbare Probleme korrigieren.

Für Mypy sind eine feste Python-Version und strengere Typprüfungen hilfreich:

```toml
[tool.mypy]
python_version = "3.9"
strict = true
warn_unused_ignores = true
disallow_untyped_defs = true
check_untyped_defs = true
```

Nützliche Befehle sind `uvx ruff check --fix`, `uvx ruff format`, `uvx mypy src`
und `uvx pre-commit run --all-files`. Besonders `select`, `src`, `fixable` und
`strict` helfen dabei, die automatische Prüfung an das eigene Projekt anzupassen.
