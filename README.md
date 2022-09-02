# Exemplos botTelegram

Descrição: Exemplos de códigos em python que funcionam como chatbots para o telegram.

Autor: Hemerson Pistori (pistori@ucdb.br)

Exemplos de uso: 

```
python botTelegram.py SEU_TOKEN_AQUI 
python coletaImagens.py SEU_TOKEN_AQUI 
```

### Dependências 

- Sistema Operacional: Ubuntu 20.04
- Versão do python: 3.10.4
- Versão do telegram: 13.13

```
conda create --name chatbot
pip install python-telegram-bot pillow
conda activate chatbot
```

### Gerando o chatbot no Telegram

- Entre no app do telegram e procure pelo usuário @botfather
- Mande a mensagem /newbot para o @botfather e vá
respondendo as perguntas. 
- Anote o token que ele vai gerar para você e o use como primeiro parâmetro quando for executar o programa botTelegram.py


