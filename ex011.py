larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimenção de {}x{} e a sua área é de {:.1f}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pinta essa parede, você precisará de {:.1f}L de tinta.'.format(tinta))