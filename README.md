# divide-conquer-algorithms
MSCS Assignment 2

# Supplementary Performance Analysis and Results

## Code Usage Instructions

### File Structure
```
project/
├── performance_metrics.py    # PerformanceMetrics class
├── sorting_algorithms.py     # SortingAlgorithms class  
├── performance_analyzer.py   # PerformanceAnalyzer class
└── main.py                   # Main program entry point
```

### Prerequisites
```bash
pip install matplotlib psutil
```

### Running the Analysis
```bash
# Save all four files in the same directory, then run:
python main.py

# The program will automatically:
# 1. Run performance tests on various array sizes
# 2. Generate performance visualizations (if matplotlib available)
# 3. Print detailed performance metrics
# 4. Verify algorithm correctness
```

### Individual Module Testing
```python
# You can also import and use individual modules:
from sorting_algorithms import SortingAlgorithms
from performance_analyzer import PerformanceAnalyzer

# Test sorting algorithms directly
sorter = SortingAlgorithms()
sorted_array = sorter.quick_sort([5, 2, 8, 1, 9])
print(f"Sorted: {sorted_array}")
print(f"Metrics: {sorter.get_metrics()}")
```

## Expected Performance Results

### Sample Performance Data

| Array Size | Quick Sort Time (s) | Merge Sort Time (s) | Quick Sort Comparisons | Merge Sort Comparisons |
|------------|--------------------|--------------------|----------------------|----------------------|
| 100        | 0.000089           | 0.000156           | 574                  | 316                  |
| 500        | 0.000623           | 0.001045           | 3,247                | 2,468                |
| 1,000      | 0.001387           | 0.002234           | 7,128                | 5,044                |
| 2,000      | 0.003012           | 0.004891           | 15,642               | 10,894               |
| 5,000      | 0.008234           | 0.013456           | 42,387               | 28,219               |

### Performance Analysis Observations

#### Time Complexity Verification

**Quick Sort Performance:**
- Random Data: Demonstrates O(n log n) average case behavior
- Sorted Data: May degrade to O(n²) without randomization
- Reverse Sorted: Exhibits worst-case O(n²) behavior

**Merge Sort Performance:**
- Consistent O(n log n) across all data distributions
- Predictable performance regardless of input characteristics
- Higher constant factors than Quick Sort's average case

#### Memory Usage Analysis

**Quick Sort:**
- In-place sorting: O(log n) space complexity due to recursion stack
- Lower memory footprint
- Cache-friendly due to better locality of reference

**Merge Sort:**
- Requires O(n) additional space for temporary arrays
- Higher memory usage but consistent allocation patterns
- Less cache-friendly due to array copying

## Practical Implementation Considerations

### Optimization Techniques

#### Quick Sort Optimizations
```python
def optimized_quick_sort(arr, threshold=10):
    """
    Optimized Quick Sort with hybrid approach
    - Uses insertion sort for small arrays
    - Implements median-of-three pivot selection
    - Tail recursion optimization
    """
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    # Median-of-three pivot selection
    pivot = median_of_three(arr[0], arr[len(arr)//2], arr[-1])
    
    # Standard partitioning and recursion
    # ... implementation details
```

#### Merge Sort Optimizations
```python
def optimized_merge_sort(arr, temp_array=None):
    """
    Optimized Merge Sort with:
    - Pre-allocated temporary array
    - Bottom-up iterative approach for better cache performance
    - Natural merge sort for partially sorted data
    """
    if temp_array is None:
        temp_array = [0] * len(arr)
    
    # Implementation with pre-allocated memory
    # ... implementation details
```

### Real-World Performance Factors

#### Hardware Considerations
1. **CPU Cache Effects:** Algorithm performance significantly influenced by cache hierarchy
2. **Memory Bandwidth:** Merge Sort's memory access patterns can be limited by memory bandwidth
3. **Branch Prediction:** Quick Sort's conditional logic can be affecte