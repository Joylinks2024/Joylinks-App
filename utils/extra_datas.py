escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def make_title(title):
    name = ""
    for letter in title:
        if letter in escape_chars:
            name += f'\\'
        else:
            name += letter
    return name


def make_html(text: str) -> str:
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") \
        .replace("<a ", "<a href='https://www.example.com' ") \
        .replace("<copy>", "<div style='background-color:#f2f2f2; padding: 5px; border: 1px dashed #ccc;'>") \
        .replace("</copy>", "</div>")


def escape_markdown(text: str) -> str:
    """
    Escape Markdown characters in the given text.
    """
    escape_chars = '\\`*_{}[]()#+-.!'
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)
