import os
import pandas as pd

####################################### MESSEJANA ##################################################################

# Pasta onde os arquivos em excel estão localizados
pasta = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.2. RMR\13.2.2. Escolas\13.2.2.2. MVM\13.2.2.2.2. Quantitativo\13.2.2.2.2.1. Base\13.2.2.2.2.1.2. Base Escolas'

# Listar todos os arquivos em excel na pasta
arquivo_preenchimento = [f for f in os.listdir(pasta) if f.endswith(".xlsx")]

# Criar uma lista para armazenar os nomes e datas de modificção dos arquivos
preenchimento_rmr = []

#iterar sobre os arquivos em excel e obter seus nomes e datas de modificação

for arquivo in arquivo_preenchimento:
    caminho_completo = os.path.join(pasta, arquivo)
    data_modificacao = os.path.getmtime(caminho_completo)
    preenchimento_rmr.append([arquivo, data_modificacao])

# Criar um DataFrame do pandas com os dados
df = pd.DataFrame(preenchimento_rmr, columns=["Nome do Arquivo", "Data de Modificação"] )

# Converter a coluna "Data de Modificação" para o formato de data
df["Data de Modificação"] = pd.to_datetime(df["Data de Modificação"], unit='s')

# Salvar o DataFrame em um arquivo excel
nome_arquivo_saida = r"G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.5. Outros\13.5.4. Preenchimento\Base das escolas de preenchimento\Preenchimento_escolas_RMR_MVM.xlsx"
df.to_excel(nome_arquivo_saida, index=False)

####################################### UNIVERSO ##################################################################
# Pasta onde os arquivos em excel estão localizados
pasta = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.2. RMR\13.2.2. Escolas\13.2.2.1. UNI\13.2.2.1.2. Quantitativo\13.2.2.1.2.1. Base\13.2.2.1.2.1.2. Base Escolas'

# Listar todos os arquivos em excel na pasta
arquivo_preenchimento = [f for f in os.listdir(pasta) if f.endswith(".xlsx")]

# Criar uma lista para armazenar os nomes e datas de modificção dos arquivos
preenchimento_rmr = []

#iterar sobre os arquivos em excel e obter seus nomes e datas de modificação
for arquivo in arquivo_preenchimento:
    caminho_completo = os.path.join(pasta, arquivo)
    data_modificacao = os.path.getmtime(caminho_completo)
    preenchimento_rmr.append([arquivo, data_modificacao])

# Criar um DataFrame do pandas com os dados
df = pd.DataFrame(preenchimento_rmr, columns=["Nome do Arquivo", "Data de Modificação"] )

# Converter a coluna "Data de Modificação" para o formato de data
df["Data de Modificação"] = pd.to_datetime(df["Data de Modificação"], unit='s')

# Salvar o DataFrame em um arquivo excel
nome_arquivo_saida = r"G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.5. Outros\13.5.4. Preenchimento\Base das escolas de preenchimento\Preenchimento_escolas_RMR_UNI.xlsx"
df.to_excel(nome_arquivo_saida, index=False)
