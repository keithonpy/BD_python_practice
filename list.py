def test_list(): #
    numbers = [1, 2, 3, 4, 5]
    # add 10 to each of the numbers in the list
    print([i+10 for i in numbers])

    # extend the list to 10
    numbers2 = numbers[::]
    numbers2.extend(range(6, 11, 1))
    print(numbers2)

if __name__ == "__main__":
    test_list()