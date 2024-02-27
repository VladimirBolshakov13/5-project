# 108273025
BASE_TEN = 10
OPEN_BRACKET = "["
CLOSE_BRACKET = "]"


def decode_instructions(encoded_instructions: str) -> str:
    """
    Декодирует закодированную инструкцию и возвращает раскодированную строку.

    Аргументы:
    encoded_instructions (str): Закодированная инструкция, содержащая цифры, скобки и символы.

    Возвращает:
    str: Раскодированная строка на основе закодированной инструкции.

    Пример использования:
    encoded_instructions = "3[a]2[bc]"
    decoded_instructions = decode_instructions(encoded_instructions)
    print(decoded_instructions)
    "aaabcbc"
    """

    stack: list[str] = []  # Список для хранения элементов стека
    num = 0
    temp_str = ""
    for char in encoded_instructions:
        if char in "0123456789":
            num = num * BASE_TEN + int(char)
        elif char == OPEN_BRACKET:
            stack.append((temp_str, num))
            temp_str = ""
            num = 0
        elif char == CLOSE_BRACKET:
            prev_str, repeat_times = stack.pop()
            temp_str = prev_str + temp_str * repeat_times
        else:
            temp_str += char

    return temp_str


if __name__ == "__main__":
    encoded_instructions = input()
    decoded_instructions = decode_instructions(encoded_instructions)
    print(decoded_instructions)
