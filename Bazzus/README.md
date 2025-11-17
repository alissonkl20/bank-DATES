# SQLite Media Database

Este projeto é uma aplicação em Python que utiliza um banco de dados SQLite para armazenar e gerenciar mídias, incluindo fotos, vídeos e textos. Abaixo estão as instruções para instalação e uso.

## Estrutura do Projeto

```
sqlite-media-db
├── src
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── db.py            # Configuração do banco de dados SQLite
│   ├── models.py        # Definição dos modelos de dados
│   └── types
│       └── index.py     # Tipos e interfaces do projeto
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd sqlite-media-db
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute o arquivo principal:
   ```
   python src/main.py
   ```

2. O aplicativo permitirá que você armazene e recupere fotos, vídeos e textos no banco de dados SQLite.

## Exemplos

- Para adicionar uma nova mídia, você pode usar a função correspondente no `main.py`.
- Para visualizar as mídias armazenadas, utilize a função de recuperação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.