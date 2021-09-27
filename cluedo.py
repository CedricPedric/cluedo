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
if ManOfVrouwVraag.lower() == 'man':
    SnorVraag = YesOrNoVraag('Bent u in staat om een snor te groeien?: ')
HaarVraag = input('Welke kleur is uw haar?: ')

AgeCheck = leeftijdVraag >= 18

if acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'geel' and ManOfVrouwVraag in ['Man', 'man', 'MAN'] and HaarVraag.lower() in ['blond', 'geel']:
    print('Je mag op auditie voor de rol van Kolonel van Geelen')

elif acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'wit' and ManOfVrouwVraag.lower() == 'vrouw' and HaarVraag.lower() in ['wit', 'grijs']:
    print('Je mag op auditie voor de rol van Mevrouw de Wit')

elif acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'rood' and ManOfVrouwVraag.lower() == 'vrouw' and HaarVraag.lower() == 'zwart':
    print('Je mag op auditie voor de rol van Rosa Roodhart')

elif (acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'paars' and ManOfVrouwVraag in ['Man', 'man', 'MAN'] and SnorVraag == True
and HaarVraag.lower() == 'grijs'):
    print('Je mag op auditie voor de rol van Professor Pimpel')

elif acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'groen' and ManOfVrouwVraag in ['Man', 'man', 'MAN']:
    print('Je mag op auditie voor de rol van Dominee Groenewoud')

elif acteerDiplomaVraag == True and AgeCheck == True and kleurVraag.lower() == 'blauw' and ManOfVrouwVraag.lower() == 'vrouw' and HaarVraag.lower() == 'bruin':
    print('Je mag op auditie voor de rol van Mevrouw Blaauw van Draet')


else:
    print('Helaas heeft u geen van de rollen :(')
    