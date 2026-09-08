"""Jogo de Adivinhação de Número.

O computador sorteia um número secreto e o jogador tenta adivinhar,
recebendo dicas de "maior" ou "menor" a cada tentativa.
"""

import random

FAIXAS_DIFICULDADE = {
    "1": ("Fácil", 1, 50, 10),
    "2": ("Médio", 1, 100, 7),
    "3": ("Difícil", 1, 200, 5),
}


def escolher_dificuldade() -> tuple:
    print("Escolha a dificuldade:")
    for chave, (nome, minimo, maximo, tentativas) in FAIXAS_DIFICULDADE.items():
        print(f"  {chave} - {nome} (1 a {maximo}, {tentativas} tentativas)")

    while True:
        escolha = input("Digite o número da dificuldade: ").strip()
        if escolha in FAIXAS_DIFICULDADE:
            return FAIXAS_DIFICULDADE[escolha]
        print("Opção inválida. Tente novamente.")


def ler_palpite(minimo: int, maximo: int) -> int:
    while True:
        entrada = input(f"Seu palpite ({minimo}-{maximo}): ").strip()
        if not entrada.lstrip("-").isdigit():
            print("Digite um número válido.")
            continue

        palpite = int(entrada)
        if palpite < minimo or palpite > maximo:
            print(f"O número deve estar entre {minimo} e {maximo}.")
            continue

        return palpite


def jogar() -> bool:
    """Executa uma partida. Retorna True se o jogador venceu."""
    nome, minimo, maximo, max_tentativas = escolher_dificuldade()
    numero_secreto = random.randint(minimo, maximo)

    print(f"\nDificuldade: {nome}")
    print(f"Adivinhe o número entre {minimo} e {maximo}.")
    print(f"Você tem {max_tentativas} tentativas.\n")

    for tentativa in range(1, max_tentativas + 1):
        palpite = ler_palpite(minimo, maximo)

        if palpite == numero_secreto:
            print(f"\nParabéns! Você acertou em {tentativa} tentativa(s)!")
            return True

        dica = "maior" if palpite < numero_secreto else "menor"
        restantes = max_tentativas - tentativa
        print(f"O número secreto é {dica} que {palpite}. "
              f"Tentativas restantes: {restantes}\n")

    print(f"\nSuas tentativas acabaram. O número secreto era {numero_secreto}.")
    return False


def main() -> None:
    print("=== Jogo de Adivinhação de Número ===\n")
    vitorias = 0
    partidas = 0

    while True:
        partidas += 1
        if jogar():
            vitorias += 1

        print(f"\nPlacar: {vitorias} vitória(s) em {partidas} partida(s).")
        de_novo = input("\nJogar novamente? (s/n): ").strip().lower()
        if de_novo != "s":
            print("\nAté a próxima!")
            break
        print()


if __name__ == "__main__":
    main()
