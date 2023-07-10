FROM python:3.9-slim
WORKDIR /app

# Copiar os arquivos de código-fonte para o diretório de trabalho
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta em que a aplicação será executada
EXPOSE 8888

# Comando para executar a aplicação
CMD ["python", "app.py"]