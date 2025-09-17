"""
_summary_

:return: _description_
:rtype: _type_
"""

import math
import unicodedata


def remover_acentos(texto):
    """
    Remove acentos

    :param texto: _description_
    :type texto: _type_
    :return: _description_
    :rtype: _type_
    """
    if texto is None:
        return texto

    return (
        unicodedata.normalize('NFKD', texto)
        .encode('ASCII', 'ignore')
        .decode('ASCII')
    )


# remover_acentos(texto='Gánçalo')
# remover_acentos(texto='5.1')
# remover_acentos(texto=None)
