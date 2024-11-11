import random
import time
# if you find any bug, please report it
# feel free to change any code to make it better

try:
    def age_average(n, a, b): # Get the random average age
        random_age = []
        for i in range(n):  # append the ages to the list
            random_age.append(random.randint(int(a), int(b)))
        for i in range(len(random_age)): # print all the random ages
            print(f"{str(random_age[i])} ", end=" ")
        age_avg = sum(random_age) / n # Get the average
        time.sleep(.1)
        print(f"\nAverage age of the ages above (which is randomly generated) is {str(age_avg)}")
        time.sleep(.1)
        choice = input("Do you want to go the main menu (Y or N): ")
        choice.capitalize()
        if choice == "Y":
            main()
        else:
            print("Bye!! 👋👋")
            time.sleep(1)
            exit() # exit lol        


    def main():
        
        
        print("Welcome to a program that will calculate age of a given group of people")
        time.sleep(.1)
        print("It's made by Iram Mahmud Ruhan")
        time.sleep(.1)
        while True:
            num_people = int((input("Enter the number of people: ")))

            time.sleep(.1)
            start_age = int(input("Enter the lowest age: "))
            
            time.sleep(.1)
            end_age = int(input("Enter the highest age: "))

            age_average(num_people, start_age, end_age)

                


    if __name__ == "__main__":
        main()

except Exception: # stop a crash
    print("Something went wrong, try again or report the bug")