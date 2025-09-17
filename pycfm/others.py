"""
_summary_

ssssss
ssssss

ssssss
"""

import json
from typing import Literal
from urllib.parse import urljoin

import pandas as pd
import requests


URL_BASE = 'https://portal.cfm.org.br/'


class Lista:
    def __init__(
        self, lista: Literal['estado', 'especialidade', 'atuação']
    ) -> None:
        """
        _summary_

        :param lista: _description_
        :type lista: Literal['estado', 'especialidade', 'atuação']
        """

        # Definição da URL
        if lista == 'estado':
            url_suffix = '/api_rest_php/api/v1/medicos/listar_ufs'

        elif lista == 'especialidade':
            url_suffix = '/api_rest_php/api/v1/medicos/listar_especialidades'

        elif lista == 'atuação':
            url_suffix = '/api_rest_php/api/v1/medicos/buscar_areas_atuacao'

        else:
            raise Exception(
                'Precisa ser "estado", "especialidade" ou "atuação"'
            )

        url = urljoin(base=URL_BASE, url=url_suffix)

        # Faz Requisição
        r = requests.get(url=url)

        # Avalia Response
        if r.status_code == 200:
            data = json.loads(r.content.decode(encoding='utf-8'))

        else:
            raise Exception('Acesso a API não deu certo')

        # Avalia Content
        if data['status'] == 'sucesso':
            self.data = data['dados']

        else:
            raise Exception('Retorno no resultado não deu certo!')

    @property
    def as_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.data)

    @property
    def as_json(self):
        return self.data


if __name__ == '__main__':
    # Especialidades
    especialidades = Lista(lista='estado')
    print(especialidades.as_json)
