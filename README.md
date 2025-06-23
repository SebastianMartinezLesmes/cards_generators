# 💳 Card Generator & Validator

Este proyecto genera tarjetas de crédito de forma aleatoria, las valida mediante el algoritmo de Luhn y consulta información del país y banco emisor a través de la API de [Binlist](https://binlist.net/). Toda la información se organiza y se guarda en archivos dentro de una carpeta `data/`.

## ✅ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente:

- Python 3.7 o superior
- Librería `requests` instalada:
  ```bash
  pip install requests

## 🗂️ Estructura del proyecto

```
CARDS_GENERATORS/
├── data/                        # Archivos generados automáticamente
│   ├── tarjetas.txt             # Tarjetas generadas
│   ├── validas.txt              # Tarjetas válidas
│   ├── invalidas.txt            # Tarjetas inválidas
│   ├── info_card.txt            # Agrupadas por país (vía Binlist)
│   └── log.txt                  # Registro de ejecución
│
├── function/                    # Lógica principal del sistema
│   ├── clear_data.py            # Limpia la carpeta data
│   ├── generador.py             # Genera tarjetas aleatorias
│   ├── validator.py             # Valida tarjetas usando algoritmo de Luhn
│   └── country.py               # Consulta la API de Binlist y agrupa por país
│
├── index.py                     # Script principal que orquesta todo
├── LICENSE
└── README.md                    # Documentación del proyecto
```

## ⚙️ Funcionamiento del sistema
Para ejecutar todo el flujo automáticamente:

```bash
python index.py
```

El script ejecuta los siguientes pasos en orden:

1. Limpiar la carpeta data/
Ejecuta clear_data.py para eliminar archivos previos.

2. Generar tarjetas
generador.py crea tarjetas aleatorias (Visa, MasterCard, etc.).

3. Validar tarjetas
validator.py filtra las válidas/inválidas con el algoritmo de Luhn.

4. Consultar país y banco
country.py consulta la API pública de Binlist para tarjetas válidas y crea el archivo info_card.txt.

5. Guardar resultados en un log
Todo se documenta en data/log.txt.

## 🔗 Herramientas relacionadas
Si deseas probar con otros validadores y/o generadores de tarjetas, puedes visitar:

👉 [VCC Generator](https://www.vccgenerator.org/)
