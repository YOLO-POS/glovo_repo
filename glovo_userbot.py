from flask import Flask, request
import hashlib
import json
from pyrogram import Client

glovo_userbot = Flask(__name__)

# Замените этот секрет на ваш секрет
client_secret = '5a7614893783e6a1ada3ce226af2cc9a'

@glovo_userbot.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные из POST-запроса
    '''post_data = request.get_json()
    print(post_data)

    # Проверяем валидность данных
    verify_original = post_data.get('verify', '')
    del post_data['verify']

    verify = [
        post_data['account'],
        post_data['object'],
        str(post_data['object_id']),
        post_data['action']
    ]

    # Если есть дополнительные параметры
    if 'data' in post_data:
        verify.append(post_data['data'])

    verify.append(str(post_data['time']))
    verify.append(client_secret)

    # Создаём строку для верификации запроса клиентом
    verify = hashlib.md5(';'.join(verify).encode()).hexdigest()

    # Проверяем валидность данных
    if verify != verify_original:
        return '', 403

    # Проверяем, является ли событие онлайн-заказом
    if post_data['object'] == 'incoming_order' and post_data['action'] == 'added':
        # Получаем информацию о заказе
        order_info = post_data.get('data', {})

        # Выводим информацию о заказе в консоль
        print(f'Получен онлайн заказ: {json.dumps(order_info, indent=2)}')

        # Отправляем результат в Telegram
        send_to_telegram(order_info)

    # Отвечаем на запрос 200 статусом'''
    print('post')
    send_to_telegram({})
    print('200')
    return '', 200

def send_to_telegram(order_info):
    api_id = 8927112
    api_hash = 'a216a15ebbf50bbbc5d96be7c7e93fbb'
    print('tg here')
    # Создаем клиент Pyrogram
    chat_id_01 = -1001581146060
    chat_id_03 = -1001957717504
    client = Client(name='me_client', api_id=api_id, api_hash=api_hash)
    client.start()
    client.send_message(-1001975419277, f'Получен новый заказ: {order_info}')
    client.stop()
    print('tg ready')
if __name__ == '__main__':
    api_id = 8927112
    api_hash = 'a216a15ebbf50bbbc5d96be7c7e93fbb'
    print('tg here copy')
    client = Client(name='me_client', api_id=api_id, api_hash=api_hash)
    client.start()
    client.send_message(-1001975419277, f'Получен новый заказ:')
    client.stop()
    glovo_userbot.run(port=8080)


