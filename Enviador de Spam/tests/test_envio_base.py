from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam
from spam.modelos import Usuario


class EnviadorMock:
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(selfself, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1

@pyteste.mark.parametrize(
    'usuarios',
    [
        [
            Usuario( nome='Julio', email='julio_costa06@hotmail.com'),
            Usuario( nome='Júlio', email='julinho.colorado@gmail.com' )
        ],
        [
            Usuario( nome='Julio', email='julio_costa06@hotmail.com'),
        ]
    ]
)
def test_qde_envio_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam( sessao, enviador)
    enviador_de_spam.enviar_email(
        'julio_costa06@hotmail.com',
        'Desenvolvendo robô de spam',
        'Confira a mensagem',
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_spam(sessao):
    usuario = Usuario( nome='Julio', email='julio_costa_06@hotmail.com'),
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'julio_costa_06@hotmail.com',
        'Desenvolvendo robô de spam',
        'Confira a mensagem',
    )
    assert enviador.enviar.assert_called_once_with(
        'julinho_colorado9@gmail.com',
        'julio_costa_06@hotmail.com',
        'Robô de email',
        'Testando... ',
    )
