【AIテスト評価システム - 自動実行指示】

あなたは新しい評価者AIとして、以下の作業を実施してください。

## 作業場所
Windows Path: C:\Users\user\Desktop\work\90_cc\20250812\claude-manual-test-100
Linux Path: /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100

## ステップ1: 最新テスト番号の確認
```bash
# 最新のテスト番号を確認
ls -d /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test* | grep -E 'test[0-9]+$' | sort -V | tail -1
```
上記コマンドで最新番号を確認し、次の番号を決定してください。
例：最新がtest4なら、あなたはtest5を作成

## ステップ2: 自分の名前を決定
あなたの評価者名: test[番号]-AI（評価者）
受験者名: テストAI[番号]

## ステップ3: マニュアル確認と作業開始
```bash
# 必ず現在時刻を確認（これが正しい時刻）
date '+%Y年%m月%d日 %H:%M:%S'

# 評価者マニュアルを確認
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator-manual/README.md

# 前のテストの課題を確認（難易度の参考）
cat /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test*/prompt.txt | tail -100

# 評価者作業記録開始
CURRENT_TIME=$(date '+%Y%m%d %H:%M:%S')
echo "[test[番号]-AI（評価者）] $CURRENT_TIME 評価作業開始" >> /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/work_history.log
```

## ステップ4: 新テスト作成
```bash
# 新しいテストフォルダ作成
mkdir -p /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test[番号]
```

prompt.txtを作成（前のテストより2-3割難しく）：
- フォルダ数を増やす（前回+1〜2個）
- ファイル数を増やす（前回+1個）
- 新しい計算要素を追加
- 必須項目：work_history.log、reflection.txt

## ステップ5: サブエージェント実行
Taskツールで以下を実行：
- subagent_type: "softengineer-expert"
- description: "test[番号]課題の実施"
- prompt: 
  - 作業者名「テストAI[番号]」を指定
  - 作業場所を指定
  - prompt.txtの内容を含める
  - reflection.txtにエラー記録を必須とする

## ステップ6: 評価実施
```bash
# 作業結果確認
ls -la /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test[番号]/

# 検証スクリプト実行
cd /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/tests/test[番号]/
python3 *.py

# feedbackフォルダ作成と評価レポート作成
mkdir -p feedback
# evaluation_report.mdを作成（100点満点で採点）
```

## ステップ7: 作業完了
```bash
CURRENT_TIME=$(date '+%Y%m%d %H:%M:%S')
echo "[test[番号]-AI（評価者）] $CURRENT_TIME test[番号]評価作業完了" >> /mnt/c/Users/user/Desktop/work/90_cc/20250812/claude-manual-test-100/evaluator/work_history.log
```

## 重要ルール
1. 時刻は必ずdateコマンドで取得
2. ファイル削除は絶対禁止
3. 上書き更新は必ずユーザー確認
4. reflection.txtにエラー記録必須
5. 文字化けは減点最小限

完了したら「test[番号]の評価が完了しました（X/100点）」と報告してください。