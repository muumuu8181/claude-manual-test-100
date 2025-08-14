#!/usr/bin/env python3
"""
シンプル指示項目カウント式難易度計算システム
- AI特性に基づく等価重み付け
- 指示の実行項目数を純粋にカウント
- 「何をするか」ではなく「いくつの指示を実行するか」で評価
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class SimpleInstructionCounter:
    def __init__(self):
        # 指示パターンの検出ルール（等価重み）
        self.instruction_patterns = [
            # ファイル・フォルダ作成指示
            r'(\d+)個のファイル',
            r'(\d+)個のフォルダ',
            r'(\d+)\s*ファイル',
            r'(\d+)\s*フォルダ',
            r'(\d+)\s*files?',
            r'(\d+)\s*folders?',
            
            # 番号付き指示リスト
            r'^\s*(\d+)[.)]\s',  # 1) または 1. の形式
            
            # 計算指示
            r'計算[：:]',
            r'を計算',
            r'結果を',
            
            # 作成指示
            r'作成してください',
            r'作成し',
            r'を作成',
            
            # 実装指示
            r'実装してください',
            r'実装し',
            r'を実装',
            
            # 記録・保存指示
            r'記録してください',
            r'保存してください',
            r'として保存',
            
            # 検証・テスト指示
            r'検証してください',
            r'テストしてください',
            r'確認してください',
            
            # 分析・評価指示
            r'分析してください',
            r'評価してください',
            r'測定してください'
        ]
    
    def count_instructions(self, prompt_path):
        """プロンプトファイルから指示項目数をカウント"""
        if not os.path.exists(prompt_path):
            return {'error': f'Prompt file not found: {prompt_path}'}
        
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        instruction_count = 0
        detected_patterns = []
        
        # 番号付きリストの検出（最も信頼性が高い）
        numbered_lines = re.findall(r'^\s*(\d+)[.)]\s.*$', content, re.MULTILINE)
        if numbered_lines:
            instruction_count = max(int(num) for num in numbered_lines)
            detected_patterns.append(f"番号付きリスト: {instruction_count}項目")
        
        # 具体的な数量指示のカウント
        file_counts = []
        folder_counts = []
        
        # ファイル数の検出
        file_patterns = [r'(\d+)個のファイル', r'(\d+)\s*ファイル', r'(\d+)\s*files?']
        for pattern in file_patterns:
            matches = re.findall(pattern, content)
            file_counts.extend([int(m) for m in matches])
        
        # フォルダ数の検出
        folder_patterns = [r'(\d+)個のフォルダ', r'(\d+)\s*フォルダ', r'(\d+)\s*folders?']
        for pattern in folder_patterns:
            matches = re.findall(pattern, content)
            folder_counts.extend([int(m) for m in matches])
        
        # 明示的なファイル名の検出
        explicit_files = len(re.findall(r'\w+\.(txt|csv|json|py|yaml|yml|html|md|xml|toml)', content))
        
        # 明示的なフォルダ名の検出
        explicit_folders = len(set(re.findall(r'(\w+)/', content)))
        
        # 動詞ベースの指示カウント
        action_patterns = [
            '作成してください', '実装してください', '記録してください', 
            '保存してください', '計算してください', '検証してください',
            'テストしてください', '確認してください', '分析してください',
            '評価してください', '測定してください'
        ]
        
        action_count = 0
        for pattern in action_patterns:
            action_count += len(re.findall(pattern, content))
        
        # 最終的な指示項目数の決定
        # 番号付きリストがある場合はそれを優先、なければ他の指標を合計
        if instruction_count > 0:
            final_count = instruction_count
            method = "番号付きリスト方式"
        else:
            # 複数の指標から推定
            total_file_items = sum(file_counts) + explicit_files
            total_folder_items = sum(folder_counts) + explicit_folders
            
            estimated_count = total_file_items + total_folder_items + action_count
            final_count = max(estimated_count, 1)  # 最低1項目
            method = "複合推定方式"
        
        return {
            'instruction_count': final_count,
            'detection_method': method,
            'details': {
                'numbered_list_max': max([int(num) for num in numbered_lines]) if numbered_lines else 0,
                'file_count_requests': file_counts,
                'folder_count_requests': folder_counts,
                'explicit_files': explicit_files,
                'explicit_folders': explicit_folders,
                'action_verbs': action_count,
                'text_length': len(content)
            },
            'detected_patterns': detected_patterns
        }
    
    def calculate_difficulty(self, test_folder_path):
        """テストフォルダの難易度を計算（指示項目数 = 難易度点数）"""
        prompt_path = os.path.join(test_folder_path, 'prompt.txt')
        
        result = self.count_instructions(prompt_path)
        
        if 'error' in result:
            return result
        
        # シンプルな1:1対応
        difficulty_score = result['instruction_count']
        
        return {
            'test_folder': os.path.basename(test_folder_path),
            'difficulty_score': difficulty_score,
            'instruction_count': result['instruction_count'],
            'detection_method': result['detection_method'],
            'details': result['details'],
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
    counter = SimpleInstructionCounter()
    
    # テストフォルダのパス
    tests_path = r"C:\Users\user\Desktop\work\90_cc\20250812\claude-manual-test-100\tests"
    
    # 全テストを評価
    results = counter.evaluate_all_tests(tests_path)
    
    # 結果を表示
    print("=== シンプル指示項目カウント式難易度計算結果 ===")
    print(f"計算日時: {datetime.now()}")
    print("原則: 1指示項目 = 1点 (AI特性に基づく等価評価)")
    print()
    
    prev_score = None
    
    for result in results:
        if 'error' in result:
            print(f"{result['test_folder']}: {result['error']}")
            continue
            
        score = result['difficulty_score']
        change = ""
        if prev_score is not None:
            diff = score - prev_score
            change = f" ({diff:+d})"
        
        print(f"{result['test_folder']}: {score}点{change}")
        print(f"  検出方式: {result['detection_method']}")
        print(f"  指示項目数: {result['instruction_count']}")
        
        # 詳細情報
        details = result['details']
        if details['numbered_list_max'] > 0:
            print(f"  番号付きリスト: 最大{details['numbered_list_max']}項目")
        if details['file_count_requests']:
            print(f"  ファイル作成要求: {details['file_count_requests']}")
        if details['folder_count_requests']:
            print(f"  フォルダ作成要求: {details['folder_count_requests']}")
        if details['explicit_files'] > 0:
            print(f"  明示ファイル: {details['explicit_files']}個")
        if details['explicit_folders'] > 0:
            print(f"  明示フォルダ: {details['explicit_folders']}個")
        
        print()
        prev_score = score
    
    # 結果をJSONで保存
    output_path = os.path.join(os.path.dirname(tests_path), 'evaluation-tools', 'simple_instruction_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"詳細結果を保存: {output_path}")
    
    # 統計情報
    if len(results) > 1 and all('error' not in r for r in results):
        scores = [r['difficulty_score'] for r in results if 'error' not in r]
        print(f"\n=== 統計情報 ===")
        print(f"平均指示項目数: {sum(scores)/len(scores):.1f}項目")
        print(f"最小指示項目数: {min(scores)}項目 ({results[scores.index(min(scores))]['test_folder']})")
        print(f"最大指示項目数: {max(scores)}項目 ({results[scores.index(max(scores))]['test_folder']})")
        print(f"指示項目数レンジ: {max(scores) - min(scores)}項目")
        
        # 旧システムとの比較用参考値も表示
        print(f"\n=== 参考: 旧複雑計算システムとの比較 ===")
        old_scores = [15.75, 48.30, 48.30, 48.30, 125.77, 197.53, 420.87, 857.81, 259.12]
        for i, result in enumerate(results[:len(old_scores)]):
            if 'error' not in result:
                new_score = result['difficulty_score']
                old_score = old_scores[i]
                ratio = old_score / new_score if new_score > 0 else 0
                print(f"{result['test_folder']}: 新{new_score}点 vs 旧{old_score:.1f}点 (比率: {ratio:.1f}倍)")

if __name__ == "__main__":
    main()