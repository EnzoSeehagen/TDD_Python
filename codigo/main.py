from codigo.bytebank import Funcionario

# enzo = Funcionario("Enzo", '31/05/2000', 3000)
# print(enzo.idade())

def teste_idade():
    funcionario_teste = Funcionario("Enzo", "31/05/2000", 2000)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()
