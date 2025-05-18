from app.usecase import cnj_validator


def test_validade_cnj():
    assert cnj_validator('0000001-00.2023.1.01.0001') == True
    assert cnj_validator('invalid-cnj') == False
