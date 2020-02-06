
lista = []


campoChaves = ['lista:','nome=','cpf->']

contatos_lista = [{'Yan':'1234-5678','Pedro ': '9999-9999',
                    'Ana': '8765-4321', 'Dados':'8877-7788 STRING: nome= Jose asdas,, ola, adfas'},{'Nan':'1234-5678','Dro': '9999-9999',
                    'Na': '8765-4321', 'Dados':'8877-7788 STRING: cpf-> 4641498555'},{'YA':'1234-5678','Dados': '9999-9999 Comeu Maça na casa __INT: lista: key 10|asdas|asdas10|asdasd  blalbnlaslb ola 124',
                    'AN': '8765-4321', 'Mari':'8877-7788'}]

dicionarioDados = {'lista:':'','nome=':'','cpf->':''}

for item in contatos_lista:
    for chave in campoChaves:
        if item['Dados'].find(chave) >=0:
            if chave == 'lista:':
                dicionarioDados[chave] = item['Dados'].split(chave)[-1].split()[1]
            else:
                dicionarioDados[chave] = item['Dados'].split(chave)[-1].split()[0]


print('Deu certo')

