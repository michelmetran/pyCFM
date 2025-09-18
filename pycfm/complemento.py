"""
Módulo com funções complementares
"""

import unicodedata


def remover_acentos(texto: str) -> str:
    """
    Remove acentos e cedilhas

    :param texto: Texto com acento, cedilha etc.
    :return: Texto sem acento, cedilha etc.
    """
    if texto is None:
        return texto

    return (
        unicodedata.normalize('NFKD', texto)
        .encode('ASCII', 'ignore')
        .decode('ASCII')
    )


if __name__ == '__main__':
    # remover_acentos(texto='Gánçalo')
    # remover_acentos(texto='5.1')
    # remover_acentos(texto=None)
    pass
