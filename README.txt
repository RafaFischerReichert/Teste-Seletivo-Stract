# README - Instalação do Código

## Pré-requisitos

Antes de instalar o código, certifique-se de que você possui os seguintes pré-requisitos:

- Python 3.x instalado em sua máquina.
- Pip (gerenciador de pacotes do Python) instalado.
- Acesso à internet para baixar as dependências.

## Passos para Instalação

1. **Clone o repositório**

   Abra o terminal e clone o repositório do projeto usando o seguinte comando:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

   Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório que contém o código.

2. **Navegue até o diretório do projeto**

   Após clonar o repositório, navegue até o diretório do projeto:

   ```bash
   cd <NOME_DO_DIRETORIO>
   ```

   Substitua `<NOME_DO_DIRETORIO>` pelo nome do diretório do projeto.

3. **Instale as dependências**

   Utilize o pip para instalar as dependências necessárias. Execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

4. **Configuração das Variáveis de Ambiente**

   Certifique-se de configurar as variáveis de ambiente necessárias, como `API_URL` e `HEADERS`. Você pode fazer isso criando um arquivo `.env` na raiz do projeto e adicionando as variáveis necessárias.

5. **Executar o Código**

   Para executar o código, utilize o seguinte comando:

   ```bash
   python TesteSeletivo.py
   ```

   O servidor será iniciado e estará disponível em `http://0.0.0.0:5000`.

## Conclusão

Após seguir esses passos, o código estará instalado e em execução na sua máquina. Você pode acessar as rotas disponíveis conforme definido no código.

Se você encontrar algum problema durante a instalação, sinta-se à vontade para abrir uma issue no repositório.