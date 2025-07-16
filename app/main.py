# app/main.py

from utils.utils import process_url

from .fetcher import fetch_with_requests, fetch_with_stealth


def download_image(url: str) -> bytes:
    """...

    :param url:
    :type url:
    :return:
    :rtype:
    """

    clean_url = process_url(url)
    content = fetch_with_requests(clean_url)

    if content is None:
        content = fetch_with_stealth(clean_url)

    if content is None:
        raise Exception(f"Не удалось загрузить изображение: {url}")

    return content
