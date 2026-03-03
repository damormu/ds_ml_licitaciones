import pandas as pd

def data_report(df):
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)

    return concatenado

def tratar_strings(df):

    df.columns = df.columns.str.replace(r"['’`´]", "", regex=True)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.replace(r"['’`´]", "", regex=True).str.lower()
    
    return df

def similitud_con_target(df, y, cols, pipeline_steps):
    
    for col in cols:
        porcentaje = len(df[df[col] == y])*100/len(df)
        print(f"Porcentage coincidencia {col} / {y.name}: {porcentaje:.2f}%")

        if porcentaje > 95:
            print(f"Se elimina columna: {col}")
            df.drop(columns=[col], inplace=True)
            pipeline_steps.append(lambda df, col=col: df.drop(col, axis=1))
    

def eliminar_columnas_nulas(df, pipeline_steps, threshold=0.6):

    # Encontrar columnas totalmente nulas o con todos los strings vacíos
    columnas_nulas = [col for col in df.columns 
                            if df[col].isnull().all() or (df[col].astype(str) == '').all()]
    
    if len(columnas_nulas) > 0:
        print(f"Total de columnas vacías: {len(columnas_nulas)}\n")
        for col in columnas_nulas:
            print(f"Se elimina columna: {col}")

        df.drop(columns=columnas_nulas, inplace=True)

        for col in columnas_nulas:
            pipeline_steps.append(lambda df, col=col: df.drop(col, axis=1))

def tratar_cardinalidad(df, pipeline_steps, threshold=0.6):
    
    l = len(df)

    # Encontrar columnas con cardinalidad 0 o mayor que el umbral
    df_report = data_report(df).reset_index()

    columnas_card_0= df_report['COL_N'][df_report['CARDIN (%)'] == 0].tolist()
    columnas_card_max = df_report['COL_N'][df_report['CARDIN (%)'] > threshold*100].tolist()

    columnas_cardinalidad = columnas_card_0 + columnas_card_max

    if len(columnas_cardinalidad) > 0:
        print(f"Total de columnas con cardinalidad 0 o mayor que {threshold*100}%: {len(columnas_cardinalidad)}\n")
        
        for col in columnas_cardinalidad:
            valores_unicos = df[col].nunique()
            porcentaje_cardin = valores_unicos*100/l
            print(f"Se elimina columna: {col} ({valores_unicos} valores únicos, {porcentaje_cardin:.2f}%)")
            pipeline_steps.append(lambda df, col=col: df.drop(col, axis=1))

        df.drop(columns=columnas_cardinalidad, inplace=True)

def otros(df, col, val='Otros'):

    df[col] = df[col].apply(lambda x: val if str(x) == '' else x)

    return df

def tratar_columnas_con_algun_blanco(df, pipeline_steps, val='Otros'):

    l = len(df)
    columnas_objeto = df.select_dtypes(include=['object']).columns.tolist()

    if len(columnas_objeto) > 0:
        print(f"Columnas con algún blanco:\n")
   
        # columnas con algún valor en blanco
        for col in columnas_objeto:
            if (df[col].astype(str) == '').any():
                nulos = len(df[df[col].astype(str) == ''])
                porcentaje = nulos*100/l

                if porcentaje > 70:
                    print(f"Se elimina columna: {col} {nulos} {porcentaje:.2f}%")
                    df.drop(columns=col, inplace=True)
                    pipeline_steps.append(lambda df, col=col: df.drop(col, axis=1))
                else:
                    print(f"Columna con blancos: {col} {nulos} {porcentaje:.2f}%")
                    otros(df, col, val)
                    pipeline_steps.append(lambda df, col=col: otros(df, col, val))

