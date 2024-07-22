senha_global = float(input("digite a senha"))

def menu_um():
    print("escolha um dos numeros abaixo")
    
    print('''
    1.cadastro
    2.lista de p cadastradas 
    3.procurar dados
    4.alterar dados 
    5.excluir dados
    0.sair do banco
''')

def cadastro(p):
    senha = float(input("digite a sua senha"))
    if senha != senha_global:
        print("senha incorreta")
        return (senha_global)
    id = input('digite seu id')
    nome = input('digite o seu nome completo')
    idade = int(input('qual a sua idade?'))
    cpf = float(input('digite o seu cpf:'))
    sair = int(input('Deseja sair? [1] para sim ou [2] para não:  '))
    if sair != 1:
        if senha == senha_global:
            return (senha,nome,id,idade,cpf, senha_global)
    
    else:
        print('Continuando cadastro')
    p.append((id, nome, idade, cpf))

def lista_de_pessoas_cadastradas(p):
    if len(p) == 0:
        print('nenhuma pessoa cadastrada')
    else:
        for ps in p:
            id, nome, idade, cpf = p
            print(f'nome{nome}idade{idade}identificador{id}cpf{cpf}')

def buscar(p):
    id_desejado = input('qual o id desejado?')
    for ps in p:
        id, nome, idade, cpf = ps
        if id == id_desejado:
            print(f'pessoa com id {id_desejado}')
            break
        else:
            print(f'pessoa com id{id_desejado} não encontrado')

def excluir_cadastro(p):
    senha_dois = input("para excluir algum cadastro, você precisa digitar a sua senha global")
    identificador_desejado = input('qual o id')
    for pessoa in p:
        identificador, nome, idade, cpf= p
        if id == identificador_desejado:
            print(f'nome:{nome},idade:{idade},id:{identificador},cpf{cpf}')
            excluir = int(input('para excluir,digite 1, e 0 para ignorar'))
            if excluir == 1:
                del pessoa[pessoa.index(p)]
                print(f'Pessoa com id {identificador_desejado} excluida com sucesso')
            break
        else:
            print(f'pessoa com id {identificador_desejado} não encontrada')
        if senha_dois == senha_global:
            return excluir_cadastro
        else :
            print("senha errada")
            return menu_um

def alterar(ps):
    senha_tres = input("para alterar um cadstro,você precisa dgitar a senha global")
    if senha_tres != senha_global:
        print("senha errada:(")
        return menu_um
    id_desejado = input('id?')
    for p in ps:
        identificador, nomr, idade, cpf = p
        if identificador == id_desejado:
            print('nome:{nome},idade:{idade},id:{identificador},cpf:{cpf}')
            nome_novo = input('deseja alterar o nome?')
            nova_idade =int(input('deseja colocar uma nova idade?'))
            novo_cpf = int(input('deseja alterar o cpf?'))
            id_novo = input('digite aqui para colocar o seu novo id')
            confirmar_alteracoes = int(input('para confirmar alterações digite 1, para ignorar digite 0'))
            if confirmar_alteracoes == 1:
                ps[ps.index(p)] = id_novo, nome_novo, nova_idade, novo_cpf
                print(f'nome:{nome_novo},idade:{nova_idade},cpf:{novo_cpf},identifiador{id_novo}')
            break
        else:
            print(f'pessoa com identificador{id_novo} nâo encontrado')

def main():
    ps = []
    opcao = 1
    while  opcao != 0:
        menu_um() 
        opcao = int(input('qual a opção?'))
        if opcao == 1:
            cadastro(ps)
        elif opcao == 2:
            lista_de_pessoas_cadastradas(ps)
        elif opcao == 3:
            buscar(ps)
        elif opcao == 4:
            alterar(ps)
        elif opcao == 5:
            excluir_cadastro(ps)
        elif opcao == 0:
            break
        else:
            print('opção invalida')

main()