import json

def ipynb_to_txt(ipynb_path, txt_path):
    try:
        # Cargar el archivo .ipynb
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Abrir el archivo .txt para escribir el contenido
        with open(txt_path, 'w', encoding='utf-8') as f:
            # Iterar sobre las celdas del notebook
            for cell in notebook['cells']:
                # Diferenciar entre celdas de código y de Markdown
                if cell['cell_type'] == 'code':
                    # Escribir el código precedido de un comentario indicativo
                    f.write('# Código:\n')
                    f.write(''.join(cell['source']) + '\n\n')
                elif cell['cell_type'] == 'markdown':
                    # Escribir el texto precedido de un comentario indicativo
                    f.write('# Texto:\n')
                    f.write(''.join(cell['source']) + '\n\n')
        print("picha")

    except FileNotFoundError:
        print(f"Error: El archivo '{ipynb_path}' no existe.")
    except IOError:
        print(f"Error: No se pudo escribir el archivo '{txt_path}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    
# Usar la función con la ruta de tu archivo .ipynb y el destino del .txt
ipynb_to_txt('KNN.ipynb', 'asdf.txt')