# src/app/fetcher.py

import requests
from fake_useragent import UserAgent
from stealth_requests import StealthSession


def fetch_with_requests(url: str) -> bytes | None:
    """Пытается загрузить данные по URL с помощью библиотеки requests и случайного User-Agent.

    Использует стандартный HTTP-запрос с добавлением случайного User-Agent для имитации браузера. Устанавливает таймаут 30 секунд для запроса.

    :param url: URL для загрузки данных
    :type url: str
    :return: Бинарные данные в случае успешной загрузки, None в случае ошибки
    :rtype: bytes | None
    """

    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.content

    except requests.exceptions.RequestException:
        return None


def fetch_with_stealth(url: str) -> bytes | None:
    """Пытается загрузить данные по URL с помощью StealthSession для обхода защиты.

    Использует специальную сессию StealthSession, которая эмулирует поведение реального браузера. Делает до 3-х попыток загрузки в случае неудачи.

    :param url: URL для загрузки данных
    :type url: str
    :return: Бинарные данные в случае успешной загрузки, None в случае ошибки
    :rtype: bytes | None
    """

    try:
        with StealthSession() as session:
            response = session.get(url, retry=3)
            response.raise_for_status()

            return response.content

    except requests.exceptions.RequestException:
        return None
