import tkinter as tk
import random

#Problem 1
initial_state = [
    [0, 0, 0, 0, 3, 4, 0, 9, 1],
    [4, 0, 0, 1, 7, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 7, 0, 0],
    [1, 0, 0, 0, 0, 3, 0, 0, 0],
    [9, 0, 5, 0, 0, 0, 1, 2, 0],
    [0, 0, 4, 5, 0, 0, 0, 6, 7],
    [6, 2, 0, 0, 0, 9, 0, 0, 0],
    [5, 4, 0, 2, 1, 0, 9, 8, 6],
    [8, 7, 0, 3, 5, 6, 4, 1, 0]
]

#Problem 2
initial_state2 = [
    [0, 6, 5, 2, 0, 0, 4, 0, 0],
    [0, 7, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 4, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 5, 9, 0, 6, 0, 7],
    [0, 0, 0, 3, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 4, 3, 0, 0, 0, 0, 0, 0]
]

#Problem 3
initial_state3 = [
    [9, 0, 4, 0, 0, 5, 6, 0, 0],
    [0, 0, 0, 4, 9, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 8, 0, 4, 0],
    [0, 3, 2, 9, 0, 4, 0, 0, 0],
    [7, 0, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 2, 8, 0],
    [5, 6, 1, 7, 0, 0, 0, 0, 8],
    [0, 0, 0, 8, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 1, 5]
]

#Problem 4
initial_state4 = [
    [0, 0, 1, 0, 8, 0, 0, 0, 0],
    [0, 3, 0, 7, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 8, 0, 5],
    [0, 0, 0, 0, 0, 1, 0, 0, 4],
    [0, 0, 0, 0, 0, 3, 0, 9, 1],
    [0, 0, 0, 6, 7, 2, 0, 0, 0],
    [7, 0, 0, 0, 3, 0, 0, 2, 0],
    [2, 0, 6, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0]
]

# Variable global para mantener la última celda resaltada
last_highlighted_cell = None

#Variable para contar la posición del algoritmo
global_pos = 0
                
def get_values_in_row_col_quad(row, col, sudoku_cells):
    # Obtener valores en la fila
    row_values = [sudoku_cells[row][j].get() for j in range(9) if sudoku_cells[row][j].get() != ""]
    
    # Obtener valores en la columna
    col_values = [sudoku_cells[i][col].get() for i in range(9) if sudoku_cells[i][col].get() != ""]
    
    # Determinar el inicio del cuadrante
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    
    # Obtener valores en el cuadrante
    quad_values = []
    for i in range(3):
        for j in range(3):
            cell_value = sudoku_cells[start_row + i][start_col + j].get()
            if cell_value != "":
                quad_values.append(cell_value)
    
    return row_values, col_values, quad_values

