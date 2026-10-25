"""Project 2: Messy Code Improvement
Shows a messy program and the improved, readable version of the same logic.

---------- BEFORE (messy) ----------
    a=[55,78,90,34,67];s=0;m=a[0]
    for i in range(5):
     s=s+a[i]
     if a[i]>m:m=a[i]
    print(s,s/5,m)

Problems: unclear names, magic number 5, index loop instead of iteration,
no functions, no labels on the output.

---------- AFTER (improved, below) ----------
"""


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return 0.0
    return calculate_total(marks) / len(marks)


def find_highest(marks):
    return max(marks)


def grade_for(average):
    if average >= 75:
        return "A"
    if average >= 60:
        return "B"
    if average >= 40:
        return "C"
    return "F"


def main():
    marks = [55, 78, 90, 34, 67]
    average = calculate_average(marks)

    print(f"Total marks : {calculate_total(marks)}")
    print(f"Average     : {average}")
    print(f"Highest mark: {find_highest(marks)}")
    print(f"Grade       : {grade_for(average)}")


if __name__ == "__main__":
    main()
