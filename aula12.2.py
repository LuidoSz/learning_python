def pedido_de_namoro():
    resposta = input("Você aceita namorar comigo? (sim/não): ")

    if resposta.lower() == "sim":
        print("eba vagabunda")
    elif resposta.lower() == "não":
        print("se mata")
    else:
        print("digita direito porra.")

pedido_de_namoro()