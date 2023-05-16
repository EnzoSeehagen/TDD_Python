from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_31_05_2000_deve_retornar_22(self):
        # GIVEN - CONTEXTO
        entrada = '31/05/2000'
        esperado = 23

        funcionario_teste = Funcionario("Enzo", entrada, 2000)

        # WHEN - AÇÃO
        resultado = funcionario_teste.idade()

        # THEN - DESFECHO
        assert resultado == esperado



