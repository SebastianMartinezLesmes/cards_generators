import os

def limpiar_carpeta_data():
    proyecto_root = os.path.dirname(os.path.dirname(__file__))
    carpeta_data = os.path.join(proyecto_root, "data")

    if not os.path.exists(carpeta_data):
        print("⚠️ La carpeta 'data' no existe.")
        return

    archivos_eliminados = 0
    for archivo in os.listdir(carpeta_data):
        ruta = os.path.join(carpeta_data, archivo)
        if os.path.isfile(ruta):
            os.remove(ruta)
            archivos_eliminados += 1
            print(f"🗑️ Eliminado: {archivo}")

    print(f"\n✅ {archivos_eliminados} archivos eliminados de la carpeta 'data'.")

if __name__ == "__main__":
    limpiar_carpeta_data()
