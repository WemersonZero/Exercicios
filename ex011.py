larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem a dimenção de {}x{} e a sua área é de {:.3f}'.format(larg, alt, (larg**alt)))
print('Para pinta essa parede, você precisará de {:.4f}L de tinta.'.format((larg**alt)/2))