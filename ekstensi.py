import random
import time
import matplotlib.pyplot as plt
import numpy as np

#membandingkan dua buah array
class ArrayAnalyzer:
    #inisialisasi
    def __init__(self, stambuk="028"):
        self.max_value = 250 - int(stambuk)
        random.seed(28) 
    #membuat array
    def generate_array(self, n):
        return [random.randint(1, self.max_value) for _ in range(n)]
    #mengecek keunikan array
    def check_uniqueness(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return False
            seen.add(num)
        return True
    #menghitung kasus terburuk
    def calculate_worst_case(self, n):
        return n * n
    #menghitung kasus rata-rata
    def calculate_average_case(self, n):
        return n * np.log2(n)
    #menganalisis array
    def analyze_arrays(self):
        n_values = [100, 150, 200, 250, 300, 350, 400, 500]
        worst_cases = []
        avg_cases = []
        
        
        for n in n_values:
            worst_cases.append(self.calculate_worst_case(n))
            avg_cases.append(self.calculate_average_case(n))
            
            
            arr = self.generate_array(n)
            is_unique = self.check_uniqueness(arr)
            print(f"\nArray size {n}:")
            print(f"First 10 elements: {arr[:10]}...")
            print(f"Is unique: {is_unique}")
        
        #menyimpan hasil analisis
        with open("worst_avg.txt", "w") as f:
            f.write("Analysis Results\n")
            f.write("===============\n\n")
            for i, n in enumerate(n_values):
                f.write(f"n = {n}:\n")
                f.write(f"Worst Case: {worst_cases[i]:.2f}\n")
                f.write(f"Average Case: {avg_cases[i]:.2f}\n\n")
        
        #membuat grafik
        plt.figure(figsize=(12, 8))
        plt.plot(n_values, worst_cases, 'r-', label='Worst Case (O(n²))')
        plt.plot(n_values, avg_cases, 'b-', label='Average Case (O(n log n))')
        plt.xlabel('Array Size (n)')
        plt.ylabel('Time Complexity')
        plt.title('Time Complexity Analysis')
        plt.legend()
        plt.grid(True)
        plt.savefig('complexity_analysis.pdf')
        plt.savefig('complexity_analysis.jpg')
        plt.close()
#main
def main():
    
    analyzer = ArrayAnalyzer() 
    analyzer.analyze_arrays()

if __name__ == "__main__":
    main()