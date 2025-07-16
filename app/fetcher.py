# app/fetcher.py

import requests
from fake_useragent import UserAgent
from stealth_requests import StealthSession


def fetch_with_requests(url: str) -> bytes | None:
    """...

    :param url:
    :type url:
    :return:
    :rtype:
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
    """...

    :param url:
    :type url:
    :return:
    :rtype:
    """

    try:
        with StealthSession() as session:
            response = session.get(url, retry=3)
            response.raise_for_status()

            return response.content

    except requests.exceptions.RequestException:
        return None
