# Executando a Aplicação Python

Este é um guia passo a passo para executar a aplicação Python em seu ambiente local. Siga as instruções abaixo para configurar e executar a aplicação com sucesso.

## Sem Docker
Certifique-se de que você tenha os seguintes pré-requisitos instalados em sua máquina:
- Python 3
- pip (gerenciador de pacotes)

### Configuração
1. Clone ou faça o download do repositório da aplicação para o seu ambiente local.
2. Navegue até o diretório raiz da aplicação usando o terminal ou prompt de comando.
3. Crie um ambiente virtual (opcional, mas recomendado) para isolar as dependências da aplicação do seu ambiente global. Execute o seguinte comando para criar um ambiente virtual:
```
python -m venv venv
```

4. Ative o ambiente virtual recém-criado. Execute o seguinte comando no terminal:
- No macOS/Linux:

  ```
  source venv/bin/activate
  ```

- No Windows:

  ```
  venv\Scripts\activate
  ```

5. Instale as dependências da aplicação usando o gerenciador de pacotes pip. Execute o seguinte comando:
```
pip install -r requirements.txt
```


### Executando
Depois de instaladas todas as dependências, se não quiser utilizar o arquivo disponível `labtrans.db`, siga os seguintes comandos:

1. Execute o seguinte comando para criar todas as estruturas de tabelas no banco:
```
python models.py
```

2. Em seguida, execute o seguinte comando para migrar todos os dados:
```
python migrate_data.py
```


## Com Docker
1. Certifique-se de que você tenha os seguintes pré-requisitos instalados em sua máquina:
- Docker
- Docker Compose

2. Na pasta raiz do projeto, execute o seguinte comando para criar a imagem da aplicação e subir o container:
```
docker-compose up --build
```

3. Após subir o container, será necessário executar alguns comandos dentro dele. Execute o comando `docker ps` para listar os containers ativos. Em seguida, execute o seguinte comando para abrir o bash dentro do container:
```
docker exec -it <id_container> bash
```

Substitua `<id_container>` pelo ID do container da aplicação.

4. Agora, dentro do container, execute os comandos de migração:
```
python models.py
python migrate_data.py
```


### Execução do init.sql
1. Na raiz do container, execute o comando `sqlite3 labtrans.db` para abrir o console do banco de dados.
2. Dentro do console, execute o comando `.read init.sql`.

**Também é possível aproveitar o arquivo `labtrans.db`. Para isso, siga estas instruções:**

1. Antes de executar `docker-compose up --build`, copie o arquivo `.db` para o diretório `data` do seu projeto.
2. Em seguida, execute o build.
3. Agora, ao executar `ls` no diretório `data`, você verá que o arquivo `.db` está compartilhado.
4. Mova esse arquivo para a pasta raiz do container usando o comando `mv labtrans.db /app`.



