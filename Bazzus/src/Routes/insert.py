# Crie o arquivo linha por linha
import sys
import os
# Adiciona a pasta atual (src) ao path para importar db.py
sys.path.append(os.path.dirname(__file__))

from db import create_connection, create_tables, inserir_midia, visualizar_midias

def inserir_dados_exemplo():
    """Script para inserir dados de exemplo no banco"""
    
    # Conectar ao banco (agora na mesma pasta src)
    conn = create_connection('baseus.db')
    if conn is None:
        print("Erro ao conectar ao banco!")
        return
    
    # Criar tabelas se não existirem
    create_tables(conn)
    
    print("Inserindo dados de exemplo...")
    
    # Inserir textos
    textos_exemplo = [
        ("Nota importante", "texto", "Esta é uma nota importante sobre o projeto."),
        ("Lista de tarefas", "texto", "1. Estudar Python\n2. Desenvolver projeto\n3. Testar sistema"),
        ("Ideias criativas", "texto", "Algumas ideias para implementar no futuro."),
    ]
    
    for nome, tipo, texto in textos_exemplo:
        inserir_midia(conn, nome, tipo, texto=texto)
    
    # Tentar inserir arquivos se existirem
    arquivos_exemplo = [
        ("Logo do projeto", "imagem", "../logo.png"),
        ("Documentação", "documento", "../README.md"),
        ("Vídeo demonstrativo", "video", "../demo.mp4"),
    ]
    
    for nome, tipo, arquivo in arquivos_exemplo:
        if os.path.exists(arquivo):
            inserir_midia(conn, nome, tipo, caminho_arquivo=arquivo)
        else:
            print(f"Arquivo {arquivo} não encontrado. Inserindo como texto...")
            inserir_midia(conn, nome, tipo, texto=f"Conteúdo do {arquivo}")
    
    # Visualizar resultados
    print("\n" + "="*60)
    print("DADOS INSERIDOS NO BANCO:")
    print("="*60)
    visualizar_midias(conn)
    
    # Fechar conexão
    conn.close()
    print("\nInserção concluída!")

def criar_dados_teste():
    """Função compatível com o menu principal para inserir dados de teste."""
    inserir_dados_exemplo()

if __name__ == "__main__":
    inserir_dados_exemplo()