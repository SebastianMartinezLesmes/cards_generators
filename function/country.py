import requests
import os

def obtener_info_bin(bin_num):
    try:
        url = f"https://lookup.binlist.net/{bin_num}"
        headers = {"Accept-Version": "3"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            pais = data.get("country", {}).get("name", "Desconocido")
            banco = data.get("bank", {}).get("name", "Banco no identificado")
            esquema = data.get("scheme", "Desconocido")
            tipo = data.get("type", "Desconocido")
            return {
                "pais": pais,
                "banco": banco,
                "esquema": esquema.capitalize(),
                "tipo": tipo.capitalize() if tipo else "Desconocido"
            }
        else:
            return {"pais": "Desconocido"}
    except Exception as e:
        return {"pais": "Error de conexión"}

def agrupar_por_pais(validas):
    agrupadas = {}
    for tarjeta in validas:
        tarjeta = tarjeta.strip()
        if not tarjeta:
            continue

        bin_info = obtener_info_bin(tarjeta[:6])
        pais = bin_info.get("pais", "Desconocido")
        banco = bin_info.get("banco", "Banco no identificado")
        esquema = bin_info.get("esquema", "Desconocido")
        tipo = bin_info.get("tipo", "Desconocido")

        info_formateada = f"✅ {tarjeta} | {banco} - {esquema} - {tipo}"

        if pais not in agrupadas:
            agrupadas[pais] = []
        agrupadas[pais].append(info_formateada)

    return agrupadas

def generar_info_card():
    proyecto_root = os.path.dirname(os.path.dirname(__file__))
    archivo_validas = os.path.join(proyecto_root, "data", "validas.txt")
    archivo_salida = os.path.join(proyecto_root, "data", "info_card.txt")

    if not os.path.exists(archivo_validas):
        print("❌ No se encontró validas.txt. Ejecuta primero el validador.")
        return

    with open(archivo_validas, "r") as f:
        tarjetas_validas = f.readlines()

    agrupadas = agrupar_por_pais(tarjetas_validas)

    with open(archivo_salida, "w", encoding="utf-8") as f:
        for pais, tarjetas in agrupadas.items():
            f.write(f"País: {pais}\n")
            for tarjeta in tarjetas:
                f.write(tarjeta + "\n")
            f.write("-----------------------------------\n")

    print(f"✅ Archivo generado en: {archivo_salida}")

if __name__ == "__main__":
    generar_info_card()
