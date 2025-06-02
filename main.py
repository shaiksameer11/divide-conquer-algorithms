"""
Main Program
Entry point for running sorting algorithm performance analysis
"""

from performance_analyzer import PerformanceAnalyzer
import sys

def main():
    """Main function to run the performance analysis"""
    
    print("🚀 Starting Sorting Algorithm Performance Analysis")
    print("=" * 60)
    print("This program will test Quick Sort and Merge Sort algorithms")
    print("and compare their performance across different data sizes.")
    print()
    
    # Check if required packages are available
    print("📋 Checking system requirements...")
    try:
        import psutil
        print("✅ psutil is available")
    except ImportError:
        print("❌ Error: Required package 'psutil' not found.")
        print("Please install with: pip install psutil")
        return
    
    try:
        import matplotlib.pyplot as plt
        print("✅ matplotlib is available - charts will be generated")
        matplotlib_available = True
    except ImportError:
        print("⚠️  matplotlib not available - charts will be skipped")
        matplotlib_available = False
    
    print()
    print("🔧 Initializing performance analyzer...")
    
    # Initialize performance analyzer
    try:
        analyzer = PerformanceAnalyzer()
        print("✅ Performance analyzer initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing analyzer: {e}")
        return
    
    # Test parameters
    sizes = [100, 500, 1000, 2000, 5000]
    data_types = ['random']  # Can be extended to ['random', 'sorted', 'reverse_sorted']
    iterations = 3
    
    print()
    print("📊 Test Configuration:")
    print(f"   Array sizes: {sizes}")
    print(f"   Data types: {data_types}")
    print(f"   Iterations per test: {iterations}")
    print()
    
    print("🏃‍♂️ Starting performance tests...")
    print("This may take a few moments...")
    print()
    
    try:
        # Run performance tests
        analyzer.run_performance_test(sizes, data_types, iterations)
        print("✅ Performance tests completed successfully")
    except Exception as e:
        print(f"❌ Error during performance testing: {e}")
        print(f"Error details: {type(e).__name__}: {str(e)}")
        return
    
    print()
    print("📈 Generating performance summary...")
    try:
        # Print summary
        analyzer.print_performance_summary(sizes)
    except Exception as e:
        print(f"❌ Error generating summary: {e}")
    
    print()
    if matplotlib_available:
        print("📊 Generating visualization charts...")
        try:
            # Visualize results (if matplotlib is available)
            analyzer.visualize_results(sizes)
            print("✅ Charts generated successfully")
        except Exception as e:
            print(f"⚠️  Chart generation failed: {e}")
    else:
        print("⚠️  Skipping chart generation (matplotlib not available)")
    
    print()
    print("🔍 Running correctness verification...")
    try:
        # Verify algorithm correctness
        analyzer.verify_correctness()
        print("✅ Correctness verification completed")
    except Exception as e:
        print(f"❌ Error during correctness verification: {e}")
    
    print()
    print("🎉 Analysis Complete!")
    print("=" * 60)
    print("Thank you for using the Sorting Algorithm Performance Analyzer.")
    print()
    
    # Ask user if they want to see additional information
    try:
        response = input("Would you like to see detailed algorithm information? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print_algorithm_info()
    except KeyboardInterrupt:
        print("\n👋 Program terminated by user.")
    except Exception:
        pass  # Just continue if input fails

def print_algorithm_info():
    """Print detailed information about the algorithms"""
    print()
    print("📚 Algorithm Information:")
    print("=" * 50)
    
    print("\n🔵 Quick Sort:")
    print("   • Average Time Complexity: O(n log n)")
    print("   • Worst Case: O(n²)")
    print("   • Space Complexity: O(log n)")
    print("   • In-place sorting: Yes")
    print("   • Stable: No")
    print("   • Best for: Random data, memory-constrained systems")
    
    print("\n🟢 Merge Sort:")
    print("   • Time Complexity: O(n log n) for all cases")
    print("   • Space Complexity: O(n)")
    print("   • In-place sorting: No")
    print("   • Stable: Yes")
    print("   • Best for: Large datasets, external sorting, parallel processing")
    
    print("\n💡 Key Differences:")
    print("   • Quick Sort is faster on average but can be slow on sorted data")
    print("   • Merge Sort is consistent but uses more memory")
    print("   • Quick Sort is preferred for general-purpose sorting")
    print("   • Merge Sort is preferred when stability is required")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n💥 Unexpected error occurred:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nIf this error persists, try running simple_main.py instead.")
        sys.exit(1)