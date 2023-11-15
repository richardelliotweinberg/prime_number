for i in range(6, 201):
##This tests the loop of all numbers between 6 and 200
    found_solution = False
##This is saying that all the found solutions are false
    for quantity1 in range(0, 34):
##This is the range of sixes that can be multiplied to up to 200
        for quantity2 in range(0, 23):
            for quantity3 in range(0, 11):
                total = 6 * quantity1 + 9 * quantity2 + 20 * quantity3
                if total == i:
                    print(f"{i}: {quantity1} x 6 + {quantity2} x 9 + {quantity3} x 20")
                    found_solution = True
                    break
            if found_solution:
                break
        if found_solution:
            break
