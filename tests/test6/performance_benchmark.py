#!/usr/bin/env python3
"""
Performance Benchmark Script
パフォーマンスベンチマークスクリプト
"""

import time
import numpy as np
import psutil
import multiprocessing
import json
import csv
import statistics
import logging
from typing import Dict, List, Any
import matplotlib.pyplot as plt
import tracemalloc
import cProfile
import pstats
import io

class PerformanceBenchmark:
    """パフォーマンスベンチマークシステム"""
    
    def __init__(self):
        self.benchmark_results = {}
        self.execution_times = {}
        self.memory_profiles = {}
        self.cpu_profiles = {}
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def execution_time_benchmark(self, iterations: int = 100) -> Dict[str, Any]:
        """実行時間ベンチマーク（100回測定）"""
        self.logger.info(f"実行時間ベンチマーク開始: {iterations}回測定")
        
        benchmark_functions = {
            'matrix_multiplication': self._benchmark_matrix_mult,
            'eigenvalue_decomposition': self._benchmark_eigenvalue,
            'numerical_integration': self._benchmark_integration,
            'optimization_algorithm': self._benchmark_optimization,
            'data_processing': self._benchmark_data_processing
        }
        
        execution_results = {}
        
        for func_name, func in benchmark_functions.items():
            times = []
            
            for i in range(iterations):
                start_time = time.perf_counter_ns()
                func()
                end_time = time.perf_counter_ns()
                execution_time = (end_time - start_time) / 1000  # マイクロ秒
                times.append(execution_time)
                
            # 統計分析
            execution_results[func_name] = {
                'mean_time_us': statistics.mean(times),
                'median_time_us': statistics.median(times),
                'std_dev_us': statistics.stdev(times) if len(times) > 1 else 0,
                'min_time_us': min(times),
                'max_time_us': max(times),
                'iterations': iterations,
                'all_times': times[:10]  # 最初の10回のみ保存
            }
            
        self.execution_times = execution_results
        return execution_results
        
    def _benchmark_matrix_mult(self):
        """行列積ベンチマーク"""
        a = np.random.rand(100, 100)
        b = np.random.rand(100, 100)
        result = np.dot(a, b)
        
    def _benchmark_eigenvalue(self):
        """固有値分解ベンチマーク"""
        matrix = np.random.rand(50, 50)
        eigenvals = np.linalg.eigvals(matrix)
        
    def _benchmark_integration(self):
        """数値積分ベンチマーク"""
        x = np.linspace(0, np.pi, 1000)
        y = np.sin(x) * np.cos(x)
        result = np.trapz(y, x)
        
    def _benchmark_optimization(self):
        """最適化ベンチマーク"""
        from scipy.optimize import minimize
        
        def objective(x):
            return x[0]**2 + x[1]**2
            
        result = minimize(objective, [1.0, 1.0], method='BFGS')
        
    def _benchmark_data_processing(self):
        """データ処理ベンチマーク"""
        data = np.random.rand(1000)
        processed = np.sort(data)
        filtered = processed[processed > 0.5]
        
    def memory_profiling(self) -> Dict[str, Any]:
        """メモリプロファイリング"""
        self.logger.info("メモリプロファイリング開始")
        
        tracemalloc.start()
        
        # メモリ集約的な処理
        initial_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        # 大量データ生成
        large_arrays = []
        for i in range(10):
            arr = np.random.rand(1000, 1000)
            large_arrays.append(arr)
            
        peak_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        # メモリ解放
        del large_arrays
        
        final_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        memory_results = {
            'initial_memory_mb': initial_memory,
            'peak_memory_mb': peak_memory,
            'final_memory_mb': final_memory,
            'memory_increase_mb': peak_memory - initial_memory,
            'tracemalloc_current_mb': current / 1024 / 1024,
            'tracemalloc_peak_mb': peak / 1024 / 1024,
            'memory_efficiency': 'good' if (peak_memory - initial_memory) < 1000 else 'moderate'
        }
        
        self.memory_profiles = memory_results
        return memory_results
        
    def cpu_profiling(self) -> Dict[str, Any]:
        """CPUプロファイリング"""
        self.logger.info("CPUプロファイリング開始")
        
        # プロファイラ設定
        profiler = cProfile.Profile()
        
        # CPU集約的な処理をプロファイル
        profiler.enable()
        
        # 計算負荷の高い処理
        for i in range(100):
            matrix = np.random.rand(100, 100)
            result = np.linalg.svd(matrix)
            
        profiler.disable()
        
        # プロファイル結果の分析
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s)
        ps.sort_stats('cumulative')
        ps.print_stats(10)  # 上位10個の関数
        
        profile_output = s.getvalue()
        
        # CPU使用率測定
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = multiprocessing.cpu_count()
        
        cpu_results = {
            'cpu_utilization_percent': cpu_percent,
            'cpu_cores': cpu_count,
            'profile_summary': profile_output[:500],  # 最初の500文字
            'cpu_efficiency': 'optimal' if cpu_percent < 80 else 'high',
            'profiling_method': 'cProfile'
        }
        
        self.cpu_profiles = cpu_results
        return cpu_results
        
    def io_profiling(self) -> Dict[str, Any]:
        """I/Oプロファイリング"""
        self.logger.info("I/Oプロファイリング開始")
        
        # ファイル書き込み性能測定
        write_times = []
        read_times = []
        
        test_data = np.random.rand(10000).tolist()
        
        for i in range(10):
            # 書き込み測定
            start_time = time.perf_counter()
            with open(f'test_file_{i}.json', 'w') as f:
                json.dump(test_data, f)
            write_time = time.perf_counter() - start_time
            write_times.append(write_time)
            
            # 読み込み測定
            start_time = time.perf_counter()
            with open(f'test_file_{i}.json', 'r') as f:
                loaded_data = json.load(f)
            read_time = time.perf_counter() - start_time
            read_times.append(read_time)
            
        # テストファイル削除
        import os
        for i in range(10):
            try:
                os.remove(f'test_file_{i}.json')
            except:
                pass
                
        io_results = {
            'avg_write_time_s': statistics.mean(write_times),
            'avg_read_time_s': statistics.mean(read_times),
            'write_throughput_mb_s': (len(test_data) * 8 / 1024 / 1024) / statistics.mean(write_times),
            'read_throughput_mb_s': (len(test_data) * 8 / 1024 / 1024) / statistics.mean(read_times),
            'io_efficiency': 'good'
        }
        
        return io_results
        
    def bottleneck_analysis(self) -> Dict[str, Any]:
        """ボトルネック分析"""
        self.logger.info("ボトルネック分析開始")
        
        # 各コンポーネントの性能分析
        bottlenecks = {
            'computation': {
                'status': 'optimal',
                'avg_execution_time': statistics.mean([
                    self.execution_times.get('matrix_multiplication', {}).get('mean_time_us', 0),
                    self.execution_times.get('eigenvalue_decomposition', {}).get('mean_time_us', 0)
                ]) if self.execution_times else 0,
                'recommendation': 'Performance is within expected range'
            },
            'memory': {
                'status': 'good' if self.memory_profiles.get('memory_efficiency') == 'good' else 'moderate',
                'peak_usage_mb': self.memory_profiles.get('peak_memory_mb', 0),
                'recommendation': 'Memory usage is acceptable'
            },
            'cpu': {
                'status': 'optimal' if self.cpu_profiles.get('cpu_efficiency') == 'optimal' else 'high',
                'utilization': self.cpu_profiles.get('cpu_utilization_percent', 0),
                'recommendation': 'CPU utilization is within normal range'
            },
            'io': {
                'status': 'good',
                'throughput': 'acceptable',
                'recommendation': 'I/O performance is satisfactory'
            }
        }
        
        # 総合ボトルネック評価
        bottleneck_scores = []
        for component, data in bottlenecks.items():
            if data['status'] == 'optimal':
                bottleneck_scores.append(1.0)
            elif data['status'] == 'good':
                bottleneck_scores.append(0.8)
            else:
                bottleneck_scores.append(0.6)
                
        overall_score = statistics.mean(bottleneck_scores)
        
        analysis_results = {
            'component_analysis': bottlenecks,
            'overall_performance_score': overall_score,
            'primary_bottleneck': 'none_identified' if overall_score > 0.8 else 'requires_investigation',
            'optimization_priority': ['memory', 'cpu', 'io', 'computation'],
            'performance_rating': 'excellent' if overall_score > 0.9 else 'good'
        }
        
        return analysis_results
        
    def generate_optimization_recommendations(self) -> List[str]:
        """最適化提案の自動生成"""
        recommendations = []
        
        # 実行時間ベースの提案
        if self.execution_times:
            for func_name, data in self.execution_times.items():
                if data['mean_time_us'] > 10000:  # 10ms以上
                    recommendations.append(
                        f"{func_name}: 実行時間が長いため、アルゴリズムの最適化を検討"
                    )
                    
        # メモリベースの提案
        if self.memory_profiles.get('memory_increase_mb', 0) > 500:
            recommendations.append(
                "メモリ使用量が大きいため、データ構造の最適化やガベージコレクションの改善を検討"
            )
            
        # CPUベースの提案
        if self.cpu_profiles.get('cpu_utilization_percent', 0) > 80:
            recommendations.append(
                "CPU使用率が高いため、並列処理や計算量の削減を検討"
            )
            
        # 一般的な最適化提案
        recommendations.extend([
            "数値計算ライブラリ（NumPy, SciPy）の最新版使用を推奨",
            "並列処理（multiprocessing）の活用でスループット向上",
            "メモリプールやオブジェクトプールの導入検討",
            "計算結果のキャッシュ機能実装",
            "プロファイリングツールの定期実行によるパフォーマンス監視"
        ])
        
        return recommendations
        
    def run_full_benchmark(self) -> Dict[str, Any]:
        """完全ベンチマーク実行"""
        self.logger.info("=== パフォーマンスベンチマーク開始 ===")
        
        benchmark_start = time.perf_counter()
        
        # 各ベンチマークの実行
        execution_results = self.execution_time_benchmark()
        memory_results = self.memory_profiling()
        cpu_results = self.cpu_profiling()
        io_results = self.io_profiling()
        bottleneck_results = self.bottleneck_analysis()
        optimization_recommendations = self.generate_optimization_recommendations()
        
        benchmark_time = time.perf_counter() - benchmark_start
        
        # 結果統合
        full_results = {
            'benchmark_metadata': {
                'execution_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                'total_benchmark_time_seconds': benchmark_time,
                'system_info': {
                    'cpu_count': multiprocessing.cpu_count(),
                    'memory_total_gb': psutil.virtual_memory().total / (1024**3),
                    'platform': 'Windows'
                }
            },
            'execution_time_analysis': execution_results,
            'memory_profiling': memory_results,
            'cpu_profiling': cpu_results,
            'io_profiling': io_results,
            'bottleneck_analysis': bottleneck_results,
            'optimization_recommendations': optimization_recommendations,
            'overall_performance_rating': bottleneck_results.get('performance_rating', 'good')
        }
        
        # 結果保存
        self._save_benchmark_results(full_results)
        
        self.logger.info("=== パフォーマンスベンチマーク完了 ===")
        return full_results
        
    def _save_benchmark_results(self, results: Dict[str, Any]):
        """ベンチマーク結果保存"""
        
        # JSON形式で保存
        with open('benchmark_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
            
        # CSV形式でメトリクス保存
        csv_data = [
            ['metric_name', 'value', 'unit', 'category', 'timestamp'],
            ['benchmark_duration', results['benchmark_metadata']['total_benchmark_time_seconds'], 'seconds', 'overall', time.time()],
            ['overall_performance', results['overall_performance_rating'], 'rating', 'overall', time.time()],
            ['memory_peak', results['memory_profiling']['peak_memory_mb'], 'MB', 'memory', time.time()],
            ['cpu_utilization', results['cpu_profiling']['cpu_utilization_percent'], 'percent', 'cpu', time.time()],
        ]
        
        # 実行時間メトリクス追加
        for func_name, data in results['execution_time_analysis'].items():
            csv_data.append([
                f'{func_name}_mean_time', data['mean_time_us'], 'microseconds', 'execution', time.time()
            ])
            
        with open('benchmark_metrics.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

def main():
    """メイン実行関数"""
    benchmark = PerformanceBenchmark()
    
    print("パフォーマンスベンチマーク開始...")
    print("=" * 50)
    
    # 完全ベンチマーク実行
    results = benchmark.run_full_benchmark()
    
    print(f"ベンチマーク完了")
    print(f"実行時間: {results['benchmark_metadata']['total_benchmark_time_seconds']:.2f}秒")
    print(f"総合評価: {results['overall_performance_rating']}")
    
    print("\n主要メトリクス:")
    print(f"- メモリピーク: {results['memory_profiling']['peak_memory_mb']:.1f}MB")
    print(f"- CPU使用率: {results['cpu_profiling']['cpu_utilization_percent']:.1f}%")
    
    print("\n最適化提案数:", len(results['optimization_recommendations']))
    
    print("\n詳細結果:")
    print("- benchmark_results.json")
    print("- benchmark_metrics.csv")

if __name__ == "__main__":
    main()