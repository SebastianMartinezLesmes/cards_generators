import os
import shutil
import stat

def on_rm_error(func, path, exc_info):
    # Cambiar permisos y volver a intentar
    os.chmod(path, stat.S_IWRITE)
    func(path)

def eliminar_cache():
    proyecto_root = os.path.dirname(os.path.dirname(__file__))

    eliminadas = 0
    for root, dirs, files in os.walk(proyecto_root):
        for carpeta in dirs:
            if carpeta == "__pycache__":
                ruta_cache = os.path.join(root, carpeta)
                try:
                    shutil.rmtree(ruta_cache, onerror=on_rm_error)
                    eliminadas += 1
                    print(f"🗑️ Carpeta eliminada: {ruta_cache}")
                except Exception as e:
                    print(f"❌ No se pudo eliminar {ruta_cache}: {e}")

    if eliminadas == 0:
        print("✅ No se encontraron carpetas __pycache__")
    else:
        print(f"✅ Se eliminaron {eliminadas} carpetas __pycache__")

if __name__ == "__main__":
    eliminar_cache()
