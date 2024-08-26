import time
import forca_bruta
import heuristica_vizinho

def main():

    op = int(input("\n Escolha o problema exemplo que deseja resolver (1-10 ou 0 para sair): "))

    while op != 0:
        problem_path = ""

        match(op):
            case 1:
                problem_path = "testes/in1.txt"
            case 2:
                problem_path = "testes/in2.txt"
            case 3:
                problem_path = "testes/in3.txt"
            case 4:
                problem_path = "testes/in4.txt"
            case 5:
                problem_path = "testes/in5.txt"
            case 6:
                problem_path = "testes/in6.txt"
            case 7:
                problem_path = "testes/in7.txt"
            case 8:
                problem_path = "testes/in8.txt"
            case 9:
                problem_path = "testes/in9.txt"
            case 10:
                problem_path = "testes/in10.txt"
            case _:
                print("Valor Inválido!")
                continue  # Volta ao início do loop se o valor for inválido
        

        print("Escolha a abordagem para resolver o problema:")
        print("1 - Força Bruta")
        print("2 - Heurística do Algoritmo de Vizinhança")
        op = int(input("Digite o número da abordagem: "))

        match(op):
            case 1:
                graph = forca_bruta.build_graph_from_file(problem_path)
                
                # Medir o tempo de execução da força bruta
                start_time = time.time()
                max_set = forca_bruta.max_independent_set(graph)
                end_time = time.time()
                
                print("O maior conjunto independente é:", max_set)
                print(f"Tempo de execução da Força Bruta: {end_time - start_time:.6f} segundos")
                
                forca_bruta.plot_graph(graph, max_set)
                
            case 2:
                graph = heuristica_vizinho.build_graph_from_file(problem_path)
                
                # Medir o tempo de execução da heurística de vizinhança
                start_time = time.time()
                max_set = heuristica_vizinho.max_independent_set(graph)
                end_time = time.time()
                
                print("O maior conjunto independente é:", max_set)
                print(f"Tempo de execução da Heurística de Vizinhança: {end_time - start_time:.6f} segundos")
                
                heuristica_vizinho.plot_graph(graph, max_set)

            case _:
                print("Valor Inválido!")
        
        op = int(input("\n Escolha o problema exemplo que deseja resolver (1-10 ou 0 para sair): "))

if __name__ == "__main__":
    main()
