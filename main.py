def min_platforms(weights: list, limit: int) -> int:
    '''Функция для определения кол-ва необходимых платформ.'''
    # Сортируем массив с роботами.
    weights.sort()
    platforms = 0
    # Воспользуемся методом двух указателей.
    left, right = 0, len(weights) - 1
    while left <= right:
        # Если на платформе можно уместить два робота.
        if weights[left] + weights[right] <= limit:
            # Смещаем оба указателя
            left += 1
            right -= 1
        else:
            # Иначе смещаем только тяжелого.
            right -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
    robots_weights = list(map(int, input().split()))
    platform_limit = int(input())
    result = min_platforms(robots_weights, platform_limit)
    print(result)
