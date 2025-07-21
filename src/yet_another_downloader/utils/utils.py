# src/app/utils/utils.py


def process_url(url: str) -> str:
    """Нормализует URL-адрес, добавляя протокол HTTPS, если он отсутствует.

    Обрабатывает следующие случаи:
    - Удаляет начальные и конечные пробелы
    - Добавляет 'https:' к URL, начинающимся с '//'
    - Добавляет 'https://' к URL без протокола

    :param url: Исходный URL-адрес, который может быть неполным
    :type url: str
    :return: Нормализованный URL-адрес с протоколом HTTPS
    :rtype: str
    """

    url = url.strip()

    if url.startswith("//"):
        url = "https:" + url

    elif not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url
