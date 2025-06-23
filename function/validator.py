import os

def luhn_verificar(numero):
    total = 0
    invertir = numero[::-1]
    for i, digito in enumerate(invertir):
        d = int(digito)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def validar_tarjetas_archivo():
    proyecto_root = os.path.dirname(os.path.dirname(__file__))
    archivo_path = os.path.join(proyecto_root, "data", "tarjetas.txt")
    validas_path = os.path.join(proyecto_root, "data", "validas.txt")
    invalidas_path = os.path.join(proyecto_root, "data", "invalidas.txt")

    if not os.path.exists(archivo_path):
        return "❌ El archivo tarjetas.txt no existe. Genera primero con generador.py"

    with open(archivo_path, "r") as f:
        tarjetas = f.readlines()

    resultados = []
    tarjetas_validas = []
    tarjetas_invalidas = []

    for tarjeta in tarjetas:
        tarjeta = tarjeta.strip()
        if not tarjeta:
            continue
        if luhn_verificar(tarjeta):
            resultados.append(f"✅ {tarjeta} es válida")
            tarjetas_validas.append(tarjeta)
        else:
            resultados.append(f"❌ {tarjeta} NO es válida")
            tarjetas_invalidas.append(tarjeta)

    # Guardar tarjetas válidas e inválidas
    with open(validas_path, "w") as f_validas:
        for v in tarjetas_validas:
            f_validas.write(v + "\n")

    with open(invalidas_path, "w") as f_invalidas:
        for i in tarjetas_invalidas:
            f_invalidas.write(i + "\n")

    return "\n".join(resultados)

if __name__ == "__main__":
    print(validar_tarjetas_archivo())
