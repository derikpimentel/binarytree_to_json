# Simula um arquivo JSON carregado
JSON_file = {
    "left": {
        "left": {
            "left": "Status",
            "root": "=",
            "right": "'True'"
        },
        "root": "AND",
        "right": {
            "left": "Activated",
            "root": "=",
            "right": "1"
        }
    },
    "root": "OR",
    "right": {
        "left": "Name",
        "root": "LIKE",
        "right": "'Derik%'"
    }
}

"""
Leitura em ordem (in-order):
Visita a subárvore esquerda, depois o nó raiz e, por último, a subárvore direita.
"""
def in_order(node):
    # Visitando os nós da esquerda
    aux_l = node["left"]
    left = in_order(aux_l) if isinstance(aux_l, dict) else aux_l

    root = node["root"] # Visitando o nó raiz

    # Visitando os nós da direita
    aux_r = node["right"]
    right = in_order(aux_r) if isinstance(aux_r, dict) else aux_r

    return f"{left} {root} {right}"

# Estrutura de execução
if __name__ == "__main__":
    print(in_order(JSON_file))