def standaardprijs(afstandKM):
    if afstandKM > 0 < 50:
        bedrag = 0.80 * afstandKM
        return (bedrag)
    elif afstandKM >= 50:
        bedrag = 15 + 0.60 * afstandKM
        return (bedrag)
    elif afstandKM < 0:
        bedrag = 0
        return (bedrag)


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'Ja' or weekendrit == 'ja':
        if leeftijd < 12 or leeftijd >= 65:
            bedrag = standaardprijs(afstandKM) * 0.65  # 26
            print('Uw ritbedrag bedraagt: ', bedrag, 'euro.')
        elif leeftijd > 12 or leeftijd < 65:
            bedrag = standaardprijs(afstandKM) * 0.6  # 24
            print('Uw ritbedrag bedraagt: ', bedrag, 'euro.')
        else:
            print('Er is iets fout gegaan, probeer het opnieuw.')
    else:
        if leeftijd < 12 or leeftijd >= 65:
            bedrag = standaardprijs(afstandKM) * 0.7  # 28
            print('Uw ritbedrag bedraagt: ', bedrag, 'euro.')
        elif leeftijd > 12 or leeftijd < 65:
            bedrag = standaardprijs(afstandKM) * 1.0  # 40
            print('Uw ritbedrag bedraagt: ', bedrag, 'euro.')
        else:
            print('Er is iets fout gegaan, probeer het opnieuw.')


ritprijs(11,'ja',50)
ritprijs(12,'ja',50)
ritprijs(64,'ja',50)
ritprijs(65,'ja',50)
ritprijs(11,'nee',50)
ritprijs(12,'nee',50)
ritprijs(64,'nee',50)
ritprijs(65,'nee',50)