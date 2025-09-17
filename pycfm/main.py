"""
Módulo para pesquisa de médicos

sss
"""

import json
import warnings
from pathlib import Path
from urllib.parse import urljoin

import requests

# from typing import Literal
# import pandas as pd


URL_BASE = 'https://portal.cfm.org.br/'


class Medico:
    def __init__(self, crm=240538) -> None:
        self.crm_class = crm

        self._busca_medico()
        self._buscar_foto()
        self._request_foto()

    def _busca_medico(self):
        """
        _summary_

        :param crm: _description_, defaults to 240538
        :type crm: int, optional
        :raises Exception: _description_
        :raises Exception: _description_
        :raises Exception: _description_
        """
        # Monta URL
        url = urljoin(
            base=URL_BASE, url='/api_rest_php/api/v1/medicos/buscar_medicos'
        )

        # Faz Requisição
        r = requests.post(
            url=url,
            json=[
                {
                    'useCaptchav2': True,
                    'captcha': '0cAFcWeA5PbSMF1dx0PQ4mDwsHahYn_y0MD43eMwGRjSEGARjaQvG6GGn7ZaRIYj3sxnlBZqdt7yU1URWLsS3VTm0laspQdPxyrBo1mgDMspcZ6nrnvCQhwXF1P2Mw-OGpH4YEaVnuvCXFnPja9drpcbgfQd0Ux0rUL5_7iWAcnndlqWRCaGllcIryIEoESOS1PnG0rYzgECZ6m8jq78Pxisx_BE56wslOy-0ZiJnc0um-oZ93lLXGxVpwnfW13HH8ZSPvekEREpS81Ahspdtp6LH_We0QRr2IJu4UGzZ-E6m4NQOoYPYd1aprWIvwt2aUME5n2ezAtK45ZH1JXiZwqMwOeSB8BQszpkJ25uAAvLhAARUqCb_ovll3N6-p8ffzRx-7EFIso-m_FTiTmMnKwotscGnSoLPCd1_LBH_5yRyAjvEP9jFDBVYiQX--udnS6I9VcvQ_Z9ifrCIN7LjEnKuL8UJRL6mr0BWnstWxFDMuMEOYedtNtaPQ45I-P502TMA8Anmz_9CdbPFgsd4M4MLR6mVcUSybnEyCEDmCkpqH2FT4P-Z_ZBFr64ez91k8vKLdmjqvwbtaysewcYTXtzYTYCkS9NHtHyQkaNNKaP9-1w8v_R5BJI5YgccDsOjY4Vupejgif7vgemYzGyb5GR0_YxzSli8nOvsZ5vQxgSwkEyfNsHdunrThUsDDDqmWwihPQ0vOcBqT3wSIBBP00iv0JKIooI4Prxlc9ehTM2_xvxle5M-Ixd7Atk2qt1VaFdb57YqcmD17',
                    'medico': {
                        'nome': '',
                        'ufMedico': '',
                        'crmMedico': f'{self.crm_class}',
                        'municipioMedico': '',
                        'tipoInscricaoMedico': '',
                        'situacaoMedico': '',
                        'detalheSituacaoMedico': '',
                        'especialidadeMedico': '',
                        'areaAtuacaoMedico': '',
                    },
                    'page': 1,
                    'pageNumber': 1,
                    'pageSize': 10,
                }
            ],
        )

        # Avalia Response
        if r.status_code == 200:
            data = json.loads(r.content.decode(encoding='utf-8'))

        else:
            raise Exception('Acesso a API não deu certo')

        # Avalia Content
        if data['status'] == 'sucesso':
            if len(data['dados']) == 1:
                self._data = data['dados'][0]

            else:
                self._data = data['dados']
                warnings.warn('Avaliar por que deu mais que um registro!')
                raise Exception('Avaliar por que deu mais que um registro!')

        else:
            raise Exception('Retorno no resultado não deu certo!')

    @property
    def uf(self):
        return self._data['SG_UF']

    @property
    def crm(self):
        return self._data['NU_CRM']

    @property
    def crm_natural(self):
        return self._data['NU_CRM_NATURAL']

    @property
    def nome(self):
        return self._data['NM_MEDICO']

    @property
    def nome_social(self):
        return self._data['NM_SOCIAL']

    @property
    def data_inscricao(self):
        return self._data['DT_INSCRICAO']

    @property
    def id_tipo_inscricao(self):
        return self._data['IN_TIPO_INSCRICAO']

    @property
    def tipo_inscricao(self):
        return self._data['TIPO_INSCRICAO']

    @property
    def id_situacao(self):
        return self._data['COD_SITUACAO']

    @property
    def situacao(self):
        return self._data['SITUACAO']

    @property
    def especialidade(self):
        return self._data['ESPECIALIDADE']

    @property
    def instituicao_graduacao(self):
        return self._data['NM_INSTITUICAO_GRADUACAO']

    @property
    def ano_graduacao(self):
        return self._data['DT_GRADUACAO']

    @property
    def security_hash(self):
        return self._data['SECURITYHASH']

    def _buscar_foto(self):
        """
        _summary_

        :raises Exception: _description_
        :raises Exception: _description_
        :raises Exception: _description_
        """

        # Monta URL
        url = urljoin(
            base=URL_BASE, url='/api_rest_php/api/v1/medicos/buscar_foto'
        )

        # Faz requisição
        r = requests.post(
            url=url,
            json=[
                {
                    'securityHash': self.security_hash,
                    'crm': f'{self.crm}',
                    'uf': self.uf,
                }
            ],
        )

        # Avalia Response
        if r.status_code == 200:
            data = json.loads(r.content.decode(encoding='utf-8'))

        else:
            raise Exception('Acesso a API não deu certo')

        # Avalia Content
        if data['status'] == 'sucesso':
            if len(data['dados']) == 1:
                self._data_foto = data['dados'][0]

            else:
                self._data_foto = data['dados']
                warnings.warn('Avaliar por que deu mais que um registro!')
                raise Exception('Avaliar por que deu mais que um registro!')

        else:
            raise Exception('Retorno no resultado não deu certo!')

    @property
    def id_solicitante(self):
        return self._data_foto['ID_SOLICITANTE']

    @property
    def situacao2(self):
        return self._data_foto['SITUACAO']

    @property
    def endereco(self):
        return self._data_foto['ENDERECO']

    @property
    def telefone(self):
        return self._data_foto['TELEFONE']

    @property
    def inscricao(self):
        return self._data_foto['INSCRICAO']

    @property
    def autorizacao_imagem(self):
        return self._data_foto['AUTORIZACAO_IMAGEM']

    @property
    def autorizacao_endereco(self):
        return self._data_foto['AUTORIZACAO_ENDERECO']

    @property
    def vp_destino(self):
        return self._data_foto['VP_DESTINO']

    @property
    def vp_inicio(self):
        return self._data_foto['VP_INICIO']

    @property
    def vp_fim(self):
        return self._data_foto['VP_FIM']

    @property
    def hash(self):
        return self._data_foto['HASH']

    def _request_foto(self):
        # Monta URL
        url = urljoin(
            base=URL_BASE,
            url='/wp-content/themes/portalcfm/assets/php/foto_medico.php',
        )

        r = requests.get(
            url=url,
            params={
                'crm': f'{self.crm}',
                'uf': self.uf,
                'hash': '4c0480bc18e5c1fecf4f3ba46beedfa9',
            },
        )

        # Avalia Response
        if r.status_code == 200:
            self.photo = r.content

        else:
            raise Exception('Acesso a API não deu certo')

    def save_photo(self, filepath: str | Path = 'foto_medico.jpg'):
        """
        _summary_

        :param filepath: _description_, defaults to 'foto_medico.jpg'
        :type filepath: str, optional
        """
        # Faz requisição de foto
        self._request_foto()

        # Para salvar a imagem, por exemplo:
        # output_path / f'medico_crm_{crm}.jpg'
        with open(file=filepath, mode='wb') as f:
            f.write(self.photo)


if __name__ == '__main__':

    medico = Medico(crm=240538)
    print(medico)
