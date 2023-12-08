import pytest

from ex001 import Pessoa, InvalidNameError, InvalidPhoneError

def test_pessoa_creation():
    person = Pessoa("Abner Eger", "+55 49 9 9170-0435")

    assert person.nome == "Abner Eger"
    assert person.telefone == "+55 49 9 9170-0435"

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        person = Pessoa("Abner", "+55 49 9 9170-0435")

def test_invalid_phone():
    with pytest.raises(InvalidPhoneError):
        person = Pessoa("Abner Eger", "")