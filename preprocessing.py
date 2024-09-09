def output_data(df):
    
    fg = '32'
    bk = '43'
    color = '\033[' + fg + ';' + bk +';5m'
    
    massage = 'Выведем данные из датасета'
    leng = round((120 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print(color + massage + '\033[0m')
    display(df)
    
    massage = 'Выведем общую информацию о датасете'
    leng = round((121 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print(color + massage + '\033[0m')
    print()
    df.info()
    
    massage = 'Выведем описание датасета'
    leng = round((120 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print()
    print(color + massage + '\033[0m')
    display(df.describe())
    
    massage = 'Выведем описание датасета'
    leng = round((120 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print(color + massage + '\033[0m')
    display(df[df.duplicated()])
