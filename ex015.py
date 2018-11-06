dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
vlr = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(vlr))