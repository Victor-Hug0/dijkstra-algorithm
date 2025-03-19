import matplotlib.pyplot as plt
import benchmark
from matplotlib.ticker import FuncFormatter, ScalarFormatter

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
    
    min_y = min(min(y_mine), min(y_ref)) if y_mine and y_ref else 5.00
    max_y = max(max(y_mine), max(y_ref)) if y_mine and y_ref else 15.00
    
    plt.loglog(x_mine, y_mine, 'o-', label='My implementation', linewidth=2)
    plt.loglog(x_ref, y_ref, 's--', label='Bin-Dij (reference)', linewidth=2)
    
    def format_k(x, pos):
        if x >= 1000000:
            return f"{int(x/1000000)}M"
        elif x >= 1000:
            return f"{int(x/1000)}k"
        return str(int(x))
    
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_k))
    plt.gca().set_xticks(graph_sizes)
    
    scalar_formatter = ScalarFormatter()
    scalar_formatter.set_scientific(False)
    plt.gca().yaxis.set_major_formatter(scalar_formatter)
    
    y_ticks = [ 0.05, 0.1, 0.3, 0.5, 1, 3, 5, 10, 15]
    
    if max_y > 15:
        y_ticks.extend([ 20, 30, 50, 70, 100])
    
    plt.gca().set_yticks(y_ticks)
    
    plt.title('Performance Comparison: My Implementation vs. Bin-Dij', fontsize=14)
    plt.xlabel('Number of nodes (n)', fontsize=12)
    plt.ylabel('Execution time (seconds)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    for i, txt in enumerate(x_mine):
        plt.annotate(format_k(txt, None), (x_mine[i], y_mine[i]), 
                     textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('dijkstra_comparison.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_comparative(benchmark.results, benchmark.graphLenght)
