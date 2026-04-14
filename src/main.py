from loader import load_data
from analyzer import total_gasto, gasto_por_categoria
from insights import dia_mayor_gasto, categoria_mayor_gasto

df = load_data("../data/gastos.csv")

print(categoria_mayor_gasto(df))