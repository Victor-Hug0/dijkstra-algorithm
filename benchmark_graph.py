import matplotlib.pyplot as plt
import benchmark

def plot_comparative(results, graph_sizes):
    reference_values = {
        32000: 0.05,      
        64000: 0.12,      
        128000: 0.25,     
        256000: 0.60,     
        512000: 1.40,     
        1024000: 3.00,    
        2048000: 6.50,   
        4096000: 15.00,   
    }
    
    my_impl_results = [(graph_sizes[r[0]], r[1]) for r in results]
    reference_results = [(size, reference_values[size]) for size in graph_sizes if size in reference_values]
    
    plt.figure(figsize=(10, 6))
    
    x_mine = [r[0] for r in my_impl_results]
    y_mine = [r[1] for r in my_impl_results]
    
    x_ref = [r[0] for r in reference_results]
    y_ref = [r[1] for r in reference_results]
    
    plt.loglog(x_mine, y_mine, 'o-', label='My implementation', linewidth=2)
    plt.loglog(x_ref, y_ref, 's--', label='Bin-Dij (reference)', linewidth=2)
    
    plt.title('Performance Comparison: My Implementation vs. Bin-Dij', fontsize=14)
    plt.xlabel('Number of nodes (n)', fontsize=12)
    plt.ylabel('Execution time (seconds)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    for i, txt in enumerate(x_mine):
        plt.annotate(f"{txt}", (x_mine[i], y_mine[i]), 
                     textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('dijkstra_comparison.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_comparative(benchmark.results, benchmark.graphLenght)
