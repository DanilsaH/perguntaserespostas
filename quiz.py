# Dicionário com as perguntas e opções de resposta

perguntas = {
    1: {
        "pergunta": "Quais serviços forneço?",
        "opcoes": [
            "1. Comunicação & Marketing",
            "2. Desenvolvimento web & Comunicação",
            "3. Desenvolvimento & Marketing digital"
        ],
        "correta": 3
    },
    2: {
        "pergunta": "Quais empresas já trabalhei?",
        "opcoes": [
            "1. ENDE, EPAL, Sonangol",
            "2. Pumangol, Lactiangol",
            "3. Unitel, Emted, Yoyo, Zap, Angomart"
        ],
        "correta": 3
    },
    3: {
        "pergunta": "Qual é a estimativa de valores que aceito como pagamento?",
        "opcoes": [
            "1. 70 mil Kz até 500 mil Kz",
            "2. 200 mil Kz até 500 milhões Kz",
            "3. 10 mil Kz até 500 mil Kz"
        ],
        "correta": 2
    },
    4: {
        "pergunta": "Propostas de Emprego",
        "opcoes": [
            "1. Sim, presencial",
            "2. Apenas híbrido",
            "3. Híbrido / remoto"
        ],
        "correta": 3
    },
    5: {
        "pergunta": "O atendimento é por:",
        "opcoes": [
            "1. Marcação (formulário)",
            "2. Preferência",
            "3. Contato livre"
        ],
        "correta": 1
    }
}

# Função para exibir o quiz e calcular a pontuação
def executar_quiz():
    pontuacao = 0
    print("Bem-vindo ao Quiz sobre Freelance de Desenvolvimento e Marketing Digital!\n")
    
    for id_pergunta, dados in perguntas.items():
        print(f"{id_pergunta}. {dados['pergunta']}")
        for opcao in dados["opcoes"]:
            print(opcao)
        
        resposta = int(input("Escolha a opção correta (1, 2 ou 3): "))
        
        if resposta == dados["correta"]:
            print(f"✔️ Resposta correta! Parabéns! Você ganhou um desconto de {score} !")
            pontuacao += 1 

        else:
            print(f"❌ Resposta incorreta! Você obteve aumento de {score}")

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas !")

# Executar o quiz
executar_quiz()





