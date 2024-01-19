# 105168265
def min_platforms(weights: list[int], limit: int) -> int:
    """Функция для определения кол-ва необходимых платформ."""
    weights.sort()
    platforms = 0
    left, right = 0, len(weights) - 1
    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
    robots_list = [int(i) for i in input().split()]
    platform_limit = int(input())
    result = min_platforms(robots_list, platform_limit)
    print(result)
