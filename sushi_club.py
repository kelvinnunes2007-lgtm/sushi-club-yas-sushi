
clientes = {}

def cadastrar_cliente(nome, email):
    nome = nome.strip()
    email = email.strip().lower()

    if not nome or "@" not in email:
        raise ValueError("Nome ou e-mail invalido")

    if email in clientes:
        raise ValueError("Cliente ja cadastrado")

    clientes[email] = {
        "nome": nome,
        "pontos": 0
    }

    return clientes[email]


def consultar_pontos(email):
    email = email.strip().lower()

    if email not in clientes:
        raise ValueError("Cliente nao encontrado")

    return clientes[email]["pontos"]


if __name__ == "__main__":
    cadastrar_cliente("Cliente Teste", "teste@exemplo.com")
    print("Cliente cadastrado com sucesso!")
    print("Pontos:", consultar_pontos("teste@exemplo.com"))
  
