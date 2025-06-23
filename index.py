import subprocess
import os
from datetime import datetime

def ejecutar_script_y_capturar(ruta_script):
    print(f"\n▶️ Ejecutando: {ruta_script}")
    resultado = subprocess.run(["python", ruta_script], capture_output=True, text=True)
    return resultado.stdout

def guardar_log(contenido):
    log_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "log.txt")

    with open(log_path, "a") as log_file:
        log_file.write(f"\n=== {datetime.now()} ===\n")
        log_file.write(contenido)
        log_file.write("\n")

    print(f"📝 Log guardado en: {log_path}")

def contar_validas(salida):
    lineas = salida.strip().split("\n")
    total = len(lineas)
    print(f"🧾 Conteo de líneas capturadas: {len(lineas)}") 
    validas = sum(1 for l in lineas if "✅" in l)
    invalidas = total - validas
    return total, validas, invalidas

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    clearner_path = os.path.join(base_dir, "function", "clear_data.py")
    generador_path = os.path.join(base_dir, "function", "generador.py")
    validador_path = os.path.join(base_dir, "function", "validator.py")
    info_card_path = os.path.join(base_dir, "function", "country.py")

    # 🧹 Limpiar archivos previos
    ejecutar_script_y_capturar(clearner_path)

    # 🃏 Generar nuevas tarjetas
    ejecutar_script_y_capturar(generador_path)

    # ✅ Validar tarjetas generadas
    salida_validador = ejecutar_script_y_capturar(validador_path)
    print("\n📋 Resultado del validador:")
    print(salida_validador)

    # 📊 Resumen de validación
    total, validas, invalidas = contar_validas(salida_validador)
    resumen = f"\nResumen:\n- Total: {total}\n- Válidas: {validas}\n- Inválidas: {invalidas}\n"

    # 🌍 Agrupar por país
    salida_info = ejecutar_script_y_capturar(info_card_path)
    print("\n🌍 Resultado de agrupación por país:")
    print(salida_info)

    # 📝 Log final
    print(resumen)
    guardar_log(salida_validador + "\n" + salida_info + resumen)