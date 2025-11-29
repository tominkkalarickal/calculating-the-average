#function to get the three test scores and calculate the average
def get_average():
    print("Enter your three test scores:")

    test_1=float(input("test 1: "))
    test_2=float(input("test 2: "))
    test_3=float(input("test 3: "))

    average=(test_1+test_2+test_3)/3
    return average

#check the average and display message
def check_average(average):
    if average> 95:
        print(f"Congratulations! You did great! Your average score is {average:.2f}.")
    if average>= 85 and average <= 95:
        print(f"You did great! but did not reach the top high. Your average score is {average:.2f}.")
    if average>= 70 and average <= 84:
        print(f"Good effort! but you could do better. Your average score is {average:.2f}.")
    if average < 70:
        print(f"You need to study harder next time. your average score is {average:.2f}.")

#main function and starting point of the program
def main():
    while True:
        avg= get_average()
        check_average(avg)
        #run the program again?
        again = input("Do you want to continue? (y/n)")
        if again != "y":
            print("End")
            break

main()


