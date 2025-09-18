## Dependências

Tratando-se de um pacote com as dependência gerenciadas pelo [uv](https://docs.astral.sh/uv/), para criar o ambiente de desenvolvimento basta dar o comando abaixo.

```shell
# Instala os pacotes definidos no pyproject.toml
uv sync --group docs --group dev
```

<br>

---

## Documentação

A documentação do projeto foi feita usando o [MkDocs](https://www.mkdocs.org/), com _deploy_ no [Read The Docs](https://app.readthedocs.org/).

Para testar localmente, basta usar:

```shell
# Serve Localmente
mkdocs serve
```
