# Dicionário para mapear as características às espécies
animais = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

# Entrada do usuário
caracteristica1 = input().strip()
caracteristica2 = input().strip()
caracteristica3 = input().strip()

# Busca no dicionário
resultado = animais[caracteristica1][caracteristica2][caracteristica3]

# Saída
print(resultado)
