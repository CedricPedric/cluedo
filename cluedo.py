def YesOrNoVraag(vraag):
    antwoordenTrue = ['yes', 'YES', 'y', 'Yes', 'ja', 'Ja']
    antwoordenFalse = ['no', 'NO', 'n', 'No', 'nee', 'Nee']
    while True:
        antwoord = input(vraag)
        if antwoord in antwoordenTrue:
            return True
        elif antwoord in antwoordenFalse:
            return False

acteerDiplomaVraag = YesOrNoVraag('Heeft u een Acteer Diploma?: ')
leeftijdVraag = int(input('Hoe oud bent u?: '))
kleurVraag = input('Wat is is favorite kleur?: ')
ManOfVrouwVraag = input('Bent u een man of vrouw?: ')
if ManOfVrouwVraag in ['Man', 'man', 'MAN']:
    SnorVraag = YesOrNoVraag('Bent u in staat om een snor te groeien?: ')
else:
    HaarVraag = input('Welke kleur is uw haar?: ')

if acteerDiplomaVraag == True and leeftijdVraag >= 18 and kleurVraag == 'geel' and ManOfVrouwVraag in ['Man', 'man', 'MAN']:
    print('Mr yellow')
elif (acteerDiplomaVraag == True and leeftijdVraag >= 18 and kleurVraag == 'wit' and ManOfVrouwVraag in ['Vrouw', 'vrouw', 'VROUW'] and
 HaarVraag in ['Grijs', 'grijs', 'wit', 'Wit']):
 print('Ms White')
else:
    print('Helaas heeft u geen van de rollen :(')