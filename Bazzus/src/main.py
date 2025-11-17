from db import create_connection, create_tables, visualizar_midias, inserir_midia, deletar_midia, estatisticas_banco, exportar_midia
from Routes.insert import criar_dados_teste

def mostrar_menu():
    """Exibe o menu principal atualizado"""
    print("""
╔══════════════════════════════════════════════╗
║            BASEUS - Gerenciador de Mídias    ║
╠══════════════════════════════════════════════╣
║ 1. Visualizar todas as mídias                ║
║ 2. Inserir nova mídia                        ║
║ 3. Deletar mídia                             ║
║ 4. Estatísticas do banco                     ║
║ 5. Criar dados de teste                      ║    
║ 6. Exportar mídia                            ║
║ 7. Sair                                      ║
╚══════════════════════════════════════════════╝
    """)

def inserir_nova_midia(conn):
    """Interface para inserir nova mídia."""
    print("\n--- INSERIR NOVA MÍDIA ---")
    nome = input("Nome da mídia: ").strip()
    if not nome:
        print("Nome é obrigatório!")
        return
    print("Tipos disponíveis: imagem, video, texto, audio, documento")
    tipo = input("Tipo da mídia: ").strip().lower()
    caminho_arquivo = input("Caminho do arquivo (deixe em branco para texto): ").strip()
    texto = None
    if caminho_arquivo:
        try:
            inserir_midia(conn, nome, tipo, caminho_arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado!")
    else:
        texto = input("Digite o texto: ").strip()
        if texto:
            inserir_midia(conn, nome, tipo, texto=texto)
        else:
            print("Texto ou arquivo é obrigatório!")

def deletar_midia_interface(conn):
    """Interface para deletar mídia."""
    print("\n--- DELETAR MÍDIA ---")
    try:
        midia_id = int(input("ID da mídia a ser deletada: "))
        deletar_midia(conn, midia_id)
    except ValueError:
        print("ID deve ser um número!")

def exportar_midia_interface(conn):
    print("\n--- EXPORTAR MÍDIA ---")
    try:
        midia_id = int(input("ID da mídia a exportar: "))
        destino = input("Caminho de destino (ex: C:\\Users\\Lzer\\Pictures\\test ou C:/Users/Lzer/Pictures/test): ").strip()
        if not destino:
            print("Você precisa informar o caminho de destino!")
            return
        exportar_midia(conn, midia_id, destino)
    except ValueError:
        print("ID deve ser um número!")

def main():
    db_name = 'baseus.db'
    conn = create_connection(db_name)
    if conn is not None:
        create_tables(conn)
        print("""
██████╗  █████╗ ███████╗███████╗██╗   ██╗███████╗
██╔══██╗██╔══██╗╚══███╔╝╚══███╔╝██║   ██║██╔════╝
██████╔╝███████║  ███╔╝   ███╔╝ ██║   ██║███████╗
██╔══██╗██╔══██║ ███╔╝   ███╔╝  ██║   ██║╚════██║
██████╔╝██║  ██║███████╗███████╗╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
        """)
        print("Bem-vindo ao BASEUS - Um passo da verdade!")
        while True:
            mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == '1':
                visualizar_midias(conn)
            elif opcao == '2':
                inserir_nova_midia(conn)
            elif opcao == '3':
                deletar_midia_interface(conn)
            elif opcao == '4':
                estatisticas_banco(conn)
            elif opcao == '5':
                criar_dados_teste()
            elif opcao == '6':
                exportar_midia_interface(conn)
            elif opcao == '7':
                print("Obrigado por usar o BASEUS!")
                break   
            else:
                print("Opção inválida! Tente novamente.")
        conn.close()
        print("Conexão com o banco fechada.")
    else:
        print("Erro! Não foi possível criar a conexão com o banco de dados.")

if __name__ == '__main__':
    main()