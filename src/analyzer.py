def total_gasto(df):
    return df["monto"].sum()

def gasto_por_categoria(df):
    return df.groupby("categoria")["monto"].sum()

def gasto_por_dia(df):
    df_copy = df.copy() #Copia para evitar reiteradas modificaciones
    df_copy["dia"] = df_copy["fecha"].dt.day_name()
    return df_copy.groupby("dia")["monto"].sum().sort_values(ascending=False) #Lo devuelve clasificado y ordenado

