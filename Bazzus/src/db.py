import sqlite3
from typing import List, Tuple, Optional
import os

def create_connection(db_file: str) -> Optional[sqlite3.Connection]:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
        print(f"Conexão com {db_file} estabelecida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao conectar com o banco: {e}")
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create tables for storing media."""
    try:
        cursor = conn.cursor()
        
        # Tabela única para mídias
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS midias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            dados BLOB,
            texto TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        print("Tabelas criadas/verificadas com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")

def inserir_midia(conn: sqlite3.Connection, nome: str, tipo: str, caminho_arquivo: str = None, texto: str = None) -> int:
    """Insere uma mídia no banco de dados."""
    cursor = conn.cursor()
    dados = None
    
    try:
        if caminho_arquivo:
            with open(caminho_arquivo, 'rb') as f:
                dados = f.read()
        
        cursor.execute('''
            INSERT INTO midias (nome, tipo, dados, texto)
            VALUES (?, ?, ?, ?)
        ''', (nome, tipo, dados, texto))
        
        conn.commit()
        midia_id = cursor.lastrowid
        print(f"Mídia '{nome}' inserida com ID: {midia_id}")
        return midia_id
        
    except Exception as e:
        print(f"Erro ao inserir mídia: {e}")
        return -1

def recuperar_midias(conn: sqlite3.Connection) -> List[sqlite3.Row]:
    """Recupera todas as mídias do banco."""
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, tipo, texto, data_criacao FROM midias')
    return cursor.fetchall()

def visualizar_midias(conn: sqlite3.Connection) -> None:
    """Exibe todas as mídias de forma formatada."""
    midias = recuperar_midias(conn)
    
    if not midias:
        print("Nenhuma mídia encontrada no banco.")
        return
    
    print("\n" + "="*80)
    print("MIDIAS ARMAZENADAS NO BANCO")
    print("="*80)
    
    for midia in midias:
        print(f"ID: {midia['id']}")
        print(f"Nome: {midia['nome']}")
        print(f"Tipo: {midia['tipo']}")
        print(f"Texto: {midia['texto'] or 'N/A'}")
        print(f"Data: {midia['data_criacao']}")
        print("-" * 40)

def buscar_midia_por_id(conn: sqlite3.Connection, midia_id: int) -> Optional[sqlite3.Row]:
    """Busca uma mídia específica pelo ID."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM midias WHERE id = ?', (midia_id,))
    return cursor.fetchone()

def deletar_midia(conn: sqlite3.Connection, midia_id: int) -> bool:
    """Remove uma mídia do banco."""
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM midias WHERE id = ?', (midia_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Mídia ID {midia_id} removida com sucesso!")
            return True
        else:
            print(f"Mídia ID {midia_id} não encontrada!")
            return False
            
    except sqlite3.Error as e:
        print(f"Erro ao deletar mídia: {e}")
        return False

def estatisticas_banco(conn: sqlite3.Connection) -> None:
    """Exibe estatísticas do banco."""
    cursor = conn.cursor()
    
    # Total de mídias
    cursor.execute('SELECT COUNT(*) FROM midias')
    total = cursor.fetchone()[0]
    
    # Mídias por tipo
    cursor.execute('SELECT tipo, COUNT(*) FROM midias GROUP BY tipo')
    por_tipo = cursor.fetchall()
    
    print("\n" + "="*50)
    print("ESTATÍSTICAS DO BANCO")
    print("="*50)
    print(f"Total de mídias: {total}")
    print("\nDistribuição por tipo:")
    for tipo, count in por_tipo:
        print(f"  {tipo}: {count}")

def exportar_midia(conn, midia_id, destino):
    """
    Exporta o arquivo binário da mídia para o caminho destino.
    Cria a pasta de destino se não existir.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT nome, tipo, dados FROM midias WHERE id = ?", (midia_id,))
    resultado = cursor.fetchone()
    if resultado and resultado[2]:
        nome, tipo, dados = resultado
        pasta_destino = os.path.dirname(destino)
        if pasta_destino and not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        with open(destino, "wb") as f:
            f.write(dados)
        print(f"Mídia '{nome}' exportada para {destino}")
    else:
        print("Mídia não encontrada ou não possui arquivo binário.")