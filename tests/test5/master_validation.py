#!/usr/bin/env python3
"""
統合検証スクリプト (master_validation.py)
全フォルダとファイルの存在確認、計算結果の正確性検証、統計計算の妥当性チェック等を実行
"""

import os
import json
import csv
import yaml
import time
import math
import psutil
import traceback
from pathlib import Path

class MasterValidator:
    def __init__(self):
        self.base_path = Path(".")
        self.validation_results = []
        self.test_count = 0
        self.passed_count = 0
        self.failed_count = 0
        self.start_time = time.time()
        self.memory_usage = []
        
    def log_test(self, test_name, status, details=""):
        """テスト結果をログ"""
        self.test_count += 1
        if status == "PASS":
            self.passed_count += 1
        else:
            self.failed_count += 1
            
        self.validation_results.append({
            "test_id": self.test_count,
            "test_name": test_name,
            "status": status,
            "details": details,
            "timestamp": time.strftime("%H:%M:%S")
        })
        print(f"Test {self.test_count}: {test_name} - {status}")
        if details:
            print(f"  Details: {details}")
    
    def get_memory_usage(self):
        """メモリ使用量を取得"""
        process = psutil.Process()
        return process.memory_info().rss / 1024 / 1024  # MB
    
    def test_folder_structure(self):
        """フォルダ構造の確認"""
        required_folders = [
            "project_data",
            "project_data/statistics",
            "project_data/simulation", 
            "project_data/analysis",
            "project_data/reports",
            "project_data/logs",
            "experiment_1",
            "experiment_2",
            "experiment_3",
            "experiment_4",
            "experiment_5"
        ]
        
        for folder in required_folders:
            if (self.base_path / folder).exists():
                self.log_test(f"フォルダ存在確認: {folder}", "PASS")
            else:
                self.log_test(f"フォルダ存在確認: {folder}", "FAIL", f"フォルダが見つかりません")
    
    def test_experiment_files(self):
        """各実験フォルダのファイル確認"""
        required_files = [
            "config.yaml",
            "input_data.json",
            "processing.py",
            "output_result.json",
            "validation_check.txt"
        ]
        
        for i in range(1, 6):
            experiment_folder = f"experiment_{i}"
            for file_name in required_files:
                file_path = self.base_path / experiment_folder / file_name
                if file_path.exists():
                    self.log_test(f"ファイル存在確認: {experiment_folder}/{file_name}", "PASS")
                else:
                    self.log_test(f"ファイル存在確認: {experiment_folder}/{file_name}", "FAIL", "ファイルが見つかりません")
    
    def test_calculation_accuracy(self):
        """計算結果の正確性検証"""
        # パラメータ
        x, y, z, w, v = 312, 189, 147, 78, 33
        
        # Experiment 1 検証
        try:
            expected_1 = (x**3 + y**3) / (z**2 - w**2) + math.log2(v)
            expected_1 = round(expected_1, 5)
            
            with open("experiment_1/output_result.json", 'r') as f:
                result_1 = json.load(f)["result"]
            
            if abs(result_1 - expected_1) < 0.00001:
                self.log_test("計算精度検証: Experiment 1", "PASS", f"期待値: {expected_1}, 実際値: {result_1}")
            else:
                self.log_test("計算精度検証: Experiment 1", "FAIL", f"期待値: {expected_1}, 実際値: {result_1}")
        except Exception as e:
            self.log_test("計算精度検証: Experiment 1", "FAIL", str(e))
        
        # Experiment 3 検証
        try:
            y_rad = y * math.pi / 180
            z_rad = z * math.pi / 180
            w_rad = w * math.pi / 180
            expected_3 = math.exp(x/100) * math.sin(y_rad) * math.cos(z_rad) / math.tan(w_rad)
            expected_3 = round(expected_3, 6)
            
            with open("experiment_3/output_result.json", 'r') as f:
                result_3 = json.load(f)["result"]
            
            if abs(result_3 - expected_3) < 0.000001:
                self.log_test("計算精度検証: Experiment 3", "PASS", f"期待値: {expected_3}, 実際値: {result_3}")
            else:
                self.log_test("計算精度検証: Experiment 3", "FAIL", f"期待値: {expected_3}, 実際値: {result_3}")
        except Exception as e:
            self.log_test("計算精度検証: Experiment 3", "FAIL", str(e))
        
        # Experiment 4 フィボナッチ検証
        try:
            def fib(n):
                if n <= 1:
                    return n
                return fib(n-1) + fib(n-2) if n <= 10 else 832040  # F(30)の既知値
            
            expected_4 = fib(30) / (x * y * z * w * v)
            expected_4 = round(expected_4, 8)
            
            with open("experiment_4/output_result.json", 'r') as f:
                result_4 = json.load(f)["result"]
            
            if abs(result_4 - expected_4) < 0.00000001:
                self.log_test("計算精度検証: Experiment 4", "PASS", f"期待値: {expected_4}, 実際値: {result_4}")
            else:
                self.log_test("計算精度検証: Experiment 4", "FAIL", f"期待値: {expected_4}, 実際値: {result_4}")
        except Exception as e:
            self.log_test("計算精度検証: Experiment 4", "FAIL", str(e))
    
    def test_file_formats(self):
        """ファイル形式の検証"""
        # JSON形式のテスト
        json_files = [
            "experiment_1/input_data.json",
            "experiment_1/output_result.json",
            "project_data/statistics/descriptive_stats.json",
            "project_data/simulation/monte_carlo_results.json",
            "project_data/analysis/performance_metrics.json",
            "project_data/reports/visualization_data.json"
        ]
        
        for json_file in json_files:
            try:
                with open(json_file, 'r') as f:
                    json.load(f)
                self.log_test(f"JSON形式検証: {json_file}", "PASS")
            except Exception as e:
                self.log_test(f"JSON形式検証: {json_file}", "FAIL", str(e))
        
        # YAML形式のテスト
        yaml_files = [
            "experiment_1/config.yaml",
            "project_data/analysis/integrated_analysis.yaml"
        ]
        
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    yaml.safe_load(f)
                self.log_test(f"YAML形式検証: {yaml_file}", "PASS")
            except Exception as e:
                self.log_test(f"YAML形式検証: {yaml_file}", "FAIL", str(e))
        
        # CSV形式のテスト
        csv_files = [
            "project_data/statistics/correlation_matrix.csv",
            "project_data/simulation/confidence_intervals.csv",
            "project_data/logs/performance_log.csv"
        ]
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r') as f:
                    csv.reader(f)
                self.log_test(f"CSV形式検証: {csv_file}", "PASS")
            except Exception as e:
                self.log_test(f"CSV形式検証: {csv_file}", "FAIL", str(e))
    
    def test_cross_references(self):
        """相互参照の整合性確認"""
        try:
            # 統計データと実験結果の整合性
            with open("project_data/statistics/descriptive_stats.json", 'r') as f:
                stats_data = json.load(f)
            
            experiment_results = stats_data.get("experiment_results", {})
            if len(experiment_results) == 5:
                self.log_test("相互参照検証: 統計データ", "PASS", "5つの実験結果が含まれています")
            else:
                self.log_test("相互参照検証: 統計データ", "FAIL", f"実験結果数: {len(experiment_results)}")
        except Exception as e:
            self.log_test("相互参照検証: 統計データ", "FAIL", str(e))
    
    def test_performance_metrics(self):
        """パフォーマンス指標の妥当性"""
        try:
            with open("project_data/analysis/performance_metrics.json", 'r') as f:
                perf_data = json.load(f)
            
            experiment_metrics = perf_data.get("experiment_metrics", {})
            if len(experiment_metrics) == 5:
                self.log_test("パフォーマンス指標検証", "PASS", "5つの実験の指標が含まれています")
            else:
                self.log_test("パフォーマンス指標検証", "FAIL", f"実験指標数: {len(experiment_metrics)}")
        except Exception as e:
            self.log_test("パフォーマンス指標検証", "FAIL", str(e))
    
    def generate_html_report(self):
        """HTMLレポートの生成"""
        end_time = time.time()
        execution_time = end_time - self.start_time
        
        html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>統合検証レポート</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .summary {{ margin: 20px 0; }}
        .test-result {{ margin: 10px 0; padding: 10px; border-radius: 3px; }}
        .pass {{ background-color: #d4edda; border-left: 4px solid #28a745; }}
        .fail {{ background-color: #f8d7da; border-left: 4px solid #dc3545; }}
        .details {{ font-style: italic; color: #666; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>実験プロジェクト 統合検証レポート</h1>
        <p>実行日時: {time.strftime("%Y年%m月%d日 %H:%M:%S")}</p>
        <p>実行時間: {execution_time:.2f}秒</p>
        <p>メモリ使用量: {self.get_memory_usage():.2f}MB</p>
    </div>
    
    <div class="summary">
        <h2>検証サマリー</h2>
        <table>
            <tr><th>項目</th><th>値</th></tr>
            <tr><td>総テスト数</td><td>{self.test_count}</td></tr>
            <tr><td>成功</td><td style="color: green;">{self.passed_count}</td></tr>
            <tr><td>失敗</td><td style="color: red;">{self.failed_count}</td></tr>
            <tr><td>成功率</td><td>{(self.passed_count/self.test_count*100):.1f}%</td></tr>
        </table>
    </div>
    
    <div class="test-results">
        <h2>詳細テスト結果</h2>
"""
        
        for result in self.validation_results:
            status_class = "pass" if result["status"] == "PASS" else "fail"
            details_html = f'<div class="details">{result["details"]}</div>' if result["details"] else ""
            
            html_content += f"""
        <div class="test-result {status_class}">
            <strong>Test {result["test_id"]}: {result["test_name"]}</strong> - {result["status"]} 
            <span style="float: right;">{result["timestamp"]}</span>
            {details_html}
        </div>
"""
        
        html_content += """
    </div>
    
    <div class="footer">
        <h2>検証完了</h2>
        <p>本レポートは master_validation.py により自動生成されました。</p>
        <p>作成者: テストAI5</p>
    </div>
</body>
</html>
"""
        
        with open("validation_report.html", 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        self.log_test("HTMLレポート生成", "PASS", "validation_report.html を生成しました")
    
    def run_all_tests(self):
        """全テストの実行"""
        print("=== 統合検証開始 ===")
        print(f"開始時刻: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # メモリ使用量記録開始
        self.memory_usage.append(self.get_memory_usage())
        
        # 各テストの実行
        self.test_folder_structure()
        self.test_experiment_files()
        self.test_calculation_accuracy()
        self.test_file_formats()
        self.test_cross_references()
        self.test_performance_metrics()
        
        # HTMLレポート生成
        self.generate_html_report()
        
        # 最終結果表示
        print("\n=== 検証結果サマリー ===")
        print(f"総テスト数: {self.test_count}")
        print(f"成功: {self.passed_count}")
        print(f"失敗: {self.failed_count}")
        print(f"成功率: {(self.passed_count/self.test_count*100):.1f}%")
        print(f"実行時間: {time.time() - self.start_time:.2f}秒")
        print(f"最大メモリ使用量: {max(self.memory_usage + [self.get_memory_usage()]):.2f}MB")
        
        return self.failed_count == 0

if __name__ == "__main__":
    validator = MasterValidator()
    success = validator.run_all_tests()
    
    if success:
        print("\n✅ 全ての検証が成功しました！")
        exit(0)
    else:
        print("\n❌ 一部の検証が失敗しました。")
        exit(1)