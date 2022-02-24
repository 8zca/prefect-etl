# Prefect ETL sample

```
poetry install
poetry run python src/01_hello.py
```

## VSCode
touch .vscode/settings.json
```
{
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Args": [
    "--max-line-length",
    "110",
    "--ignore=E203,W503,W504"
  ],
  "python.formatting.blackPath": "black path", // input
  "python.formatting.blackArgs": ["--line-length", "110"],
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.sortImports.path": "isort path", // input
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
 }
}
```
