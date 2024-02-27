# 108200943
def decode_instructions(s: str) -> str:
    """
    Декодирует строку, представляющую набор инструкций, закодированных в определенном формате.

    Входная строка s содержит инструкции, закодированные следующим образом:
    - Цифры представляют количество повторений подстроки.
    - Квадратные скобки [] указывают на секцию инструкций, которую нужно повторить.

    Args:
        s: Строка, содержащая закодированные инструкции.

    Returns:
        Раскодированные инструкции в виде строки.

    Example:
        Input: "3[a]2[bc]"
        Output: "aaabcbc"

    """
    stack = []
    num = 0
    temp_str = ""
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append((temp_str, num))
            temp_str = ""
            num = 0
        elif char == "]":
            prev_str, repeat_times = stack.pop()
            temp_str = prev_str + temp_str * repeat_times
        else:
            temp_str += char
    return temp_str


if __name__ == "__main__":
    encoded_instructions = input()
    decoded_instructions = decode_instructions(encoded_instructions)
    print(decoded_instructions)
