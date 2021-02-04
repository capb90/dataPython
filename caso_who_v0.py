def caso_who(ruta_archivo_csv: str)-> dict:
    import pandas as pd
    import numpy as np
    tamaño_ruta=len(ruta_archivo_csv)
    if ruta_archivo_csv[tamaño_ruta-4:tamaño_ruta]=='.csv':
        try:
            datos = pd.read_csv(ruta_archivo_csv)
            df_original=pd.DataFrame(datos)
            df_original.date = pd.to_datetime(df_original.date)
            casos_covid = (df_original['total_cases_per_million'] * df_original['population']) / 1000000
            camas = (df_original['hospital_beds_per_thousand'] * df_original['population']) / 1000
            razon = casos_covid / camas
            df_original['razon']=razon
            #df_original=df_original.groupby(['date','continent'])['razon'].mean().unstack()
            df_respuesta = pd.pivot_table(df_original, values='razon', index='date', columns='continent', aggfunc=np.mean)
            df_respuesta.plot()
            dic_salida=df_respuesta.to_dict()
            return  dic_salida
        except:
            return "Error al leer el archivo de datos."

    else:
        return "Extensión inválida."



ruta='https://raw.githubusercontent.com/tikuro/Covid/main/owid-covid-data.csv'
print(caso_who(ruta_csv))
