"""
реализовать 3 сортировки 3-х разных типов
пузырек, реккурентная, сортировка суммированием
"""


def bubble_sort(arr):
    """
    Реализация сортировки пузырьком.

    Аргументы:
    arr -- список элементов, который нужно отсортировать.

    Возвращает:
    Отсортированный список элементов.

    Внешний цикл проходит по всем элементам списка.
    Внутренний цикл проходит по парам соседних элементов и меняет их местами, если они находятся в неправильном порядке.
    После каждой итерации внешнего цикла наибольший элемент всплывает на правильную позицию.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """
    Реализация рекурсивной сортировки Quick Sort.

    Аргументы:
    arr -- список элементов, который нужно отсортировать.

    Возвращает:
    Отсортированный список элементов.

    Если длина входного списка меньше или равна 1, возвращается сам список.
    Опорный элемент (pivot) выбирается как элемент в середине списка.
    Создаются списки left, middle и right, содержащие элементы меньше, равные и больше опорного элемента соответственно.
    Затем рекурсивно вызывается функция quick_sort для списков left и right, а результаты объединяются с middle и возвращаются.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(arr):
    """
    Реализация сортировки подсчетом.

    Аргументы:
    arr -- список целых чисел, который нужно отсортировать.

    Возвращает:
    Отсортированный список целых чисел.

    Сначала находится максимальное значение во входном списке arr.
    Создается список counts длиной max_val + 1, где каждый элемент инициализируется нулем.
    Затем происходит подсчет количества встречающихся элементов: каждый элемент arr инкрементирует соответствующий элемент counts.
    Далее, создается отсортированный массив sorted_arr, куда каждый элемент добавляется соответствующее количество раз в зависимости от его значения в counts.
    Наконец, возвращается отсортированный массив sorted_arr.
    """

    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted_arr = []

    for num in arr:
        counts[num] += 1

    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def main():
    # Создание трех массивов для сортировки
    arr_bubble = [57, 23, 45, 32, 15, 78, 88, 42, 67]
    arr_quick = [55, 21, 37, 29, 18, 62, 49, 84, 91]
    arr_counting = [10, 8, 6, 4, 2, 9, 7, 5, 3]

    # Вывод отсортированных результатов
    print("Отсортированный массив с помощью сортировки пузырьком:", bubble_sort(arr_bubble))
    print("Отсортированный массив с помощью рекурсивной сортировки:", quick_sort(arr_quick))
    print("Отсортированный массив с помощью сортировки подсчетом:", counting_sort(arr_counting))


if __name__ == "__main__":
    main()