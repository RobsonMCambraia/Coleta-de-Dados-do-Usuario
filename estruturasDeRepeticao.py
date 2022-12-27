nome = []
idade = []
sexo = []
profissão = []
salario = []
estado_civil = []
continuar = '1'
contador = 0
while True:

  while True:
    if contador > 0:
      continua = input('Deseja cadastrar outra pessoa?\n 1 - SIM\n 2 - NÃO\n')
    else:
      continua = input('Deseja realizar um cadastro?\n 1 - SIM\n 2 - NÃO\n')

    if continua == '1':
      contador += 1
      continuar == '1'
      print('Cadastre um usuário:')
      break
    elif continua != '1' and continua != '2':
      print('Diite um valor válido!')
    else:
      continuar = '2'
      break

  if continuar == '1':
    while True:
      nome_users = input('Digite seu nome completo:\t').upper().lstrip(' ')
      if len(nome_users) > 3:
        nome.append(nome_users)
        break
      else:
        print('Insira um nome com mais de 3 caracteres!')

    while True:
      idade_users = str(input('Digite a sua idade em anos:\t')).lstrip('0').lstrip(' ')
      if idade_users.isnumeric() == True:
        idade_users = int(idade_users)

        if idade_users <= 150:
          idade.append(idade_users)
          break
        else:
            print('Insira uma idade válida!')
      else:
        print('Insira uma idade válida!')

    while True:
      sexo_users = str(input('Digite seu sexo (Masculino/Feminino):\t')).upper()

      if sexo_users == 'MASCULINO' or sexo_users == 'FEMININO':
        sexo.append(sexo_users)
        break
      else:
        print('Diite um sexo válido!')

    while True:
      profissão_users = str(input('Qual sua atual ocupação profissão?\t')).upper().lstrip(' ')

      if len(profissão_users) > 3:
        profissão.append(profissão_users)
        break
      else:
        print('Digite uma profissão válida!')

    while True:
      salario_users = str(input('Qual o valor do seu salário?\t'))

      if salario_users.isnumeric() == True:
        salario_users = float(salario_users)
        if salario_users > 0:
          salario.append(salario_users)
          break
        else:
          print('Digite um salário válido!')      
      else:
        print('Digite um salário válido!')

    while True:
      civil_users = str(input('Qual o seu estado civil (Solteiro/Casado/Viúvo/Divorciado)?')).upper()

      if civil_users == 'SOLTEIRO' or civil_users == 'CASADO' or civil_users == 'VIÚVO' or civil_users == 'VIUVO' or civil_users == 'DIVORCIADO':
        estado_civil.append(civil_users)
        break
      else:
        print('Digite um estado civil válido! ')
  else:
    print(f'Cadastros feitos:\t{contador}\n')

    for prints in range(len(nome)):
      print(f'Usuário: {nome[prints]}')
      print(f'Idade: {idade[prints]}')
      print(f'Sexo: {sexo[prints]}')
      print(f'Profissão: {profissão[prints]}')
      print(f'Salário: R$ {salario[prints]}')
      print(f'Estado Civil: {estado_civil[prints]}\n')

    print('Encerrando sistema...')
    break
