def extract_price(text: str) -> str:
    """Функция, которая извлекает из строки цену"""
    """Примеры:
    $110.00 $122.00
    Ex Tax: $90.00
    $98.00 $122.00
    Ex Tax: $80.00
    $122.00
    Ex Tax: $100.00"""

    # text == "$110.00 $122.00\nEx Tax: $90.00"
    # разбиение предложения по переносу строки
    # split_by_lines == ["$110.00 $122.00", "Ex Tax: $90.00"]
    split_by_lines: list[str] = text.split("\n")

    # разбиение предложения по пробелам
    # first_price == ["$110.00", "$122.00"]
    first_price_lines = split_by_lines[0].split(' ')

    # взятие первого эл-та т.е. актуальной цены
    first_price = first_price_lines[0]

    return first_price

