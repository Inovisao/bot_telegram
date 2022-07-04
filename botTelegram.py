"""
Exemplo de um chatbot para Telegram

Código disponibilizado por Karan Batra
Pequenas alterações feitas por Hemerson Pistori (pistori@ucdb.br)

Como executar:
python botTelegram.py COPIE_AQUI_SEU_TOKEN

Funcionalidade: apenas repete as mensagens que alguém envia para o seu chatbot
"""

import sys

# Lê o token como parâmetro na linha de comando
MEU_TOKEN=sys.argv[1]

print('Carregando BOT usando o token ',MEU_TOKEN)

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define algumas respostas padrão para alguns comandos

# Resposta para o comando /start
def start(update, context):
    update.message.reply_text('Olá, já comecei, é só escrever qualquer coisa')


# Resposta para o comando /help
def help(update, context):
    update.message.reply_text('Eu só sei repetir o que me falam')


# Apenas responde com o mesmo texto que o usuário entrou
def echo(update, context):
    resposta='Você disse: '+update.message.text+' ?'
    update.message.reply_text(resposta)

# Salva as mensagens de erro
def error(update, context):
    logger.warning('Operação "%s" causou o erro "%s"', update, context.error)


def main():

    # Cria o módulo que vai ficar lendo o que está sendo escrito
    # no seu chatbot e respondendo.
    # Troque TOKEN pelo token que o @botfather te passou (se
    # ainda não usou @botfather, leia novamente o README)
    updater = Updater(MEU_TOKEN, use_context=True)

    # Cria o submódulo que vai tratar cada mensagem recebida
    dp = updater.dispatcher

    # Define as funções que vão ser ativadas com /start e /help
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Define a função 
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Define a função que vai tratar os erros
    dp.add_error_handler(error)

    # Inicia o chatbot
    updater.start_polling()

    # Roda o bot até que você dê um CTRL+C
    updater.idle()


if __name__ == '__main__':
    print('Bot respondendo, use CRTL+C para parar')
    main()

