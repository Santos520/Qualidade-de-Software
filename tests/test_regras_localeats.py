import pytest

from src.regras_localeats import calcular_desconto


def test_pedido_com_desconto():
    resultado = calcular_desconto(100)
    assert resultado == 10


def test_pedido_sem_desconto():
    resultado = calcular_desconto(50)
    assert resultado == 0


def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-10)