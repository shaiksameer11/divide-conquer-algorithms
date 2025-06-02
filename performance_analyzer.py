"""
Performance Analyzer Module
Handles testing and comparison of sorting algorithms
"""

import random
from typing import List, Dict
from sorting_algorithms import SortingAlgorithms

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Matplotlib not available. Visualization features will be disabled.")

class PerformanceAnalyzer:
    """Class to analyze and compare algorithm performance"""
    
    def __init__(self):
        self.sorter = SortingAlgorithms()
        self.results = {
            'quick_sort': {'time': [], 'comparisons': [], 'memory': []},
            'merge_sort': {'time': [], 'comparisons': [], 'memory': []}
        }
    
    def generate_test_data(self, size: int, data_type: str) -> List[int]:
        """
        Generate test data of specified type and size
        
        Args:
            size: Size of the array
            data_type: Type of data ('random', 'sorted', 'reverse_sorted')
            
        Returns:
            Generated test data
        """
        if data_type == 'random':
            return [random.randint(1, 1000) for _ in range(size)]
        elif data_type == 'sorted':
            return list(range(1, size + 1))
        elif data_type == 'reverse_sorted':
            return list(range(size, 0, -1))
        else:
            raise ValueError("Invalid data type. Use 'random', 'sorted', or 'reverse_sorted'")
    
    def run_performance_test(self, sizes: List[int], data_types: List[str], iterations: int = 3):
        """
        Run comprehensive performance tests
        
        Args:
            sizes: List of array sizes to test
            data_types: List of data types to test
            iterations: Number of iterations for each test
        """
        print("Running Performance Analysis...")
        print("=" * 50)
        
        total_tests = len(sizes) * len(data_types)
        current_test = 0
        
        for data_type in data_types:
            print(f"\n🔍 Testing with {data_type} data:")
            print("-" * 30)
            
            for size in sizes:
                current_test += 1
                print(f"📊 Array size: {size} (Test {current_test}/{total_tests})")
                
                # Quick Sort performance
                quick_times = []
                quick_comparisons = []
                quick_memory = []
                
                # Merge Sort performance
                merge_times = []
                merge_comparisons = []
                merge_memory = []
                
                print(f"   🔄 Running {iterations} iterations...")
                
                for iteration in range(iterations):
                    print(f"      Iteration {iteration + 1}/{iterations}", end="")
                    
                    # Generate test data
                    test_data = self.generate_test_data(size, data_type)
                    
                    # Test Quick Sort
                    print(" - Quick Sort", end="")
                    self.sorter.quick_sort(test_data)
                    metrics = self.sorter.get_metrics()
                    quick_times.append(metrics.execution_time)
                    quick_comparisons.append(metrics.comparisons)
                    quick_memory.append(metrics.memory_usage)
                    
                    # Test Merge Sort
                    print(" - Merge Sort", end="")
                    self.sorter.merge_sort(test_data)
                    metrics = self.sorter.get_metrics()
                    merge_times.append(metrics.execution_time)
                    merge_comparisons.append(metrics.comparisons)
                    merge_memory.append(metrics.memory_usage)
                    
                    print(" ✅")
                
                # Calculate averages
                avg_quick_time = sum(quick_times) / len(quick_times)
                avg_quick_comparisons = sum(quick_comparisons) / len(quick_comparisons)
                avg_quick_memory = sum(quick_memory) / len(quick_memory)
                
                avg_merge_time = sum(merge_times) / len(merge_times)
                avg_merge_comparisons = sum(merge_comparisons) / len(merge_comparisons)
                avg_merge_memory = sum(merge_memory) / len(merge_memory)
                
                # Store results
                self.results['quick_sort']['time'].append(avg_quick_time)
                self.results['quick_sort']['comparisons'].append(avg_quick_comparisons)
                self.results['quick_sort']['memory'].append(avg_quick_memory)
                
                self.results['merge_sort']['time'].append(avg_merge_time)
                self.results['merge_sort']['comparisons'].append(avg_merge_comparisons)
                self.results['merge_sort']['memory'].append(avg_merge_memory)
                
                # Print results
                print(f"   📈 Results:")
                print(f"      Quick Sort - Time: {avg_quick_time:.6f}s, "
                      f"Comparisons: {avg_quick_comparisons:.0f}, "
                      f"Memory: {avg_quick_memory:,} bytes")
                print(f"      Merge Sort - Time: {avg_merge_time:.6f}s, "
                      f"Comparisons: {avg_merge_comparisons:.0f}, "
                      f"Memory: {avg_merge_memory:,} bytes")
                
                # Show which is faster
                if avg_quick_time < avg_merge_time:
                    speedup = avg_merge_time / avg_quick_time
                    print(f"      🏆 Quick Sort is {speedup:.2f}x faster")
                else:
                    speedup = avg_quick_time / avg_merge_time
                    print(f"      🏆 Merge Sort is {speedup:.2f}x faster")
                
                print()
    
    def visualize_results(self, sizes: List[int]):
        """
        Create visualizations of performance results
        
        Args:
            sizes: List of array sizes used in testing
        """
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib not available. Skipping visualization.")
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Algorithm Performance Comparison', fontsize=16)
        
        # Execution Time Comparison
        axes[0, 0].plot(sizes, self.results['quick_sort']['time'], 
                       marker='o', label='Quick Sort', linewidth=2)
        axes[0, 0].plot(sizes, self.results['merge_sort']['time'], 
                       marker='s', label='Merge Sort', linewidth=2)
        axes[0, 0].set_xlabel('Array Size')
        axes[0, 0].set_ylabel('Execution Time (seconds)')
        axes[0, 0].set_title('Execution Time Comparison')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Comparisons Comparison
        axes[0, 1].plot(sizes, self.results['quick_sort']['comparisons'], 
                       marker='o', label='Quick Sort', linewidth=2)
        axes[0, 1].plot(sizes, self.results['merge_sort']['comparisons'], 
                       marker='s', label='Merge Sort', linewidth=2)
        axes[0, 1].set_xlabel('Array Size')
        axes[0, 1].set_ylabel('Number of Comparisons')
        axes[0, 1].set_title('Comparisons Comparison')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Memory Usage Comparison
        axes[1, 0].plot(sizes, self.results['quick_sort']['memory'], 
                       marker='o', label='Quick Sort', linewidth=2)
        axes[1, 0].plot(sizes, self.results['merge_sort']['memory'], 
                       marker='s', label='Merge Sort', linewidth=2)
        axes[1, 0].set_xlabel('Array Size')
        axes[1, 0].set_ylabel('Memory Usage (bytes)')
        axes[1, 0].set_title('Memory Usage Comparison')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Time Complexity Analysis (Log Scale)
        axes[1, 1].loglog(sizes, self.results['quick_sort']['time'], 
                         marker='o', label='Quick Sort', linewidth=2)
        axes[1, 1].loglog(sizes, self.results['merge_sort']['time'], 
                         marker='s', label='Merge Sort', linewidth=2)
        axes[1, 1].set_xlabel('Array Size (log scale)')
        axes[1, 1].set_ylabel('Execution Time (log scale)')
        axes[1, 1].set_title('Time Complexity Analysis')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def print_performance_summary(self, sizes: List[int]):
        """Print a summary of performance results"""
        print("\nPerformance Summary")
        print("=" * 50)
        
        total_quick_time = sum(self.results['quick_sort']['time'])
        total_merge_time = sum(self.results['merge_sort']['time'])
        
        avg_quick_comparisons = sum(self.results['quick_sort']['comparisons']) / len(sizes)
        avg_merge_comparisons = sum(self.results['merge_sort']['comparisons']) / len(sizes)
        
        print(f"Total Quick Sort Time: {total_quick_time:.6f} seconds")
        print(f"Total Merge Sort Time: {total_merge_time:.6f} seconds")
        print(f"Average Quick Sort Comparisons: {avg_quick_comparisons:.0f}")
        print(f"Average Merge Sort Comparisons: {avg_merge_comparisons:.0f}")
        
        if total_quick_time < total_merge_time:
            print(f"Quick Sort is {(total_merge_time/total_quick_time):.2f}x faster on average")
        else:
            print(f"Merge Sort is {(total_quick_time/total_merge_time):.2f}x faster on average")
    
    def verify_correctness(self):
        """Test algorithm correctness with sample data"""
        print("\nCorrectness Verification:")
        print("-" * 30)
        
        # Test with small arrays
        test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [5, 2, 4, 6, 1, 3],
            [1],
            []
        ]
        
        for i, arr in enumerate(test_arrays, 1):
            print(f"Test {i}: {arr}")
            
            # Quick Sort
            quick_sorted = self.sorter.quick_sort(arr.copy())
            print(f"  Quick Sort: {quick_sorted}")
            
            # Merge Sort
            merge_sorted = self.sorter.merge_sort(arr.copy())
            print(f"  Merge Sort: {merge_sorted}")
            
            # Verify correctness
            python_sorted = sorted(arr)
            quick_correct = quick_sorted == python_sorted
            merge_correct = merge_sorted == python_sorted
            
            print(f"  Quick Sort Correct: {quick_correct}")
            print(f"  Merge Sort Correct: {merge_correct}")
            print()