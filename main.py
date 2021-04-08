def subset(arr):
    sum = arr[0]
    maxsum, beg, end, left, right, h, hmax = 0, 0, 1, 0, len(arr), 1, 0

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            h += 1
            sum += arr[i]
            end = i + 1
        else:
            if h > hmax:
                hmax = h
                left = beg
                right = end
            if h == hmax:
                if sum > maxsum:
                    maxsum = sum
                    left = beg
                    right = end
            h = 1
            beg = i
            end = i + 1
            sum = arr[i]
        if h > hmax or (h == hmax and sum > maxsum):
            left = beg
            right = end
    arr = arr[left: right]
    return arr


if __name__ == '__main__':
    arr1 = list(map(int, input("Введите элементы массива:").split()))
    print("Исходный массив: ", arr1)

    print("Результат: ", subset(arr1))