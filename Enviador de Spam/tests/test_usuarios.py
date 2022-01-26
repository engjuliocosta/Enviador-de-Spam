from spam.modelos import Usuario

def test_salvar_usuario(sessao):
    usuario = Usuario( nome='Julio', email='julio_costa06@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuario(sessao):
    usuarios = [
        Usuario( nome='Julio', email='julio_costa06@hotmail.com'),
        Usuario( nome='Henrique', email='henriquegomes02@gmail.com' )
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()




