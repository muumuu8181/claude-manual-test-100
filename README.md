# Claude Manual Test System

**Version: 0.1**

## 概要
AIテスト受験者の作業を評価するための自動評価システムです。評価者がサブエージェントを活用して、テスト実施から評価まで完全自動化できます。

手動でAIの能力を検証するプロジェクト。

## システム構成

```
claude-manual-test-100/
├── README.md              # このファイル (v0.1)
├── evaluator-manual/      # 評価者用マニュアル
│   ├── README.md         # メインマニュアル
│   ├── evaluation_checklist.md
│   ├── evaluation_guidelines.md
│   ├── evaluation_template.md
│   ├── next_prompt_examples.md
│   └── new_evaluator_instructions.md
├── evaluator/            # 評価者専用作業フォルダ
│   ├── work_history.log
│   └── logs/
├── audit-reports/        # 第三者監査レポート（管理者用）
│   ├── README.md         # 監査ガイド
│   └── [年]/[月]/        # 年月別レポート
├── evaluation-tools/     # 客観的評価ツール
│   ├── objective_difficulty_calculator.py # 難易度自動計算ツール
│   └── objective_difficulty_results.json  # 計算結果
└── tests/               # テストケース
    ├── test1/
    ├── test2/
    ├── test2-v2/
    ├── test2-v3/
    ├── test3/
    ├── test4/
    ├── test5/
    ├── test6/
    └── _old/             # 過去バージョン
```

## 主な機能

- ✅ サブエージェントによる自動テスト実施
- ✅ 標準化された評価基準（100点満点）
- ✅ 客観的難易度計算システム（AI主観排除）
- ✅ 時刻記録の自動化（dateコマンド必須）
- ✅ エラー・問題の詳細記録
- ✅ 段階的な難易度設定

## 重要なルール

### 1. 時刻記録
**全AIは必ずdateコマンドで時刻を取得すること**
```bash
date '+%Y%m%d %H:%M:%S'
```

### 2. 作業記録
- 受験者: tests/test[番号]/work_history.log
- 評価者: evaluator/work_history.log

### 3. reflection.txt必須項目
- エラー・問題の記録（エラーなしも明記）
- 指示の明確さ評価
- 作業の困難さ
- 工夫した点
- 改善案

## 使用方法

### 新しい評価者の場合
```bash
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/new_evaluator_instructions.md
```

### テスト実施フロー
1. test[番号]フォルダ作成
2. prompt.txt作成（課題）
3. サブエージェント呼び出し（Task tool使用）
4. 自動評価実施
5. feedbackフォルダに評価レポート作成

### 客観的難易度計算ツール
**場所:** `evaluation-tools/objective_difficulty_calculator.py`

**特徴:**
- 100点制約なしの完全機械的計算
- AI主観を完全排除
- プロンプト解析による自動評価
- **誰がいつ実行しても同じ結果**

**使用方法:**
```bash
cd evaluation-tools
python objective_difficulty_calculator.py
```

**結果例 (test1-7):**
```
test1: 15.75点
test2: 48.30点 (+32.55)
test3: 125.77点 (+77.47)
test4: 197.53点 (+71.76)
test5: 420.87点 (+223.34)
test6: 857.81点 (+436.94)
test7: 259.12点 (-598.69) ← 逆転検出
```

**活用方法:**
- 新テスト作成時の難易度確認
- AI評価との客観的比較
- 難易度逆転の事前検出

## バージョン履歴

### v0.2 (2025-08-13)
- **評価基準の根本的改訂**
  - 動作検証を最重要項目に変更（配点40%）
  - test6の再評価により判明した問題を修正
  - 必須評価チェックリスト（evaluation_checklist_mandatory.md）を新規作成
  - チェックリスト確認のwork_history.logへの記録を必須化
- **ドキュメント整備**
  - audit-reportsフォルダの追加
  - フォルダ構成図の更新（test5, test6, _old追加）

### v0.1 (2025-08-13)
- 初版リリース
- test1〜test4まで実施済み
- サブエージェント統合完了
- 評価マニュアル整備完了
- reflection.txt記載ガイドライン強化

## 今後の予定
- 難易度の限界値探索
- 評価基準の精緻化
- エラーパターンの分析

## 作成者
Claude Code（評価システム設計・実装）

---
13:58 2025/08/12 - プロジェクト開始