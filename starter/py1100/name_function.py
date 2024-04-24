def get_format_name(first: str, last: str):
    """フォーマットした氏名を取得する

    Args:
        first (str): 名前
        last (str): 苗字
    """
    full_name = f"{first} {last}"
    return full_name.title()


def get_format_name2(first: str, last: str, middle: str = ""):
    """フォーマットした氏名を取得する

    Args:
        first (str): 名前
        last (str): 苗字
        middle (str): ミドルネーム
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
