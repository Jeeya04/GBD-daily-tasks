# pg1: Product of all elements except itself

def product_except_self(numbers):
    result = []

    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if i != j:
                product *= numbers[j]
        result.append(product)

    return result


nums = [1, 2, 3, 4]
print(product_except_self(nums))
