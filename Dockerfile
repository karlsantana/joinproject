# Use Python 3.9 como base
FROM python:3.9-slim

# Configure o diretório de trabalho no contêiner
WORKDIR /app

# Copie e instale as dependências antes de copiar o projeto (melhor uso de cache)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pelo servidor Django
EXPOSE 8000

# Copiar todo o código do projeto para o contêiner
COPY . /app/

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
