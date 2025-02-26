# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque


def labirinto(maze: Maze) -> bool:
    stack = deque() #Etapa 1: Cria a pilha
    visited = set() #Cria a coleção de lugares visitados
    
    init_pos = maze.get_init_pos_player() #Etapa 2: Essa função retorna a posição inicial aleatória do jogador, então salvamos ela numa variável
    stack.append(init_pos) #Etapa 3: O método append coloca o item no topo da pilha
    visited.add(init_pos) #Adicionando a posição inicial ao grupo de posições visitadas
    while stack: #Etapa 4: Enquanto a pilha não estiver vazia
        current_pos = stack.pop() #Etapa 5: Retira uma localização (linha, coluna) da pilha 
        
        if maze.find_prize(current_pos): #Etapa 6: Se a posição tiver o prêmio no local então "Caminho foi encontrado" e Retorne True
            return True
        #Caso contrário, se este local não contiver o prêmio
        maze.mov_player(current_pos) #Etapa 7: Move o jogador para este local
        
        x, y = current_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_pos = (x + dx, y + dy)
            # Verifica se a nova posição está dentro dos limites do labirinto
            if 0 <= new_pos[0] < maze.M.shape[0] and 0 <= new_pos[1] < maze.M.shape[1]:  
                #Etapa 8: Examine se as casas adjacentes estão livres
                if new_pos not in visited and maze.is_free(new_pos):
                    #Se sim insira sua posição na pilha
                    stack.append(new_pos)
                    visited.add(new_pos)
                    
        time.sleep(0.1) #Precisa do intervalo para conseguirmos visualizar cada movimento
        
    return False
    
if __name__ == "__main__":
    maze_csv_path = "labirinto1.txt"  
    maze = Maze() 
    maze.load_from_csv(maze_csv_path)
    
  
    maze.run()
    
    
    maze.init_player()
    
    #Começa a procura pelo prêmio
    
    if labirinto(maze):
        print("Caminho encontrado!")
    else:
        print("Caminho não encontrado!")





