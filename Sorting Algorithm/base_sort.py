import time
import numpy as np
from typing import List
from tqdm import tqdm

class BaseSorter:
    def __init__(self, name: str):
        self.name = name
        self.times = {size: [] for size in [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000]}
    
    def generate_random_array(self, size: int) -> List[int]:
        return list(np.random.randint(1, 500, size=size))
    
    def sort(self, arr: List[int]) -> List[int]:
        raise NotImplementedError("Subclasses must implement sort method")
    
    def measure_performance(self):
        for size in tqdm([10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000], desc="Sizes"):
            for _ in tqdm(range(10), desc=f"Trials for size {size}", leave=False):
                arr = self.generate_random_array(size)
                start_time = time.time()
                self.sort(arr.copy())  # Use copy to ensure fresh array each time
                end_time = time.time()
                self.times[size].append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    def get_average_times(self):
        return {size: sum(times)/len(times) for size, times in self.times.items()}