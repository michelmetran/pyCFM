# pyCFM

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/pyCFM)
[![PyPI - Version](https://img.shields.io/pypi/v/pycfm?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/pycfm/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/pyCFM?logo=ReadTheDocs&label=Read%20The%20Docs)](https://pyCFM.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/pyCFM/actions/workflows/publish-to-pypi-uv.yml/badge.svg)](https://github.com/michelmetran/pyCFM/actions/workflows/publish-to-pypi-uv.yml)

O [Conselho Federal de Medicina (CFM)](https://portal.cfm.org.br/) mantem serviço de busca de médicos, utilizando nome, CRM, especialidade etc. Inicialmente pensei em usar o _site_ do [Conselho Regional de Medicina do Estado de São Paulo (CREMESP)](https://cremesp.org.br/) contudo, dessa forma, eu só teria o CRM de médicos registrados no estado de São Paulo. Logo, optei por acessar o sistema de busca de médicos do [Conselho Federal de Medicina (CFM)](https://portal.cfm.org.br/).

![CFM](./docs/assets/logo_cfm.jpg)

<br>

Em meados de setembro de 2025 surgiu a necessidade de pesquisar diversos médicos, a partir do CRM. Para isso foi desenvolvido o [pyCFM](https://pyCFM.readthedocs.io/), que facilita a busca dessas informações usando _python_.

No Brasil os _Conselhos Regionais de Medicina_ (CRMs), são os órgãos responsáveis por fiscalizar e regulamentar o exercício da medicina em cada estado. Todo médico precisa estar registrado no CRM do estado onde atua para poder exercer legalmente a profissão.

- Cada médico tem um número de CRM único por estado. Portanto, é possível encontrar CRMs identicos para o mesmo CRM. Por isso a importância de definir o estado do CRM.
- O CRM também atua em questões éticas, julgando condutas médicas.
- Exemplo: [CREMESP](https://cremesp.org.br/) (São Paulo), CRM-RJ (Rio de Janeiro).

<br>

Já o [Conselho Federal de Medicina (CFM)](https://portal.cfm.org.br/) é o órgão nacional que supervisiona os _Conselhos Regionais de Medicina_ (CRMs). Ele define normas, regula a ética médica em nível federal e representa os médicos perante o governo e a sociedade.

- Atua na formulação de políticas públicas de saúde.
- Julga recursos de decisões dos CRMs.
- Publica resoluções que orientam a prática médica no Brasil.

<br>

---

## Pacote

- Para gerenciamento do projeto e dependências, utilizou-se o [uv](https://docs.astral.sh/uv/).
- Para documentação foi usado o [MkDocs](https://www.mkdocs.org/)
- Foi usado o [requests](https://pypi.org/project/requests/) para as requisições.

<br>

---

## TODO

1. ~~Usar `session`~~
