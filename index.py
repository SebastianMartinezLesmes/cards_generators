import os
from datetime import datetime

# Importar las funciones directamente
from function.clear_data import limpiar_carpeta_data
from function.generador import generar_lista_tarjetas
from function.validator import validar_tarjetas_archivo
from function.country import generar_info_card
from function.clear_cache import eliminar_cache

def guardar_log(contenido):
    log_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "log.txt")

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"\n=== {datetime.now()} ===\n")
        log_file.write(contenido)
        log_file.write("\n")

    print(f"📝 Log guardado en: {log_path}")

if __name__ == "__main__":
    print("\n🧹 Limpiando archivos anteriores...")
    limpiar_carpeta_data()

    print("\n🃏 Generando nuevas tarjetas...")
    generar_lista_tarjetas(cantidad=150)

    print("\n✅ Validando tarjetas...")
    salida_validador, validas, invalidas = validar_tarjetas_archivo()
    print("\n📋 Resultado del validador:")
    print(salida_validador)

    total = validas + invalidas
    resumen = f"\nResumen:\n- Total: {total}\n- Válidas: {validas}\n- Inválidas: {invalidas}\n"
    print(resumen)

    print("🌍 Consultando BIN y agrupando por país...")
    generar_info_card()

    guardar_log(salida_validador + resumen)

    print("\n📦 Limpiando caché de Python...")
    eliminar_cache()