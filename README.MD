# Books API

Este projeto é uma API RESTful para gerenciar livros usando FastAPI e Supabase.

## Funcionalidades

- Obter uma lista de livros
- Obter um livro específico por ID
- Armazenar um novo livro
- Atualizar um livro existente
- Excluir um livro

## Requisitos

- Python 3.x
- FastAPI
- Supabase

## Instalação

1. Clone o repositório:

   ```shell
   git clone https://github.com/seu-nome-de-usuario/books-api.git

2.  Instale as dependências:
    
    ```shell
    pip install -r requirements.txt
    
3.  Configuração do Supabase:
    
    -   Crie um projeto no Supabase e obtenha sua URL e Chave de API do Supabase.
    -   Substitua a configuração do cliente Supabase no código (`SUPABASE_URL SUPABASE_KEY`) com sua própria configuração do cliente Supabase.
    
4.  Execute a aplicação:

    ```shell
    uvicorn main:app --reload 
    
5.  A API estará disponível em [http://localhost:8000](http://localhost:8000/).
    

## Pontos de Extremidade da API

-   `GET /books` - Obter uma lista de todos os livros.
-   `GET /books/{id}` - Obter um livro específico por ID.
-   `POST /books` - Armazenar um novo livro.
-   `PUT /books/{id}` - Atualizar um livro existente.
-   `DELETE /books/{id}` - Excluir um livro.

Para obter os formatos detalhados de requisição e resposta, consulte a documentação da API disponível na URL raiz (`/docs`).

## Tratamento de Erros

A API trata erros e retorna códigos de status HTTP apropriados e detalhes de erro quando necessário. Alguns cenários comuns de erro incluem:

-   Livro não encontrado: `404 Not Found`
-   Payload de requisição inválido: `400 Bad Request`
-   Erro do servidor: `500 Internal Server Error`

## Licença

Este projeto está licenciado sob a [Licença MIT](https://chat.openai.com/LICENSE).