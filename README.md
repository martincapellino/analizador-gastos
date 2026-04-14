# Sistema de Análisis de Gastos

## Objetivo 
Desarrollar un sistema simple que permita al usuario cargar sus gastos personales mediante un archivo CSV y obtener un análisis de sus hábitos de consumo

---

## Usuarios
-Usuario General (persona que desea analizar y optimizar sus gastos)

---

## Entradas del sistema
El sistema recibirá un archivo .csv con los gastos del usuario, especificando en cada uno:
fecha,categoria,detalle,monto
Por ejemplo: 2026-04-01,comida,delivery,2500

Reglas:
-Fecha en formato YYYY-MM-DD
-La categoría la determina el usuario
-El detalle lo determina el usuario
-Monto numérico (positivo o negativo)

---

## Salidas del sistema
-Cálculo del gasto total
-Análisis de gastos por categoría
-Identificación de patrones de consumo (por ejemplo, días con mayor gasto)
-Insights simples sobre posibles mejoras en los hábitos financieros.

---

## Requerimientos funcionales
El sistema deberá:

1. Cargar un archivo CSV de gastos del usuario
2. Calcular el gasto total y por categoría
3. Identificar patrones de consumo
4. Generar insights simples

---

## Requerimientos no funcionales
-Código organizado en módulos
-Uso de Python con librerías como NumPy y Pandas
-Fácil de mantener y escalar
-Ejecución simple desde 'main.py'
-Manejo básico de errores en lectura de datos


