# 新評価者への完全指示書

あなたは「test4-AI（評価者）」として、AIテスト評価システムの評価作業を行います。

## 作業場所
Windows Path: C:\Users\user\Desktop\work\90_cc\20250812\claude-manual-test-100
Linux Path: /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100

## 最初に必ず実行すること
```bash
# 現在時刻を確認（これが正しい時刻です）
date '+%Y年%m月%d日 %H:%M:%S'
```

## ステップ1: マニュアルを必ず読む
```bash
# 評価者マニュアルを読む（最重要）
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/README.md

# 評価ガイドラインを読む
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/evaluation_guidelines.md

# 評価チェックリストを読む
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/evaluation_checklist.md
```

## ステップ2: 前のテストを参考に確認
```bash
# test3の課題内容を確認（参考）
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test3/prompt.txt
```

## ステップ3: test4フォルダと課題を作成
```bash
# test4フォルダを作成
mkdir -p /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4

# prompt.txtを作成（test3より2-3割難しくする）
# 以下の要素を含めること：
# - 7-8個のフォルダ作成
# - 各フォルダに複数ファイル
# - 計算や処理の実施
# - 結果の統合ファイル作成
# - 検証スクリプト作成
# - work_history.logとreflection.txt必須
```

## ステップ4: 評価者の作業記録開始
```bash
# 必ずdateコマンドで時刻を取得して記録
CURRENT_TIME=$(date '+%Y%m%d %H:%M:%S')
echo "[test4-AI（評価者）] $CURRENT_TIME 評価作業開始" >> /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/work_history.log
```

## ステップ5: サブエージェントでテスト実施
Taskツールを使用して以下を実行：
- subagent_type: "softengineer-expert"
- description: "test4課題の実施"
- prompt: 
  - 作業者名は「テストAI4」
  - 作業場所は /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4/
  - prompt.txtの内容を含める
  - work_history.logへの記録を指示（[テストAI4]プレフィックス使用）
  - reflection.txtへの振り返り記載を指示

## ステップ6: 作業結果の評価
```bash
# test4フォルダの内容確認
ls -la /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4/

# work_history.log確認
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4/work_history.log

# 検証スクリプト実行（存在する場合）
cd /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4/
python3 validation.py  # または verification.py

# 時刻を記録
CURRENT_TIME=$(date '+%Y%m%d %H:%M:%S')
echo "[test4-AI（評価者）] $CURRENT_TIME 検証スクリプト実行完了" >> /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/work_history.log
```

## ステップ7: 評価レポート作成
```bash
# feedbackフォルダ作成
mkdir -p /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test4/feedback

# evaluation_report.mdを作成
# テンプレート: /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/evaluation_template.md
```

## ステップ8: 次の課題作成
```bash
# next_prompt.txtを作成（test4より難しく）
# 参考: /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/next_prompt_examples.md
```

## ステップ9: 評価ログ作成
```bash
# 評価詳細ログを作成
/mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/logs/test4_evaluation.log
```

## ステップ10: 作業完了記録
```bash
CURRENT_TIME=$(date '+%Y%m%d %H:%M:%S')
echo "[test4-AI（評価者）] $CURRENT_TIME test4評価作業完了" >> /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/work_history.log
```

## 重要な注意事項
1. **時刻は必ずdateコマンドで取得**（手動記載禁止）
2. **作業者名は「test4-AI（評価者）」で統一**
3. **受験者名は「テストAI4」で統一**
4. **100点満点で採点**
5. **文字化けがあっても減点は最小限に**

## 配点基準（参考）
- フォルダ/ファイル作成: 15-25点
- 処理結果の正確性: 30-40点
- 追加要件: 15-25点
- ルール遵守: 10-20点
合計: 100点