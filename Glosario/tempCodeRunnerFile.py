    try:
        glo.updateGlosario('Palabra', 'name')
        print(glo.Glosario_List) 
    except ValueError as e:
        print("Error! ")