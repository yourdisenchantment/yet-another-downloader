# src/app/main.py

from .fetcher import fetch_with_requests, fetch_with_stealth
from .utils.utils import process_url


def downloader(url: str) -> bytes:
    """Скачивает изображение по указанному URL.

    Функция пытается загрузить изображение сначала с помощью стандартного HTTP-запроса,
    а в случае неудачи использует альтернативный метод с эмуляцией браузера.

    :param url: URL изображения для скачивания. Поддерживаются протоколы HTTP/HTTPS, а также сокращенные URL, начинающиеся с '//'
    :type url: str
    :return: Бинарные данные изображения
    :rtype: bytes
    """

    clean_url = process_url(url)
    content = fetch_with_requests(clean_url)

    if content is None:
        content = fetch_with_stealth(clean_url)

    if content is None:
        raise Exception(f"Не удалось загрузить изображение: {url}")

    return content
