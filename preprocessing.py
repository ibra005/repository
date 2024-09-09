def pprocess(df):
    print('\033[34mВыведем данные из датасета\033[0m')
    display(df)
   
    print('\033[34mВыведем общую информацию о датасете\033[0m')
    print()
    df.info()
    
    print()
    print('\033[34mВыведем описание датасета\033[0m')
    display(df.describe())
    
    print('\033[34mВыведем дубли\033[0m')
    display(df[df.duplicated()])
