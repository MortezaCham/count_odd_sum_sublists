def count_odd_sum_sublists(items):
    #creating a variable for counting sublists with odd sum
    odd_sums = 0
    #chosing each element of items for checking sum of it with other elements
    for i in range(len(items)):
        #creating a variable for saving sums of each sublists
        pre_sum = 0
        #chosing next elements of items for creating sub lists and calculating sums
        for j in range(i, len(items)):
            #calculating sum of sublists
            pre_sum += items[j]
            #checking if sum is odd or not
            if pre_sum % 2 == 1:
                #if sum is odd we count it
                odd_sums += 1

    return odd_sums