def tratar_columnas_con_algun_cero(df, pipeline_steps):

    l = len(df)
    columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()

    if len(columnas_numericas) > 0:
        print(f"Columnas con algún cero:\n")
   
        # columnas con algún valor cero
        for col in columnas_numericas:
            if (df[col] == 0).any():
                ceros = len(df[df[col] == 0])
                porcentaje = ceros*100/l

                if porcentaje > 70:
                    print(f"Se elimina columna: {col} {ceros} {porcentaje:.2f}%")
                    df.drop(columns=col, inplace=True)
                    pipeline_steps.append(lambda df, col=col: df.drop(col, axis=1))
                else:
                    print(f"Columna con ceros: {col} {ceros} {porcentaje:.2f}%")


def tratar_codi_cpv(df):

    col = 'Codi CPV'

    col_div = col + '_div'
    df[col_div] = df[col].apply(lambda x: x[:2] if isinstance(x, str) and x.strip() != '' else '0').astype('int')

    col_grp = col + '_grp'
    df[col_grp] = df[col].apply(lambda x: x[:-2] if isinstance(x, str) and x.strip() != '' else '0').astype('int')

    df.drop(columns=[col], inplace=True)
                    
    return df

def fechas(df):

    columnas_fecha = [col for col in df.columns if col.startswith('Data')]

    for col in columnas_fecha:
        df["datetime_" + col] = pd.to_datetime(df[col], format='%d/%m/%Y', errors='coerce')

        # Miramos si hay nulos en el nuevo campo
        mask = df["datetime_" + col].isnull()
        df_nulos = df[col][mask]
        l = len(df_nulos)

        if l > 0:
            indexs = df_nulos.index.to_list()

            print(f"\nFechas incongruentes {col}: \n{df_nulos}")
            
            # Solucionamos las columnas incongruentes
            for idx in indexs:
                source = df.at[idx, col]
                fixed = source.replace('/00', '/20')
                df.at[idx, col] = fixed
                df.at[idx, "datetime_" + col] = pd.to_datetime(fixed, format='%d/%m/%Y', errors='coerce')

            # Miramos si hay nulos en el nuevo campo
            mask = df["datetime_" + col].isnull()
            df_nulos = df[col][mask]
            l = len(df_nulos)

            if l == 0:
                print(f"\nFechas corregidas: {col}")
                for idx in indexs:
                    print(f"{df.at[idx, col]}")
            else:
                print('error')

        df[col] = df["datetime_" + col]
        df.drop(columns=["datetime_" + col], inplace=True)

    return df

def columnas_dt(df, col):
    
    # Añadimos las columnas dia, mes y año de las fechas y eliminamos la columna fecha
    df["day_" + col] = df[col].dt.day
    df["month_" + col] = df[col].dt.month
    df["year_" + col] = df[col].dt.year

    return df

def duracion(df, col_ini, col_fin):
    
    if col_ini in df.columns:
        columnas_dt(df, col_ini)

    if col_fin in df.columns:
        columnas_dt(df, col_fin)      
    
    if (col_fin in df.columns and col_ini in df.columns):

        # Calcular la diferencia de días siempre positiva
        df['durada_dies'] = (
            df.apply(lambda row: (row[col_fin] - row[col_ini]).days if row[col_fin] >= row[col_ini] else (row[col_ini] - row[col_fin]).days, axis=1)
        )

    df.drop(columns=[col_ini, col_fin], inplace=True)

    return df


def similitud_con_exercici(df, pipeline_steps):

    col = 'Exercici'
    l = len(df)

    columnas_year = [col_year for col_year in df.columns if col_year.startswith('year_Data')]
    for col_year in columnas_year:
        coincidencias = len(df[df[col] == df[col_year]])
        porcentaje = coincidencias*100/l
        if porcentaje == 100:
            print(f"Se elimina la columna {col_year} Porcentage coincidencia con {col} : {porcentaje:.2f}%")
            df.drop(columns=[col_year], inplace=True)
            pipeline_steps.append(lambda df, col=col_year: df.drop(col, axis=1))
        # else:
        #     print(col_year, porcentaje)

def mediana(df, col):
    
    if col in df.columns:
        mediana = df[col].median()
        df.loc[df[col] <= 0, col] = mediana
    
    return df


    
        

                   



