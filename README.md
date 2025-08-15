# Claude Manual Test System

**Version: 0.3**

## 概要
AIテスト受験者の作業を評価するための自動評価システムです。評価者がサブエージェントを活用して、テスト実施から評価まで完全自動化できます。

手動でAIの能力を検証するプロジェクト。

## 👥 役割定義（Role Definitions）- ダブルチェック方式

### 🎯 新体制：PM + Checkers

このプロジェクトは**ダブルチェック方式**を採用しています：
1. **Project Manager (PM)** がタスク全体を実行
2. **Specialist Checkers** が専門視点でチェック

---

## 第1層：実行役

### Project Manager（プロジェクトマネージャー）
**複雑なタスクや複数領域にまたがる作業を依頼されたら、あなたはPMです**
- 責任: タスク全体を引き受けて完遂
- 特徴: 複数の専門領域をカバー
- 最後に必ず: 「次は○○ Checkerでチェックしてください」と明記

### Test Taker（テスト受験者）
**「テストを実施してください」と言われたら、あなたはこの役割です**
- 作業場所: `tests/v0.2/test*/executions/`
- 成果物: work_history.log、指定されたフォルダ・ファイル

### Test Evaluator（テスト評価者）
**「テスト結果を評価してください」と言われたら、あなたはこの役割です**
- 作業場所: `tests/v0.2/test*/evaluations/`
- 成果物: evaluation_report_AI_XXX.md

---

## 第2層：チェック役（Specialist Checkers）

### Platform Checker
**「フォルダ構成をチェックして」と言われたら、この役割です**
- チェック内容: フォルダ構造、命名規則、配置の妥当性
- 判定: 構造的に問題ないか

### Document Checker
**「ドキュメントをチェックして」と言われたら、この役割です**
- チェック内容: 文書品質、わかりやすさ、既存形式との整合性
- 判定: 読み手にとって適切か

### Quality Checker
**「品質をチェックして」と言われたら、この役割です**
- チェック内容: 既存ルールとの整合性、一貫性
- 判定: プロジェクト全体として問題ないか

### Test Checker
**「動作をチェックして」と言われたら、この役割です**
- チェック内容: 実際に動くか、期待通りの結果か
- 判定: 機能的に問題ないか

---

## 🔄 運用フロー

1. **ユーザー** → PM: 「○○を作って」
2. **PM**: 作業実行 → 「完了しました。次は△△ Checkerでチェックしてください」
3. **ユーザー** → Checker: PMの指示をコピペ
4. **Checker**: チェック → 「問題あり/なし」
5. 問題あれば PM が修正

---

## 📝 PMの心得

作業完了時は必ず以下を明記：
```
【次のステップ】
○○ Checkerに以下の指示を出してください：
「[具体的なチェック指示]」
```

## システム構成

```
claude-manual-test-100/
├── README.md              # このファイル (v0.1)
├── SUPREME_RULE.md        # 最上位ルール（全AI必読）
├── COMMON_RULES.md        # 全AI共通ルール
├── PM_MANUAL.md           # PM専用マニュアル
├── CHECKER_MANUAL.md      # Checker専用マニュアル
├── PROJECT_ISSUES.md      # 課題・要望管理リスト
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
├── ai-communications/    # AI間連絡記録
│   ├── active/          # 進行中の連絡
│   └── completed/       # 完了済み連絡
├── user-prompt-logs/     # ユーザープロンプト記録
│   ├── daily/           # 日別記録
│   └── by-role/         # 役割別記録
├── pm-workspace/         # PM専用作業エリア
│   ├── analysis/        # 分析・感想
│   ├── verification/    # 検証用
│   ├── rules/           # ルール明確化
│   ├── contingency/     # 想定外対応
│   └── work-history/    # PM作業履歴
├── discussions/          # プロジェクト議論記録
├── test-design-improvement/ # テスト設計改善プロジェクト
│   ├── AI-1/           # AI-1による設計案
│   ├── AI-2/           # AI-2による設計案
│   ├── AI-3/           # AI-3による設計案
│   ├── AI-4/           # AI-4による設計案
│   └── cross_feedback/ # 相互フィードバック
├── USER_PROMPTS/         # ユーザー用プロンプト集
│   └── ALL_PROMPTS.md   # 全プロンプト統合版
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

### v0.3 (2025-08-14)
- **テスト設計改善プロジェクト追加**
  - 複数AIによる包括的なテスト設計評価
  - 客観的難易度計算ツールの強化
  - test7の追加と詳細な評価実施
  - クロスフィードバック機能の実装

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