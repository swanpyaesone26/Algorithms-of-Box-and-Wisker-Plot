import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self):
        self.data = []                    # Initialize an empty list to store the data from user input

    def add_data(self, value):
        self.data.append(value)           # Add user input to the data list

    def gather_data(self):
        while True:
            user_input = input("Please enter a number (or press Enter to finish): ")
            if user_input == "":
                break                    # If user want to stop loop press enter
            try:
                num = float(user_input)
                self.add_data(num)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def insertion_sort(self):
        n = len(self.data)
        for i in range(1, n):
            j = i
            while j > 0 and self.data[j-1] > self.data[j]:
                self.data[j], self.data[j-1] = self.data[j-1], self.data[j]
                j -= 1

    def find_median(self):
        n = len(self.data)
        middle_index = n // 2
        if n % 2 == 1:
            return self.data[middle_index]
        else:
            return (self.data[middle_index-1] + self.data[middle_index]) / 2

    def find_quartiles(self):
        n = len(self.data)
        Q2 = self.find_median()

        if n % 2 == 0:
            first_half = self.data[:n//2]
            second_half = self.data[n//2:]
        else:
            first_half = self.data[:n//2]
            second_half = self.data[n//2+1:]

        Q1 = DataAnalysis._find_median_static(first_half)
        Q3 = DataAnalysis._find_median_static(second_half)

        return Q1, Q2, Q3

    @staticmethod
    def _find_median_static(data_slice):
        n = len(data_slice)
        middle_index = n // 2
        if n % 2 == 1:
            return data_slice[middle_index]
        else:
            return (data_slice[middle_index-1] + data_slice[middle_index]) / 2

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def analyze_data(self):
        self.insertion_sort()
        min_num = self.data[0]
        max_num = self.data[-1]
        mean_xbar = self.calculate_mean()
        Q1, Q2, Q3 = self.find_quartiles()
        median_value = Q2

        print(f"This is Q1: {Q1}")
        print(f"This is Q2: {Q2}")
        print(f"This is Q3: {Q3}")
        print(f"This is minimum value: {min_num}")
        print(f"This is maximum value: {max_num}")
        print(f"This is x bar (mean): {mean_xbar}")

        if mean_xbar > median_value:
            print("This is right-skewed.")
        else:
            print("This is left-skewed.")

    def visualize_data(self):
        plt.figure(figsize=(10, 6))
        plt.boxplot(self.data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'))
        plt.title('Box and Whisker Plot')
        plt.xlabel('Values')
        plt.scatter(self.data, [1] * len(self.data), color='red', zorder=3, marker='o')
        plt.show()



analysis = DataAnalysis()
analysis.gather_data()

# Analyzing and visualizing data
analysis.analyze_data()
analysis.visualize_data()
