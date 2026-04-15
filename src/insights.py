from analyzer import gasto_por_dia, gasto_por_categoria


def dia_mayor_gasto(df):
    gastos = gasto_por_dia(df)
    dia = gastos.idxmax()
    monto = gastos.max()
    return f"El día que más gastaste fue el {dia} con ${monto}."


def categoria_mayor_gasto(df):
    gastos = gasto_por_categoria(df)
    categoria = gastos.idxmax()
    monto = gastos.max()
    return f"Tu mayor gasto es en {categoria} con ${int(monto)}."

def mayor_gasto_individual(df):
    idx = df["monto"].idxmax()
    fila = df.loc[idx]
    monto = fila["monto"]
    categoria = fila["categoria"]
    fecha = fila["fecha"].strftime("%Y-%m-%d") # recorta el tiempo
    detalle = fila["detalle"]
    return f"Tu mayor gasto fue en {categoria} el día {fecha}. Gastaste ${int(monto)} en {detalle}."

def top_categorias(df, n=3):
    gasto = gasto_por_categoria(df)
    ordenado = gasto.sort_values(ascending=False)
    ordenado = ordenado.head(n)
    resultado = 'Categorias con mas gastos:\n'
    for i, (cat, monto) in enumerate(ordenado.items(), 1):
        resultado += f'{i}. {cat}: {int(monto)}\n'
    return resultado


