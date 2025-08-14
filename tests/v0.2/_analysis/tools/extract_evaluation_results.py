#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
評価レポートから○×を抽出して集計するツール
評価者自身の集計ミスを無視し、実際の○×のみを正確にカウントします
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


def extract_evaluation_results(file_path: str) -> Dict:
    """
    評価レポートファイルから○×を抽出する
    
    Args:
        file_path: 評価レポートのファイルパス
    
    Returns:
        評価結果の辞書
    """
    results = {
        'evaluator': '',
        'date': '',
        'items': {},
        'actual_pass_count': 0,
        'reported_pass_count': None,
        'reported_rate': None
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        in_table = False
        for line in lines:
            # 評価者名を抽出
            if line.startswith('評価者：'):
                results['evaluator'] = line.replace('評価者：', '').strip()
            
            # 評価日時を抽出
            elif line.startswith('評価日時：'):
                results['date'] = line.replace('評価日時：', '').strip()
            
            # テーブル開始を検出
            elif '| 項目番号 | 評価項目 | 結果 |' in line:
                in_table = True
                continue
            
            # テーブル内の評価結果を抽出
            elif in_table and line.startswith('|'):
                # テーブルのセパレータ行をスキップ
                if '---|' in line:
                    continue
                
                # 評価項目の行をパース
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 4:
                    try:
                        item_num = int(parts[1])
                        item_name = parts[2]
                        result = parts[3]
                        
                        # ○または×を抽出
                        if '○' in result:
                            results['items'][item_num] = ('○', item_name)
                            results['actual_pass_count'] += 1
                        elif '×' in result:
                            results['items'][item_num] = ('×', item_name)
                    except (ValueError, IndexError):
                        pass
            
            # 報告された達成項目数を抽出
            elif '達成項目数：' in line:
                match = re.search(r'(\d+)/(\d+)', line)
                if match:
                    results['reported_pass_count'] = int(match.group(1))
            
            # 報告された達成率を抽出
            elif '達成率：' in line:
                match = re.search(r'([\d.]+)%', line)
                if match:
                    results['reported_rate'] = float(match.group(1))
    
    except Exception as e:
        print(f"エラー: {file_path} の読み込みに失敗しました: {e}")
    
    return results


def find_evaluation_reports(base_dir: str) -> List[str]:
    """
    指定ディレクトリ配下の全評価レポートファイルを検索する
    
    Args:
        base_dir: 検索開始ディレクトリ
    
    Returns:
        評価レポートファイルのパスリスト
    """
    report_files = []
    base_path = Path(base_dir)
    
    # evaluationsフォルダ内のevaluation_report_*.mdファイルを検索
    for eval_dir in base_path.glob('evaluations/EVAL_*'):
        for report_file in eval_dir.glob('evaluation_report_*.md'):
            report_files.append(str(report_file))
    
    return sorted(report_files)


def generate_html_report(all_results: List[Dict], output_file: str, test_name: str = ""):
    """
    集計結果をHTML形式で出力する
    
    Args:
        all_results: 全評価結果のリスト
        output_file: 出力HTMLファイルパス
        test_name: テスト名（表示用）
    """
    
    # 項目名の収集（最初の評価者から取得）
    item_names = {}
    if all_results:
        for item_num, (result, name) in all_results[0]['items'].items():
            item_names[item_num] = name
    
    html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{test_name} 評価結果集計レポート（実際の○×カウント）</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #2196F3;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
        }}
        .warning-box {{
            background-color: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
        }}
        .table-container {{
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow-x: auto;
            margin-bottom: 30px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            min-width: 800px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
        }}
        .evaluator-header {{
            background-color: #1976D2;
        }}
        .item-col {{
            text-align: left;
            background-color: #f9f9f9;
            font-weight: 500;
        }}
        .pass {{
            color: #4CAF50;
            font-weight: bold;
            font-size: 18px;
        }}
        .fail {{
            color: #f44336;
            font-weight: bold;
            font-size: 18px;
        }}
        .summary-row {{
            background-color: #e3f2fd;
            font-weight: bold;
        }}
        .discrepancy {{
            background-color: #ffebee;
            color: #c62828;
            font-weight: bold;
        }}
        .correct {{
            background-color: #e8f5e9;
            color: #2e7d32;
        }}
        .timestamp {{
            text-align: right;
            color: #666;
            font-size: 14px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <h1>{test_name} 評価結果集計レポート（実際の○×カウント）</h1>
    
    <div class="warning-box">
        <strong>⚠️ 注意:</strong> このレポートは評価レポート内の実際の○×を直接カウントしています。
        評価者自身が報告した集計値とは異なる場合があります（集計ミスの可能性）。
    </div>
"""
    
    # 評価項目別○×表
    html_content += """
    <div class="table-container">
        <h2>評価項目別 ○×比較表（実際のカウント）</h2>
        <table>
            <thead>
                <tr>
                    <th>項目</th>
                    <th class="item-col">評価内容</th>
"""
    
    # 評価者のヘッダーを追加
    for result in all_results:
        html_content += f'                    <th class="evaluator-header">{result["evaluator"]}</th>\n'
    
    html_content += """                    <th>○数</th>
                    <th>一致度</th>
                </tr>
            </thead>
            <tbody>
"""
    
    # 各項目の結果を表示
    for item_num in range(1, 14):
        item_name = item_names.get(item_num, f"項目{item_num}")
        html_content += f'                <tr>\n'
        html_content += f'                    <td>{item_num}</td>\n'
        html_content += f'                    <td class="item-col">{item_name}</td>\n'
        
        pass_count = 0
        for result in all_results:
            if item_num in result['items']:
                mark, _ = result['items'][item_num]
                if mark == '○':
                    html_content += f'                    <td class="pass">○</td>\n'
                    pass_count += 1
                else:
                    html_content += f'                    <td class="fail">×</td>\n'
            else:
                html_content += f'                    <td>-</td>\n'
        
        total_evaluators = len(all_results)
        agreement = 100 if pass_count == 0 or pass_count == total_evaluators else round((max(pass_count, total_evaluators - pass_count) / total_evaluators) * 100, 1)
        
        html_content += f'                    <td>{pass_count}</td>\n'
        html_content += f'                    <td>{agreement}%</td>\n'
        html_content += f'                </tr>\n'
    
    # 合計行
    html_content += '                <tr class="summary-row">\n'
    html_content += '                    <td colspan="2"><strong>実際の○数</strong></td>\n'
    for result in all_results:
        html_content += f'                    <td>{result["actual_pass_count"]}</td>\n'
    html_content += '                    <td colspan="2">-</td>\n'
    html_content += '                </tr>\n'
    
    # 報告された値との比較
    html_content += '                <tr>\n'
    html_content += '                    <td colspan="2"><strong>報告された○数</strong></td>\n'
    for result in all_results:
        if result['reported_pass_count'] is not None:
            if result['reported_pass_count'] != result['actual_pass_count']:
                html_content += f'                    <td class="discrepancy">{result["reported_pass_count"]} ⚠️</td>\n'
            else:
                html_content += f'                    <td class="correct">{result["reported_pass_count"]} ✓</td>\n'
        else:
            html_content += '                    <td>-</td>\n'
    html_content += '                    <td colspan="2">-</td>\n'
    html_content += '                </tr>\n'
    
    html_content += """            </tbody>
        </table>
    </div>
"""
    
    # 集計ミスの検出
    discrepancies = []
    for result in all_results:
        if result['reported_pass_count'] is not None and result['reported_pass_count'] != result['actual_pass_count']:
            discrepancies.append({
                'evaluator': result['evaluator'],
                'actual': result['actual_pass_count'],
                'reported': result['reported_pass_count'],
                'difference': result['actual_pass_count'] - result['reported_pass_count']
            })
    
    if discrepancies:
        html_content += """
    <div class="table-container">
        <h2>集計ミスの検出</h2>
        <table>
            <thead>
                <tr>
                    <th>評価者</th>
                    <th>実際の○数</th>
                    <th>報告された○数</th>
                    <th>差分</th>
                    <th>備考</th>
                </tr>
            </thead>
            <tbody>
"""
        for disc in discrepancies:
            html_content += f"""                <tr>
                    <td>{disc['evaluator']}</td>
                    <td class="correct">{disc['actual']}</td>
                    <td class="discrepancy">{disc['reported']}</td>
                    <td>{disc['difference']:+d}</td>
                    <td>{"過小報告" if disc['difference'] > 0 else "過大報告"}</td>
                </tr>
"""
        html_content += """            </tbody>
        </table>
    </div>
"""
    
    html_content += f"""
    <div class="timestamp">
        生成日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}
    </div>
</body>
</html>
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTMLレポートを生成しました: {output_file}")


def main():
    """メイン処理"""
    # コマンドライン引数でテスト名を指定可能に
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
    else:
        test_name = 'test1'
    
    # 基準ディレクトリ（ツールから2階層上のv0.2配下のテストフォルダ）
    script_dir = Path(__file__).parent.parent.parent  # _analysis/tools -> v0.2
    base_dir = script_dir / test_name
    
    if not base_dir.exists():
        print(f"エラー: テストフォルダが見つかりません: {base_dir}")
        return
    
    print(f"評価レポートを検索中: {base_dir}")
    
    # 評価レポートファイルを検索
    report_files = find_evaluation_reports(str(base_dir))
    
    if not report_files:
        print("評価レポートファイルが見つかりませんでした。")
        return
    
    print(f"{len(report_files)}個の評価レポートを発見しました。")
    
    # 各レポートから結果を抽出
    all_results = []
    for report_file in report_files:
        print(f"処理中: {report_file}")
        result = extract_evaluation_results(report_file)
        if result['evaluator']:
            all_results.append(result)
            
            # 集計ミスをチェック
            if result['reported_pass_count'] is not None:
                if result['actual_pass_count'] != result['reported_pass_count']:
                    print(f"  [WARNING] 集計ミス検出: {result['evaluator']} - 実際: {result['actual_pass_count']}個, 報告: {result['reported_pass_count']}個")
                else:
                    print(f"  [OK] 集計一致: {result['evaluator']} - {result['actual_pass_count']}個")
    
    # HTMLレポートを生成（tool_outputsフォルダに保存）
    output_dir = script_dir / '_analysis' / 'tool_outputs'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f'{test_name}_analysis_report.html'
    
    generate_html_report(all_results, str(output_file), test_name)
    
    print("\n処理完了!")
    print(f"結果は {output_file} に保存されました。")


if __name__ == '__main__':
    main()