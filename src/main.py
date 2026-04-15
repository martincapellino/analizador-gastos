from loader import load_data
from analyzer import (total_gasto, gasto_por_categoria, gasto_por_dia)
from insights import (dia_mayor_gasto, categoria_mayor_gasto, mayor_gasto_individual, top_categorias)

def main():
    df = load_data("../data/gastos.csv")
    print('***ANALISIS DE GASTOS***')
    print(f'Gasto total: ${int(total_gasto(df))}\n')
    print(f'Gastos por categoria:\n{gasto_por_categoria(df)}')
    print(f'Dia con mayor gasto:\n{dia_mayor_gasto(df)}')
    print(f'Gastos por dia:\n{gasto_por_dia(df)}')
    print(f'Categoria con mayor gasto:\n{categoria_mayor_gasto(df)}')
    print(f'Mayor gasto individual:\n{mayor_gasto_individual(df)}')
    print(f'Top 3 categorias:\n{top_categorias(df)}')

if __name__ == '__main__':
    main()