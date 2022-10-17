# Exemplos botTelegram

Descrição: Exemplos de códigos em python que funcionam como chatbots para o telegram.

Autor: Hemerson Pistori (pistori@ucdb.br)

### Informações sobre como foi testado

O software foi testado usando as seguintes versões de
Sistema Operacional, Linguagem e Biblioteca do Telegram

- Sistema Operacional: Ubuntu 20.04
- Versão do python: 3.10.4
- Versão do telegram: 13.13

### Gerando o chatbot no Telegram

- Instale o app do Telegram no seu celular e crie uma conta para você
- Entre no app do telegram e procure pelo usuário @botfather
- Mande a mensagem /newbot para o @botfather e vá
respondendo às perguntas que ele fizer. 
- Anote o TOKEN que ele vai gerar para você e o use no local indicado a seguir 

### Instalando as dependências no Linux (bibliotecas)

- Abra o terminal do Linux usando CTRL+ALT+T
- Verifique os ambientes conda já instalados usando o comando
abaixo (se já tiver o ambiente chamado chatbot, não precisa executar os comandos de instalação)
```
conda env list
```

- Se o ambiente conda chatbot não existir, execute os comandos abaixo para criar o ambiente e instalar as dependências

```
conda create -y --name chatbot python=3.10
conda activate chatbot
pip install python-telegram-bot pillow
```

### Iniciando o seu chatbot

- Use o botão ao lado de 'Clone' para baixar o arquivo compactador (.zip) contendo estes códigos em python na sua
máquina
- Abra o terminal do Linux usando CTRL+ALT+T
- Entre na pasta Downloads usando o comando abaixo
```
cd Downloads
```
- Use o comando abaixo para ver todos os arquivos que terminam com zip que estão na pasta Downloads para conferir
se baixou direito
```
ls *zip
```
- Descompacte o arquivo usando o comando abaixo
```
unzip bot_tel*
```
- Entre na pasta descompactada
```
cd bot_telegram-master
```

- Rode um dos comandos abaixo para iniciar o seu BOT. Não esqueça de trocar pelo TOKEN que você criou anteriormente usando o @botfather

```
python coletaImagens.py SEU_TOKEN_AQUI 
python botTelegram.py SEU_TOKEN_AQUI 
```


