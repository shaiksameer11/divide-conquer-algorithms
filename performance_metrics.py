"""
Performance Metrics Module
Tracks and stores algorithm performance data
"""

class PerformanceMetrics:
    """Class to keep track of how well algorithms perform"""
    
    def __init__(self):
        self.comparisons = 0  # How many times we compare two numbers
        self.swaps = 0        # How many times we swap two numbers
        self.execution_time = 0  # How long the algorithm takes to run
        self.memory_usage = 0    # How much computer memory is used
        
    def reset(self):
        """Set all measurements back to zero"""
        self.comparisons = 0
        self.swaps = 0
        self.execution_time = 0
        self.memory_usage = 0
    
    def __str__(self):
        """Return a string representation of the metrics"""
        return (f"Comparisons: {self.comparisons}, "
                f"Swaps: {self.swaps}, "
                f"Time: {self.execution_time:.6f}s, "
                f"Memory: {self.memory_usage} bytes")
    
    def to_dict(self):
        """Convert metrics to dictionary format"""
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'execution_time': self.execution_time,
            'memory_usage': self.memory_usage
        }