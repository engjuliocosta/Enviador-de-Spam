from spam.enviador_de_email import Enviador, EmailInvalido


def teste_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['00243490@ufrgs.br', 'julio_costa06@hotmail.com']
                        )
def teste_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        '00243490@ufrgs.br',
        'Formatura',
        'Formatura dia 31 de janeiro',
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'julio']
                        )
def teste_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            '00243490@ufrgs.br',
            'Formatura',
            'Formatura dia 31 de janeiro',
        )