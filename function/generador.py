import random
import os

def luhn_generar_digito(numero_base):
    total = 0
    invertir = numero_base[::-1]
    for i, digito in enumerate(invertir):
        d = int(digito)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return str((10 - total % 10) % 10)

def generar_tarjeta(tipo):
    prefijos = {
        "visa": ["4", "450799", "402400", "451416", "454883"],
        "mastercard": ["51", "52", "53", "54", "55", "2221", "2222", "2223", "2720", "540265", "525248"],
        "amex": ["34", "37"],
        "discover": ["6011", "622126", "622925", "644", "645", "646", "647", "648", "649", "65"],
        "diners": ["300", "301", "302", "303", "304", "305", "36", "38"],
        "jcb": ["3528", "3589"],
        "unionpay": ["62"]
    }

    longitudes = {
        "visa": 16,
        "mastercard": 16,
        "amex": 15,
        "discover": 16,
        "diners": 14,
        "jcb": 16,
        "unionpay": 16
    }

    tipo = tipo.lower()
    prefijo = random.choice(prefijos[tipo])
    longitud_base = longitudes[tipo] - 1
    numero_base = prefijo + ''.join(random.choices("0123456789", k=longitud_base - len(prefijo)))
    return numero_base + luhn_generar_digito(numero_base)

def generar_lista_tarjetas(cantidad=50):
    tipos = ["visa", "mastercard", "amex", "discover", "diners", "jcb", "unionpay"]

    tarjetas = [generar_tarjeta(random.choice(tipos)) for _ in range(cantidad)]

    # 🟩 Guardar archivo en carpeta "data", una carpeta arriba
    proyecto_root = os.path.dirname(os.path.dirname(__file__))
    archivo_path = os.path.join(proyecto_root, "data", "tarjetas.txt")

    with open(archivo_path, "w") as f:
        for tarjeta in tarjetas:
            f.write(tarjeta + "\n")
    print(f"✅ Se generaron {cantidad} tarjetas en: {archivo_path}")

if __name__ == "__main__":
    generar_lista_tarjetas()
