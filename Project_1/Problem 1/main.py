import backtracking_with_deduction
import backtracking_without_deduction
import time


def main():
    # sudoku with deductive method: x-wing
    a = time.time()
    backtracking_with_deduction.run_sudoku()
    b = time.time()
    c = b - a #find the time it takes for it to find a solution
    print("Time with deduction:", c)
    print()

    a = time.time()
    backtracking_without_deduction.run_sudoku()  # this is without deduction
    b = time.time()
    d = b - a #find the time it takes for it to find a solution

    print("Time without deduction:", d)
    print()

    print("Without deduction it is", c / d, "times faster.")



if __name__ == "__main__":
    main()
