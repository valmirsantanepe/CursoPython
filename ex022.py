nome = input('Digite seu nome completo: \n').strip()
print('Analizando seu nome.. ')
print('Nome com todas as letras maiusculas: ', nome.upper())
print('Nome com todas as letras minusculas: ', nome.lower())
print('Total de caracteres considerando os espaços: ', len(nome))
print('Total de carcteres sem considerar os espaços: ', len(nome)-nome.count(' '))
print('Seu primeir nome tem {} letras' .format(nome.find(' ')))