def get_empty_cell_info(i, j):
        row_values, col_values, quad_values = get_values_in_row_col_quad(i, j, sudoku_cells)
        return row_values, col_values, quad_values, i, j, (i // 3) * 3 + (j // 3)
    
def go_all():
    while(len(empty_cells) > 0):
        get_possible_number()
    get_possible_number()
   
#Reglas que tiene que seguir el algoritmo para obtener la solución
def get_possible_number():
    global last_highlighted_cell, global_pos
    
    #Restablecer el texto
    info_label.config(text="")
    
    if len(empty_cells) <= 0:
        #Finished Game
        update_text("HA TERMINADO EL JUEGO")
        return
    
    # Restablecer el borde de la última celda resaltada
    if last_highlighted_cell is not None:
        i, j = last_highlighted_cell
        sudoku_cells[i][j].config(highlightbackground="black", highlightthickness=0)
    
    i = empty_cells[global_pos][0]
    j = empty_cells[global_pos][1]
        
    # Resaltar la nueva celda
    sudoku_cells[i][j].config(highlightbackground="red", highlightthickness=1)
    last_highlighted_cell = (i, j)
    
    #Conseguir info de la celda
    row, column, quad, rowNum, columnNum, quadNum = get_empty_cell_info(i, j)
    
    #Conseguir posibles
    possible_row = possible_list(row)
    possible_col = possible_list(column)
    possible_quad = possible_list(quad)
    
    all_possibles_this = set(possible_row) & set(possible_col) & set(possible_quad)
    all_possibles_this = sorted(list(all_possibles_this))
    
    all_possibles_this = regla_4(all_possibles_this, rowNum, columnNum)
    
    print(all_possibles_this)
    
    #Regla 1 - Si se puede poner 1 número solo, se pone
    if regla_1(possible_row, possible_col, possible_quad, rowNum, columnNum, quadNum):
        pass
    
    #Regla 2 - Si viendo todos los números posibles combinando la fila, columna y cuadrante, sólo hay 1 en común
    elif regla_2(all_possibles_this, rowNum, columnNum, quadNum):
        pass

    #Regla 3 - Si viendo todos los números posibles en todas las posiciones de la misma, fila, columna y cuadrante, hay algun num solo en esta pos
    elif regla_3(possible_row, possible_col, possible_quad, rowNum, columnNum, quadNum):
        pass
    
    else:
        global_pos += 1
        
    if global_pos >= len(empty_cells):
        global_pos = 0
    
def possible_list(myList):
    numeros_completos = range(1, 10)
    lista_strings = [str(numero) for numero in numeros_completos]
    numeros_faltantes = set(lista_strings) - set(myList)
    return sorted(list(numeros_faltantes))

def regla_1(possible_row, possible_col, possible_quad, rowNum, columnNum, quadNum):
    global global_pos
    
    if len(possible_row) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(possible_row[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 1: El {possible_row[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque sólo falta este número en esta fila")
        return True
    if len(possible_col) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(possible_col[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 1: El {possible_col[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque sólo falta este número en esta columna")
        return True
    if len(possible_quad) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(possible_quad[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 1: El {possible_quad[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque sólo falta este número en este cuadrante")
        return True
    return False

def regla_2(nums, rowNum, columnNum, quadNum):
    global global_pos
    
    if len(nums) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(nums[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 2: El {nums[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}. Viendo todos los números posibles de fila, columna y cuadrante, sólo hay un número que sea posible en todos a la vez")
        return True
    return False
        
def regla_3(possible_row, possible_col, possible_quad, rowNum, columnNum, quadNum):
    #Check row
    all_possibles_row = []
    all_possibles_col = []
    all_possibles_quad = []
    
    quad_positions = []
    
    start_row = rowNum - rowNum % 3
    start_col = columnNum - columnNum % 3
    
    # Itera sobre las 3 filas y columnas del cuadrante
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            quad_positions.append((r, c))
            
    quad_positions.remove((rowNum, columnNum))
    
    #Consigu todos los posibles de los mismos de su columna, fila y cuadrante
    for cell in empty_cells:
        #Conseguir info de la celda
        row_this, column_this, quad_this, rowNum_this, columnNum_this, quadNum_this = get_empty_cell_info(cell[0], cell[1])
        
        #Conseguir posibles
        possible_row_this = possible_list(row_this)
        possible_col_this = possible_list(column_this)
        possible_quad_this = possible_list(quad_this)

        all_possibles_this = set(possible_row_this) & set(possible_col_this) & set(possible_quad_this)
        all_possibles_this = sorted(list(all_possibles_this))
            
        if cell[0] == rowNum and cell[1] != columnNum:
            for poss in all_possibles_this:
                if poss not in all_possibles_row:
                    all_possibles_row.append(poss)
                    
        if cell[1] == columnNum and cell[0] != rowNum:
            for poss in all_possibles_this:
                if poss not in all_possibles_col:
                    all_possibles_col.append(poss)
            
        if cell in quad_positions:
            for poss in all_possibles_this:
                if poss not in all_possibles_quad:
                    all_possibles_quad.append(poss)
                    
    #Comprobar que alguno de los posibles en nuestra posición no esté en los posibles del resto
    final_possibles_row = []
    
    for poss in possible_row:
        if poss not in all_possibles_row:
            final_possibles_row.append(poss)
            
    final_possibles_col = []
    
    for poss in possible_col:
        if poss not in all_possibles_col:
            final_possibles_col.append(poss)
            
    final_possibles_quad = []
    
    for poss in possible_quad:
        if poss not in all_possibles_quad:
            final_possibles_quad.append(poss)
            
    if len(final_possibles_row) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(final_possibles_row[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 3: El {final_possibles_row[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque esta posición es la única en esta fila que tiene este número como posible")
        return True
    if len(final_possibles_col) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(final_possibles_col[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 3: El {final_possibles_col[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque esta posición es la única en esta columna que tiene este número como posible")
        return True
    if len(final_possibles_quad) == 1:
        #Colocar num
        sudoku_cells[rowNum][columnNum].insert(0, str(final_possibles_quad[0]))
        sudoku_cells[rowNum][columnNum].config(state='readonly')
        empty_cells.pop(global_pos)
        update_text(f"Regla 3: El {final_possibles_quad[0]} ha sido añadido a la posición {(rowNum + 1, columnNum + 1)}, porque esta posición es la única en este cuadrante que tiene este número como posible")
        return True
            
    return False

#Quitar posibilidades en filas, columnas y cuadrantes
def regla_4(possible_nums, rowNum, colNum):
    #Search affecting quadrants
    quadrant_row = rowNum // 3
    quadrant_col = colNum // 3
    quadrant_index = quadrant_row * 3 + quadrant_col
    
    adjacent_quadrants = []
    
    for i in range(3):
        for j in range(3):
            if i == quadrant_row or j == quadrant_col:
                adjacent_index = i * 3 + j
                if adjacent_index != quadrant_index:
                    start_row = (adjacent_index // 3) * 3
                    start_col = (adjacent_index % 3) * 3
                    
                    # Lista para almacenar las posiciones del cuadrante
                    positions = []

                    # Itera sobre las 3 filas y columnas del cuadrante
                    for r in range(start_row, start_row + 3):
                        for c in range(start_col, start_col + 3):
                            if (r,c) in empty_cells:
                                positions.append((r, c))
                    
                    add_quad = True
                    for pos in positions:
                        if pos[0] != rowNum and pos[1] != colNum:
                            add_quad = False
                    
                    if add_quad:        
                        adjacent_quadrants.append(positions)
                    
    for quadrant_positions in adjacent_quadrants:
        if len(quadrant_positions) == 0:
            continue
        #Comprobar que las posiciones estén en la misma row
        ref = quadrant_positions[0][0]
        same_row = True
        for pos in quadrant_positions:
            if pos[0] != ref:
                #No están en la misma row
                same_row = False
        
        ref = quadrant_positions[0][1]
        same_col = True
        for pos in quadrant_positions:
            if pos[1] != ref:
                #No están en la misma col
                same_col = False
        
        if (same_row or same_col) and len(quadrant_positions) > 1:
            #Están en la misma fila o columna
            #Comprobar que tengan 1 número en común y quitárselo de posibles a la celda
            #Obtener posibles de esas celdas
            
            same_possibles = []
            
            for pos in quadrant_positions:
                row_this, column_this, quad_this, rowNum_this, columnNum_this, quadNum_this = get_empty_cell_info(pos[0], pos[1])
                possible_row_this = possible_list(row_this)
                possible_col_this = possible_list(column_this)
                possible_quad_this = possible_list(quad_this)

                all_possibles_this = set(possible_row_this) & set(possible_col_this) & set(possible_quad_this)
                all_possibles_this = sorted(list(all_possibles_this))
                same_possibles.append(all_possibles_this)
                
            numeros_comunes = set(same_possibles[0])
            for lista in same_possibles[1:]:
                numeros_comunes = numeros_comunes.intersection(set(lista))
                
            removed = []
            for num in numeros_comunes:
                if num in possible_nums:
                    possible_nums.remove(num)
                    removed.append(num)
            
            if len(removed) > 0:
                update_text(f"Regla 4: los números {removed} han sido eliminados de los posibles ya que en un cuadrante contiguo sólo hay casillas en paralelo, lo que obliga a que los números posibles de esas casillas para esa fila o columna estén en esas casillas")
                
    return possible_nums

def update_text(text_to_show):
    text = info_label.cget("text")
    text += "\n" + text_to_show
    # Actualizar el texto del Label
    info_label.config(text=text)

# Crear la ventana principal
root = tk.Tk()
root.title("Sudoku")

# Configurar el tamaño de la ventana
root.geometry("500x550")  # Ajustado para acomodar los bordes más gruesos

# Crear la cuadrícula del Sudoku y almacenar las referencias a las celdas
sudoku_cells = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry = tk.Entry(root, width=2, font=('Arial', 20), justify='center', bd=1)
        entry.grid(row=i, column=j, sticky="nsew", padx=(0,5) if j in [2,5] else 0, pady=(0,5) if i in [2,5] else 0)
        if initial_state3[i][j] != 0:  # Si la celda no debe estar vacía, coloca el número
            entry.insert(0, str(initial_state3[i][j]))
            entry.config(state='readonly')  # Opcional: haz que las celdas predefinidas no sean editables
        sudoku_cells[i][j] = entry

empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku_cells[i][j].get() == ""]

# Crear el botón ContinueGame
continue_button = tk.Button(root, text="Continuar Sudoku", command=get_possible_number)
continue_button.grid(row=10, column=0, columnspan=9)

# Crear el botón Go All
go_all_btn = tk.Button(root, text="Resolver Completo", command=go_all)
go_all_btn.grid(row=11, column=0, columnspan=9)

# Crear el Label para mostrar la información de la celda resaltada
info_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=300)  # Ajusta el valor de wraplength según sea necesario
info_label.grid(row=12, column=0, columnspan=9, sticky="w")

# Iniciar el loop principal de la GUI
root.mainloop()
