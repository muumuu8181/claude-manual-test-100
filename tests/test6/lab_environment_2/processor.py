#!/usr/bin/env python3
"""
Lab Environment 2 - Matrix Operations Processor
3次元行列演算、固有値分解、QR分解、SVD分解の実装
"""

import numpy as np
import scipy.linalg
import time
import json
import csv
from typing import Dict, List, Tuple, Any, Optional
import logging
import warnings

# 数値計算の警告を抑制
warnings.filterwarnings('ignore', category=np.ComplexWarning)

class Lab2MatrixProcessor:
    """Lab Environment 2の行列演算プロセッサ"""
    
    def __init__(self):
        self.alpha = 427
        self.beta = 256
        self.gamma = 198
        self.delta = 87
        self.epsilon = 64
        self.zeta = 31
        
        # 行列サイズ
        self.matrix_size = 10
        
        # ログ設定
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # 計算結果保存用
        self.matrices = {}
        self.decomposition_results = {}
        
    def generate_3d_matrices(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        3次元行列 A[10x10x10] * B[10x10x10] の生成
        各要素は (α+i)*(β+j)*(γ+k) / (δ*ε*ζ) で初期化
        """
        self.logger.info("3次元行列生成開始")
        start_time = time.perf_counter_ns()
        
        size = self.matrix_size
        denominator = self.delta * self.epsilon * self.zeta
        
        # 行列 A の生成
        matrix_a = np.zeros((size, size, size), dtype=np.float64)
        matrix_b = np.zeros((size, size, size), dtype=np.float64)
        
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    # 行列 A の要素
                    numerator_a = (self.alpha + i) * (self.beta + j) * (self.gamma + k)
                    matrix_a[i, j, k] = numerator_a / denominator
                    
                    # 行列 B の要素（わずかに異なる初期化）
                    numerator_b = (self.alpha + i + 1) * (self.beta + j + 1) * (self.gamma + k + 1)
                    matrix_b[i, j, k] = numerator_b / denominator
        
        end_time = time.perf_counter_ns()
        generation_time = (end_time - start_time) / 1000
        
        self.matrices['matrix_a'] = matrix_a
        self.matrices['matrix_b'] = matrix_b
        
        self.logger.info(f"3次元行列生成完了: 時間={generation_time:.3f}μs")
        
        return matrix_a, matrix_b
        
    def element_wise_multiplication(self, matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
        """要素ごとの積の計算"""
        self.logger.info("要素ごとの積計算開始")
        start_time = time.perf_counter_ns()
        
        element_product = matrix_a * matrix_b
        
        end_time = time.perf_counter_ns()
        computation_time = (end_time - start_time) / 1000
        
        self.matrices['element_product'] = element_product
        
        # 統計情報
        statistics = {
            'min_value': float(np.min(element_product)),
            'max_value': float(np.max(element_product)),
            'mean_value': float(np.mean(element_product)),
            'std_value': float(np.std(element_product)),
            'sum_value': float(np.sum(element_product)),
            'computation_time_microseconds': computation_time
        }
        
        self.logger.info(f"要素ごとの積計算完了: 時間={computation_time:.3f}μs")
        return element_product, statistics
        
    def matrix_flattening_and_reshaping(self, matrix_3d: np.ndarray) -> np.ndarray:
        """3次元行列を2次元行列に変換（固有値分解用）"""
        # 3D行列を2D行列に変換（最初の2次元を使用）
        matrix_2d = matrix_3d.reshape(self.matrix_size, -1)[:, :self.matrix_size]
        return matrix_2d
        
    def eigenvalue_decomposition(self, matrix_2d: np.ndarray) -> Dict[str, Any]:
        """固有値分解の実行"""
        self.logger.info("固有値分解開始")
        start_time = time.perf_counter_ns()
        
        try:
            # 固有値・固有ベクトルの計算
            eigenvalues, eigenvectors = np.linalg.eig(matrix_2d)
            
            # 実数部のみを取得（複素数が含まれる場合）
            eigenvalues_real = np.real(eigenvalues)
            eigenvalues_imag = np.imag(eigenvalues)
            
            # 固有値をソート
            idx = np.argsort(np.abs(eigenvalues_real))[::-1]
            eigenvalues_sorted = eigenvalues_real[idx]
            eigenvectors_sorted = np.real(eigenvectors[:, idx])
            
            # 条件数の計算
            max_eigenvalue = np.max(np.abs(eigenvalues_real))
            min_eigenvalue = np.min(np.abs(eigenvalues_real[eigenvalues_real != 0]))
            condition_number = max_eigenvalue / min_eigenvalue if min_eigenvalue != 0 else np.inf
            
            end_time = time.perf_counter_ns()
            computation_time = (end_time - start_time) / 1000
            
            # 固有値検証（Av = λv）
            verification_errors = []
            for i in range(len(eigenvalues_real)):
                if i < len(eigenvectors_sorted[0]):
                    expected = eigenvalues_real[i] * eigenvectors_sorted[:, i]
                    actual = matrix_2d @ eigenvectors_sorted[:, i]
                    error = np.linalg.norm(actual - expected)
                    verification_errors.append(error)
            
            result = {
                'eigenvalues': eigenvalues_sorted.tolist(),
                'eigenvalues_imaginary': eigenvalues_imag[idx].tolist(),
                'max_eigenvalue': float(max_eigenvalue),
                'min_eigenvalue': float(min_eigenvalue),
                'condition_number': float(condition_number),
                'eigenvectors_shape': eigenvectors_sorted.shape,
                'computation_time_microseconds': computation_time,
                'verification_errors': verification_errors[:5],  # 最初の5個のみ
                'max_verification_error': max(verification_errors) if verification_errors else 0.0,
                'complex_eigenvalues_count': int(np.sum(np.abs(eigenvalues_imag) > 1e-10))
            }
            
            self.decomposition_results['eigenvalue'] = result
            self.logger.info(f"固有値分解完了: 条件数={condition_number:.3e}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"固有値分解エラー: {e}")
            raise
            
    def qr_decomposition(self, matrix_2d: np.ndarray) -> Dict[str, Any]:
        """QR分解の実行"""
        self.logger.info("QR分解開始")
        start_time = time.perf_counter_ns()
        
        try:
            # QR分解（pivoting付き）
            Q, R, P = scipy.linalg.qr(matrix_2d, pivoting=True)
            
            # 標準QR分解（pivoting無し）
            Q_standard, R_standard = np.linalg.qr(matrix_2d)
            
            end_time = time.perf_counter_ns()
            computation_time = (end_time - start_time) / 1000
            
            # 検証: A = QR
            reconstruction_pivoted = Q @ R
            reconstruction_standard = Q_standard @ R_standard
            
            reconstruction_error_pivoted = np.linalg.norm(matrix_2d[:, P] - reconstruction_pivoted)
            reconstruction_error_standard = np.linalg.norm(matrix_2d - reconstruction_standard)
            
            # 直交性検証: Q^T * Q = I
            orthogonality_error_pivoted = np.linalg.norm(Q.T @ Q - np.eye(Q.shape[1]))
            orthogonality_error_standard = np.linalg.norm(Q_standard.T @ Q_standard - np.eye(Q_standard.shape[1]))
            
            result = {
                'q_matrix_shape': Q.shape,
                'r_matrix_shape': R.shape,
                'pivot_vector': P.tolist(),
                'q_determinant': float(np.linalg.det(Q)),
                'r_diagonal': np.diag(R).tolist(),
                'computation_time_microseconds': computation_time,
                'reconstruction_error_pivoted': float(reconstruction_error_pivoted),
                'reconstruction_error_standard': float(reconstruction_error_standard),
                'orthogonality_error_pivoted': float(orthogonality_error_pivoted),
                'orthogonality_error_standard': float(orthogonality_error_standard),
                'pivoting_used': True,
                'matrix_rank_estimate': int(np.sum(np.abs(np.diag(R)) > 1e-12))
            }
            
            self.decomposition_results['qr'] = result
            self.matrices['Q'] = Q
            self.matrices['R'] = R
            
            self.logger.info(f"QR分解完了: 再構成誤差={reconstruction_error_pivoted:.3e}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"QR分解エラー: {e}")
            raise
            
    def svd_decomposition(self, matrix_2d: np.ndarray) -> Dict[str, Any]:
        """SVD分解の実行"""
        self.logger.info("SVD分解開始")
        start_time = time.perf_counter_ns()
        
        try:
            # SVD分解
            U, s, Vt = np.linalg.svd(matrix_2d, full_matrices=False)
            
            end_time = time.perf_counter_ns()
            computation_time = (end_time - start_time) / 1000
            
            # 再構成検証: A = U * S * Vt
            S_matrix = np.diag(s)
            reconstruction = U @ S_matrix @ Vt
            reconstruction_error = np.linalg.norm(matrix_2d - reconstruction)
            
            # 特異値の分析
            condition_number_svd = s[0] / s[-1] if s[-1] > 1e-16 else np.inf
            effective_rank = int(np.sum(s > 1e-12))
            
            # 直交性検証
            u_orthogonality = np.linalg.norm(U.T @ U - np.eye(U.shape[1]))
            v_orthogonality = np.linalg.norm(Vt @ Vt.T - np.eye(Vt.shape[0]))
            
            result = {
                'u_matrix_shape': U.shape,
                'singular_values': s.tolist(),
                'vt_matrix_shape': Vt.shape,
                'max_singular_value': float(s[0]),
                'min_singular_value': float(s[-1]),
                'condition_number_svd': float(condition_number_svd),
                'effective_rank': effective_rank,
                'computation_time_microseconds': computation_time,
                'reconstruction_error': float(reconstruction_error),
                'u_orthogonality_error': float(u_orthogonality),
                'v_orthogonality_error': float(v_orthogonality),
                'frobenius_norm': float(np.linalg.norm(matrix_2d, 'fro')),
                'nuclear_norm': float(np.sum(s))
            }
            
            self.decomposition_results['svd'] = result
            self.matrices['U'] = U
            self.matrices['s'] = s
            self.matrices['Vt'] = Vt
            
            self.logger.info(f"SVD分解完了: 条件数={condition_number_svd:.3e}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"SVD分解エラー: {e}")
            raise
            
    def compare_decomposition_methods(self) -> Dict[str, Any]:
        """分解手法の比較分析"""
        if 'eigenvalue' not in self.decomposition_results or 'qr' not in self.decomposition_results or 'svd' not in self.decomposition_results:
            raise ValueError("すべての分解結果が必要です")
            
        eigen_result = self.decomposition_results['eigenvalue']
        qr_result = self.decomposition_results['qr']
        svd_result = self.decomposition_results['svd']
        
        comparison = {
            'condition_number_comparison': {
                'eigenvalue_method': eigen_result['condition_number'],
                'svd_method': svd_result['condition_number_svd'],
                'difference': abs(eigen_result['condition_number'] - svd_result['condition_number_svd'])
            },
            'computation_time_comparison': {
                'eigenvalue_time': eigen_result['computation_time_microseconds'],
                'qr_time': qr_result['computation_time_microseconds'],
                'svd_time': svd_result['computation_time_microseconds'],
                'fastest_method': min(
                    eigen_result['computation_time_microseconds'],
                    qr_result['computation_time_microseconds'],
                    svd_result['computation_time_microseconds']
                )
            },
            'accuracy_comparison': {
                'eigenvalue_max_error': eigen_result['max_verification_error'],
                'qr_reconstruction_error': qr_result['reconstruction_error_pivoted'],
                'svd_reconstruction_error': svd_result['reconstruction_error'],
                'most_accurate_method': 'SVD' if svd_result['reconstruction_error'] < min(
                    eigen_result['max_verification_error'],
                    qr_result['reconstruction_error_pivoted']
                ) else 'Eigenvalue'
            },
            'numerical_stability': {
                'qr_orthogonality': qr_result['orthogonality_error_pivoted'],
                'svd_u_orthogonality': svd_result['u_orthogonality_error'],
                'svd_v_orthogonality': svd_result['v_orthogonality_error']
            }
        }
        
        return comparison
        
    def run_full_computation(self) -> Dict[str, Any]:
        """完全な行列計算実行"""
        self.logger.info("Lab Environment 2 完全計算開始")
        
        # 3次元行列生成
        matrix_a, matrix_b = self.generate_3d_matrices()
        
        # 要素ごとの積
        element_product, product_stats = self.element_wise_multiplication(matrix_a, matrix_b)
        
        # 2次元行列への変換
        matrix_2d = self.matrix_flattening_and_reshaping(element_product)
        
        # 各種分解の実行
        eigenvalue_result = self.eigenvalue_decomposition(matrix_2d)
        qr_result = self.qr_decomposition(matrix_2d)
        svd_result = self.svd_decomposition(matrix_2d)
        
        # 分解手法の比較
        comparison_result = self.compare_decomposition_methods()
        
        # 結果統合
        full_result = {
            'environment': 'lab_environment_2',
            'parameters': {
                'alpha': self.alpha,
                'beta': self.beta,
                'gamma': self.gamma,
                'delta': self.delta,
                'epsilon': self.epsilon,
                'zeta': self.zeta
            },
            'matrix_properties': {
                'original_shape': matrix_a.shape,
                'flattened_shape': matrix_2d.shape,
                'element_product_statistics': product_stats
            },
            'eigenvalue_decomposition': eigenvalue_result,
            'qr_decomposition': qr_result,
            'svd_decomposition': svd_result,
            'decomposition_comparison': comparison_result,
            'total_computation_time': sum([
                eigenvalue_result['computation_time_microseconds'],
                qr_result['computation_time_microseconds'],
                svd_result['computation_time_microseconds']
            ])
        }
        
        self.logger.info("Lab Environment 2 完全計算完了")
        return full_result

def main():
    """メイン実行関数"""
    processor = Lab2MatrixProcessor()
    
    try:
        # 計算実行
        results = processor.run_full_computation()
        
        # 結果保存
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
            
        # メトリクス保存
        metrics_data = [
            ['metric_name', 'value', 'unit', 'timestamp'],
            ['max_eigenvalue', results['eigenvalue_decomposition']['max_eigenvalue'], 'numeric', time.time()],
            ['min_eigenvalue', results['eigenvalue_decomposition']['min_eigenvalue'], 'numeric', time.time()],
            ['condition_number', results['eigenvalue_decomposition']['condition_number'], 'numeric', time.time()],
            ['qr_reconstruction_error', results['qr_decomposition']['reconstruction_error_pivoted'], 'numeric', time.time()],
            ['svd_reconstruction_error', results['svd_decomposition']['reconstruction_error'], 'numeric', time.time()],
            ['total_computation_time', results['total_computation_time'], 'microseconds', time.time()]
        ]
        
        with open('metrics.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(metrics_data)
            
        print("計算完了。結果はresults.jsonとmetrics.csvに保存されました。")
        print(f"条件数: {results['eigenvalue_decomposition']['condition_number']:.3e}")
        print(f"最大固有値: {results['eigenvalue_decomposition']['max_eigenvalue']:.6f}")
        
    except Exception as e:
        logging.error(f"計算実行中にエラー: {e}")
        raise

if __name__ == "__main__":
    main()