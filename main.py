import random
import time


class Program:
    _rand = random.Random()

    @staticmethod
    def main():
        while True:
            print("\nSelect an option:")
            print("1. Use the array directly (integer numbers)")
            print("2. Use the method that generates an array (integer numbers)")
            print("3. Use the array directly (decimal numbers)")
            print("4. Use the method that generates an array (decimal numbers)")
            print("0. Exit")

            try:
                option = int(input())
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to continue...")
                continue

            if option == 0:
                return

            if option not in range(1, 5):
                print("Invalid option. Please choose an option from 0 to 4.")
                input("Press Enter to continue...")
                continue

            Program.process_option(option)

    @staticmethod
    def process_option(option):
        if option == 1:
            array1 = [4, 2, 3, 5, 5, 7, 1]
            Program.sort_and_print(array1, "Array before sorting:")
        elif option == 2:
            array2 = Program.generate_int_array()
            Program.sort_and_print(array2, "Array before sorting:")
        elif option == 3:
            array3 = [0.42, 0.33, 0.37, 0.57, 0.40]
            Program.sort_and_print(array3, "Array before sorting:")
        elif option == 4:
            array4 = Program.generate_double_array()
            Program.sort_and_print(array4, "Array before sorting:")

    @staticmethod
    def generate_double_array(min_val=0, length=10, values=5):
        values_list = []

        for i in range(min_val, length):
            if i < values:
                new_value = round(Program._rand.random(), 2)
                if new_value in values_list:
                    i -= 1
                    continue
                values_list.append(new_value)
            else:
                break

        return values_list

    @staticmethod
    def generate_int_array(min_val=0, length=10, values=5):
        values_list = []

        for i in range(min_val, length):
            if i < values:
                new_value = Program._rand.randint(min_val, length)
                if new_value in values_list:
                    i -= 1
                    continue
                values_list.append(new_value)
            else:
                break

        return values_list

    @staticmethod
    def sort_and_print(array, message):
        print(f"{message} {array}")
        start_time = time.time()
        Program.bucket_sort(array)
        end_time = time.time()
        print(f"\nArray after sorting: {array}")
        print(f"Time: {end_time - start_time} seconds")
        input("Press Enter to continue...")

    @staticmethod
    def bucket_sort(array):
        max_val = max(array)
        buckets = [[] for _ in range(int(max_val * len(array)) + 1)]

        for element in array:
            index = int(element * len(array))
            if index >= len(buckets):
                index = len(buckets) - 1
            buckets[index].append(element)

        Program.print_bucket_state(buckets)

        for i in range(len(buckets)):
            buckets[i].sort()

        Program.print_bucket_state(buckets)

        index = 0
        for i in range(len(buckets)):
            for item in buckets[i]:
                array[index] = item
                index += 1

    @staticmethod
    def print_bucket_state(buckets):
        print("Current state of buckets:")
        for i in range(len(buckets)):
            print(f"Bucket {i}: {buckets[i]}")
        print()

    @staticmethod
    def get_current_time():
        return 0  # Replace this with actual time handling


if __name__ == "__main__":
    Program.main()
