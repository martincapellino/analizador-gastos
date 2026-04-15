# Sistema de Análisis de Gastos

## Descripción 
Sistema simple que permita al usuario cargar sus gastos personales mediante un archivo CSV y obtener un análisis de sus hábitos de consumo.

---

## Objetivo

El objetivo del proyecto es practicar:
-Manipulación de datos con Pandas
-Organización de código en módulos
-Principios básicos de ingeniería de software
-Generación de insights a partir de datos reales

---

## Estructura del proyecto

analizador-gastos/
│
├── data/
│ └── gastos.csv
│
├── src/
│ ├── loader.py
│ ├── analyzer.py
│ ├── insights.py
│ └── main.py
│
└── README.md

---

## Entradas del sistema

El sistema recibirá un archivo .csv con los gastos del usuario, con el siguiente formato:
fecha,categoria,detalle,monto
Por ejemplo: 2026-04-01,comida,delivery,2500

Reglas:
-Fecha en formato YYYY-MM-DD
-La categoría la determina el usuario
-El detalle lo determina el usuario
-Monto numérico (positivo o negativo)

---

## Salidas del sistema

### Análisis básico
-Gasto total
-Gasto por categoría
-Gasto por día de la semana

### Insights generados
-Día de mayor gasto
-Categoría con mayor consumo
-Mayor gasto en específico
-Top categorías de gasto

---

## Ejecución
```bash
python src/main.py
```

---

## Tecnologías utilizadas
-Python
-Numpy
-Pandas

---

## Estado del proyecto
Versión inicial. 
En desarrollo con mejoras progresivas.

---

## Aprendizajes del proyecto
-Separación en módulos (loader/analyzer/insights)
-Uso de Pandas para análisis de datos
-Manipulación de Series y DataFrames
-Buenas prácticas de estructura de proyectos en Python
-Posibilidad de utilizar mi conocimiento de Ingeniería de Software



