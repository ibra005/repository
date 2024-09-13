def output_data(df):
    
    fg = '34' # цвет шрифта
    bk = '43' # цвет фона
    color = f'\033[{fg};{bk};5m'
    
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
    
    massage = 'Выведем описательную статистику датасета'
    leng = round((120 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print()
    print(color + massage + '\033[0m')
    display(df.describe())
    
    massage = 'Выведем явные дубликаты'
    leng = round((120 - len(massage)) / 2)
    massage = ((' ' * leng) + massage + (' ' * leng))[:120]
    print(color + massage + '\033[0m')
    display(df[df.duplicated()])
