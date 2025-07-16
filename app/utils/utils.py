# app/utils/utils.py


def process_url(url: str) -> str:
    """...

    :param url:
    :type url:
    :return:
    :rtype:
    """

    url = url.strip()

    if url.startswith("//"):
        url = "https:" + url

    elif not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url
