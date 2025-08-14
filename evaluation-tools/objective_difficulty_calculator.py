#!/usr/bin/env python3
"""
客観的難易度計算システム
- 100点制約なし
- プロンプト解析による完全自動化
- AI主観排除の機械的判定
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class ObjectiveDifficultyCalculator:
    def __init__(self):
        self.difficulty_factors = {
            # ファイル関連要素（客観的）
            'file_extensions': {
                '.txt': 1,
                '.csv': 3,
                '.json': 5,
                '.yaml': 7,
                '.yml': 7,
                '.py': 8,
                '.html': 6,
                '.md': 4,
                '.xml': 6,
                '.toml': 5,
                '.svg': 4
            },
            
            # 数学・計算関連キーワード（客観的）
            'math_keywords': {
                '四則演算': 2,
                '加算': 1, '減算': 1, '乗算': 1, '除算': 1,
                '平方根': 3, 'sqrt': 3,
                '累乗': 3, 'power': 3,
                '対数': 5, 'log': 5, 'ln': 5,
                '三角関数': 6, 'sin': 6, 'cos': 6, 'tan': 6,
                '積分': 8, 'integral': 8,
                '微分': 8, 'derivative': 8,
                '行列': 10, 'matrix': 10,
                'フィボナッチ': 7, 'fibonacci': 7,
                'モンテカルロ': 12, 'monte carlo': 12,
                '最適化': 10, 'optimization': 10,
                '機械学習': 15, 'machine learning': 15, 'ML': 15,
                'ニューラルネットワーク': 18, 'neural network': 18,
                '統計': 6, 'statistics': 6,
                '確率': 5, 'probability': 5
            },
            
            # システム・技術関連キーワード（客観的）
            'system_keywords': {
                'API': 8,
                'エンタープライズ': 20, 'enterprise': 20,
                'セキュリティ': 10, 'security': 10,
                '監視': 8, 'monitoring': 8,
                'データベース': 12, 'database': 12,
                '並行処理': 15, 'parallel': 15, 'concurrent': 15,
                '非同期': 12, 'async': 12, 'asynchronous': 12,
                'マルチスレッド': 14, 'multithread': 14,
                '分散': 18, 'distributed': 18,
                'クラスター': 16, 'cluster': 16,
                'ETL': 12,
                'パイプライン': 10, 'pipeline': 10
            },
            
            # 精度・品質要求（客観的）
            'precision_patterns': {
                r'小数点第(\d+)位': lambda m: int(m.group(1)) * 2,
                r'誤差(\d+)%以内': lambda m: (100 - int(m.group(1))) / 10,
                r'誤差.*10\^-(\d+)': lambda m: int(m.group(1)) * 3,
                r'精度.*10\^-(\d+)': lambda m: int(m.group(1)) * 3,
                r'カバレッジ(\d+)%': lambda m: int(m.group(1)) / 10
            }
        }
    
    def analyze_prompt(self, prompt_path):
        """プロンプトファイルを解析して難易度要素を抽出"""
        if not os.path.exists(prompt_path):
            return {'error': f'Prompt file not found: {prompt_path}'}
        
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        factors = {
            'file_count_requested': self._count_requested_files(content),
            'folder_count_requested': self._count_requested_folders(content),
            'file_types_score': self._calculate_file_types_score(content),
            'math_complexity_score': self._calculate_math_score(content),
            'system_complexity_score': self._calculate_system_score(content),
            'precision_requirements_score': self._calculate_precision_score(content),
            'text_length': len(content),
            'instruction_count': self._count_instructions(content)
        }
        
        return factors
    
    def _count_requested_files(self, content):
        """要求されるファイル数をカウント"""
        # 「XX個のファイル」「XX files」のパターン
        patterns = [
            r'(\d+)個のファイル',
            r'(\d+)\s*files?',
            r'以下の(\d+)つのファイル',
            r'(\d+)ファイル'
        ]
        
        total_files = 0
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                total_files += int(match)
        
        # 明示的なファイル名の数もカウント
        file_extensions = ['.txt', '.csv', '.json', '.py', '.yaml', '.yml', '.html', '.md']
        for ext in file_extensions:
            total_files += len(re.findall(rf'\w+\{re.escape(ext)}', content))
        
        return total_files
    
    def _count_requested_folders(self, content):
        """要求されるフォルダ数をカウント"""
        patterns = [
            r'(\d+)個のフォルダ',
            r'(\d+)\s*folders?',
            r'以下の(\d+)つのフォルダ'
        ]
        
        total_folders = 0
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                total_folders += int(match)
        
        # フォルダ名の明示的な記載もカウント
        folder_patterns = [r'(\w+)/', r'(\w+)フォルダ']
        for pattern in folder_patterns:
            total_folders += len(set(re.findall(pattern, content)))
        
        return total_folders
    
    def _calculate_file_types_score(self, content):
        """ファイルタイプの複雑度スコア"""
        score = 0
        for ext, points in self.difficulty_factors['file_extensions'].items():
            if ext in content or ext.upper() in content:
                score += points
        return score
    
    def _calculate_math_score(self, content):
        """数学・計算の複雑度スコア"""
        score = 0
        content_lower = content.lower()
        
        for keyword, points in self.difficulty_factors['math_keywords'].items():
            if keyword.lower() in content_lower:
                score += points
        
        return score
    
    def _calculate_system_score(self, content):
        """システム・技術の複雑度スコア"""
        score = 0
        content_lower = content.lower()
        
        for keyword, points in self.difficulty_factors['system_keywords'].items():
            if keyword.lower() in content_lower:
                score += points
        
        return score
    
    def _calculate_precision_score(self, content):
        """精度要求の複雑度スコア"""
        score = 0
        
        for pattern, calc_func in self.difficulty_factors['precision_patterns'].items():
            matches = re.finditer(pattern, content)
            for match in matches:
                score += calc_func(match)
        
        return score
    
    def _count_instructions(self, content):
        """指示数をカウント"""
        # 番号付きリストの検出
        numbered_instructions = len(re.findall(r'^\d+[.)]\s', content, re.MULTILINE))
        
        # 「してください」「してください。」の数
        request_patterns = len(re.findall(r'してください[。.]?', content))
        
        return max(numbered_instructions, request_patterns)
    
    def calculate_difficulty(self, test_folder_path):
        """テストフォルダの難易度を計算"""
        prompt_path = os.path.join(test_folder_path, 'prompt.txt')
        
        factors = self.analyze_prompt(prompt_path)
        
        if 'error' in factors:
            return factors
        
        # 難易度スコア計算（100点制約なし）
        difficulty_score = (
            factors['file_count_requested'] * 2.5 +           # ファイル数要求
            factors['folder_count_requested'] * 3.0 +         # フォルダ数要求
            factors['file_types_score'] * 1.2 +               # ファイルタイプ複雑度
            factors['math_complexity_score'] * 1.5 +          # 数学的複雑度
            factors['system_complexity_score'] * 1.0 +        # システム複雑度
            factors['precision_requirements_score'] * 2.0 +   # 精度要求
            factors['instruction_count'] * 1.8 +              # 指示数
            (factors['text_length'] / 100) * 0.5              # テキスト長（情報量）
        )
        
        return {
            'test_folder': os.path.basename(test_folder_path),
            'difficulty_score': round(difficulty_score, 2),
            'factors': factors,
            'calculated_at': datetime.now().isoformat()
        }
    
    def evaluate_all_tests(self, tests_folder_path):
        """全テストの難易度を評価"""
        results = []
        
        # test1, test2, ... の順序でソート
        test_folders = [d for d in os.listdir(tests_folder_path) 
                       if d.startswith('test') and os.path.isdir(os.path.join(tests_folder_path, d))]
        test_folders.sort(key=lambda x: int(re.findall(r'\d+', x)[0]) if re.findall(r'\d+', x) else 0)
        
        for test_folder in test_folders:
            if test_folder.startswith('.') or test_folder == 'hardly-report':
                continue
                
            test_path = os.path.join(tests_folder_path, test_folder)
            if os.path.isdir(test_path):
                result = self.calculate_difficulty(test_path)
                results.append(result)
        
        return results

def main():
    calculator = ObjectiveDifficultyCalculator()
    
    # テストフォルダのパス
    tests_path = r"C:\Users\user\Desktop\work\90_cc\20250812\claude-manual-test-100\tests"
    
    # 全テストを評価
    results = calculator.evaluate_all_tests(tests_path)
    
    # 結果を表示
    print("=== 客観的難易度計算結果 ===")
    print(f"計算日時: {datetime.now()}")
    print()
    
    total_increase = 0
    prev_score = None
    
    for result in results:
        if 'error' in result:
            print(f"{result['test_folder']}: {result['error']}")
            continue
            
        score = result['difficulty_score']
        change = ""
        if prev_score is not None:
            diff = score - prev_score
            change = f" ({diff:+.2f})"
            total_increase += diff
        
        print(f"{result['test_folder']}: {score:.2f}点{change}")
        
        # 詳細要因（上位3つ）
        factors = result['factors']
        main_factors = [
            f"ファイル数: {factors['file_count_requested']}個",
            f"フォルダ数: {factors['folder_count_requested']}個", 
            f"数学複雑度: {factors['math_complexity_score']}点"
        ]
        print(f"  主要要因: {', '.join(main_factors)}")
        print()
        
        prev_score = score
    
    # 結果をJSONで保存
    output_path = os.path.join(os.path.dirname(tests_path), 'evaluation-tools', 'objective_difficulty_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"詳細結果を保存: {output_path}")
    
    # 統計情報
    if len(results) > 1 and all('error' not in r for r in results):
        scores = [r['difficulty_score'] for r in results if 'error' not in r]
        print(f"\n=== 統計情報 ===")
        print(f"平均難易度: {sum(scores)/len(scores):.2f}点")
        print(f"最小難易度: {min(scores):.2f}点 ({results[scores.index(min(scores))]['test_folder']})")
        print(f"最大難易度: {max(scores):.2f}点 ({results[scores.index(max(scores))]['test_folder']})")
        print(f"難易度レンジ: {max(scores) - min(scores):.2f}点")

if __name__ == "__main__":
    main()