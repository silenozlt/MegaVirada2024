import random

class MegaSenaGenerator:
    def __init__(self):
        self.historico_mega_virada = {
            2023: [24, 37, 45, 46, 53, 58],
            2022: [4, 5, 10, 34, 58, 59],
            2021: [12, 15, 23, 32, 33, 46],
            2020: [17, 20, 22, 35, 41, 42],
            2019: [3, 35, 38, 40, 57, 58],
            2018: [5, 10, 12, 18, 25, 33],
            2017: [3, 6, 10, 17, 34, 37],
            2016: [5, 11, 22, 24, 51, 53],
            2015: [2, 18, 31, 42, 51, 56],
            2014: [1, 5, 11, 16, 20, 56],
            2013: [20, 30, 36, 38, 47, 53],
            2012: [14, 32, 33, 36, 41, 52],
            2011: [3, 4, 29, 36, 45, 55],
            2010: [2, 10, 34, 37, 43, 50],
            2009: [10, 27, 40, 46, 49, 58],
            2008: [1, 11, 26, 51, 59, 60],
            2007: [3, 4, 6, 22, 37, 58],
            2006: [1, 8, 15, 45, 50, 53],
            2005: [2, 13, 25, 29, 38, 55],
            2004: [9, 22, 31, 37, 56, 59]
        }
        
        self.precos = {
            6: 5.00,
            7: 35.00,
            8: 140.00,
            9: 420.00
        }
        
    def analisa_frequencia(self):
        numeros_frequentes = {}
        for numeros in self.historico_mega_virada.values():
            for num in numeros:
                numeros_frequentes[num] = numeros_frequentes.get(num, 0) + 1
        return numeros_frequentes
    
    def gera_jogos(self, qtd_jogos, qtd_numeros):
        if qtd_numeros < 6 or qtd_numeros > 9:
            raise ValueError("A quantidade de números deve estar entre 6 e 9")
            
        frequencia = self.analisa_frequencia()
        jogos = []
        
        for _ in range(qtd_jogos):
            pesos = [frequencia.get(i, 0) + 1 for i in range(1, 61)]
            jogo = sorted(random.choices(range(1, 61), weights=pesos, k=qtd_numeros))
            
            while len(set(jogo)) != qtd_numeros:
                jogo = sorted(random.choices(range(1, 61), weights=pesos, k=qtd_numeros))
            
            jogos.append(jogo)
            
        return jogos
    
    def calcula_valor(self, qtd_jogos, qtd_numeros):
        valor_unitario = self.precos[qtd_numeros]
        valor_total = valor_unitario * qtd_jogos
        return valor_unitario, valor_total

def main():
    gerador = MegaSenaGenerator()
    
    while True:
        try:
            print("\nValores por jogo:")
            for num, valor in gerador.precos.items():
                print(f"{num} números: R$ {valor:.2f}")
                
            qtd_jogos = int(input("\nQuantos jogos você quer gerar? "))
            qtd_numeros = int(input("Quantos números por jogo (6 a 9)? "))
            
            valor_unitario, valor_total = gerador.calcula_valor(qtd_jogos, qtd_numeros)
            jogos = gerador.gera_jogos(qtd_jogos, qtd_numeros)
            
            print(f"\nValor por jogo: R$ {valor_unitario:.2f}")
            print(f"Valor total: R$ {valor_total:.2f}")
            
            print("\nJogos gerados:")
            for i, jogo in enumerate(jogos, 1):
                print(f"Jogo {i}: {jogo}")
                
            jogar_novamente = input("\nDeseja gerar mais jogos? (s/n): ")
            if jogar_novamente.lower() != 's':
                break
                
        except ValueError as e:
            print(f"Erro: {e}")
            continue

if __name__ == "__main__":
    main()