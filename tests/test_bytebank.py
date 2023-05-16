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

    def test_quando_nome_recebe_enzo_seehagen_deve_retornar_seehagen(self):
        entrada = "Enzo Seehagen"
        esperado = "Seehagen"

        funcionario_teste = Funcionario(entrada, "31/05/2000", 2000)

        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_salario_deve_ser_reajustado_dez_porcento_a_menos_quando_o_salario_atual_passa_de_cem_mil_reais_por_mes(
            self):
        entrada_nome = "Enzo Seehagen"
        entrada_salaraio = 100000
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "31/05/2000", entrada_salaraio)

        funcionario_teste.reajuste()

        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_salario_deve_ser_reajustado_dez_porcento_a_mais_quando_o_salario_atual_passa_de_dez_mil_reais_por_mes(self):

        entrada = 25000
        esperado = 27500

        funcionario_teste = Funcionario("Enzo Seehagen", "31/05/2000", entrada)

        funcionario_teste.acrecimo()

        resultado = funcionario_teste.salario

        assert resultado == esperado
