import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    border1=1
    border101=101
    predict = np.random.randint(border1, border101)
    
    while number != predict:
        count += 1
        if number > predict:
          border1=predict
          predict = np.random.randint(border1+1, border101)
        elif number < predict:
          border101=predict
          predict = np.random.randint(border1, border101)

    return count