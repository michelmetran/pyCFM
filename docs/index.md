[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/pyESAJ)
[![PyPI - Version](https://img.shields.io/pypi/v/pyesaj?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/pyesaj/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/pyESAJ?logo=ReadTheDocs&label=Read%20The%20Docs)](https://pyESAJ.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/pyESAJ/actions/workflows/publish-to-pypipoetry.yml/badge.svg)](https://github.com/michelmetran/pyESAJ/actions/workflows/publish-to-pypipoetry.yml)

O [e-SAJ](https://esaj.tjsp.jus.br/) (_Sistema de Automação da Justiça_) é um
portal
do [Tribunal de Justiça de São Paulo](https://www.tjsp.jus.br/) (TJSP),
desenvolvido
pela [Softplan](https://www.softplan.com.br/), que facilita a troca de
informações e agiliza o trâmite processual. Ele
oferece diversos serviços _online_ voltados para advogados, cidadãos e
serventuários da justiça. Algumas funcionalidades
do e-SAJ incluem:

- **Consulta Processual**: acesso às informações de tramitação dos processos de
  primeiro e segundo grau.
- **Peticionamento Eletrônico**: protocolo e consulta de petições iniciais e
  intermediárias.
- **Diário da Justiça Eletrônico**: consulta aos cadernos das edições
  publicadas.
- **_Push_**: serviço que permite ao advogado receber por e-mail as informações
  sobre a movimentação processual.

<br>

---

## Pacote

O
pacote [pyESAJ](https://dev.azure.com/mpsp/Informa%C3%A7%C3%B5es%20Estat%C3%ADsticas/_git/pyesaj)
foi desenvolvido para permitir a interação com
o [e-SAJ](https://esaj.tjsp.jus.br/) por meio
do _python_.

Foram utilizados conceitos de _web scraping_, por meio do
_framework_ [Selenium](https://www.selenium.dev/), para interagir com o _Sistema
de Automação da Justiça_, e também
o [Pydantic](https://docs.pydantic.dev/latest/) para validação de objetos,
parâmetros de _input_, parâmetros de pesquisa de processos judiciais, bem como
_outputs_ representados por listas de processos e outros objetos.

Para gerenciamento do projeto e dependências, utilizou-se
o [Poetry](https://python-poetry.org/).

<br>

---

## Motivação

Em meados de setembro de 2025 surgiu a necessidade de obter o nome de diversos médicos e eu só tinha os dados do CRM dos médicos.

Dessa forma foi criado o
_package_ [pyCFM](https://dev.azure.com/mpsp/Informa%C3%A7%C3%B5es%20Estat%C3%ADsticas/_git/pyesaj),
que obtem os dados

![CFM](./assets/logo_cfm.jpg)
