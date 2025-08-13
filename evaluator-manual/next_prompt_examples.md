# next_prompt.txt 作成例集

## 基本構造テンプレート
```text
【作業指示】
1) [フォルダ作成指示]
2) [ファイル作成指示]
3) [処理内容指示]
4) [まとめファイル指示]
5) [検証指示]
6) [次の課題作成指示]
```

## 難易度別の具体例

### 📝 Level 1（難易度10）: 超基本
```text
【作業指示】
1) 2つのフォルダを作成してください。input, outputとrename。
2) inputフォルダにdata.txtを作成し、「100,200,300」と記載。
3) outputフォルダにresult.txtを作成し、合計値を記載。
4) 作業完了後、check.txtに「完了」と記載。
```

### 📝 Level 2（難易度15）: 基本+α
```text
【作業指示】
1) 4つのフォルダを作成してください。data_A, data_B, data_C, data_Dとrename。
2) 各フォルダにvalue.txtとformula.txtを作成。
3) 数値 x=50, y=30 を使用：
   data_A: x+y の結果と式
   data_B: x-y の結果と式
   data_C: x*y の結果と式
   data_D: x/y の結果と式（小数点第2位まで）
4) summary.csvを作成し、全結果をまとめる。
5) verify.shを作成し、ファイル存在確認のスクリプトを記載。
```

### 📝 Level 3（難易度20）: 中級
```text
【作業指示】
1) 6つのフォルダを作成。calc_1〜calc_6とrename。
2) 各フォルダに3ファイル：input.json, process.txt, output.json
3) 数値 a=100, b=75, c=50 を使用：
   calc_1: {"operation": "sum", "result": a+b+c}
   calc_2: {"operation": "product", "result": a*b/c}
   calc_3: {"operation": "power", "result": a^2 - b^2}
   （以下略）
4) master_report.jsonに全結果を階層的に統合。
5) validator.pyで全JSONの妥当性を検証。
6) error.logにエラーがあれば記録、なければ"No errors"。
```

### 📝 Level 4（難易度25）: 中上級
```text
【作業指示】
1) 階層構造：project/
   ├── src/（module_1〜module_5の5フォルダ）
   ├── tests/（test_1〜test_5の5フォルダ）
   └── docs/
2) 各moduleフォルダ：config.yaml, main.py, output.log
3) 各testフォルダ：test_[番号].py, expected.txt, actual.txt
4) 処理内容：
   - module間で依存関係（module_2はmodule_1の結果を使用）
   - エラーハンドリング（0除算、負の平方根等）
5) docs/に自動生成：
   - architecture.md（構造説明）
   - test_report.html（テスト結果）
6) Makefileを作成し、全処理を自動化。
```

### 📝 Level 5（難易度30）: 上級
```text
【作業指示】
1) マイクロサービス構造を模擬：
   services/
   ├── auth_service/
   ├── data_service/
   ├── calc_service/
   └── report_service/
2) 各サービス：
   - Dockerfile（模擬）
   - api.json（エンドポイント定義）
   - handler.py（処理ロジック）
   - test_integration.py
3) サービス間通信：
   - auth_service → token.json生成
   - data_service → tokenを検証してデータ提供
   - calc_service → データを処理
   - report_service → 結果を集約
4) docker-compose.yml（模擬）で全体構成を定義。
5) monitoring/フォルダ：
   - metrics.json（各サービスのメトリクス）
   - alerts.yaml（閾値設定）
6) CI/CD：.github/workflows/test.yml（模擬）
7) 負荷テスト：benchmark.pyで1000回の処理をシミュレート。
```

## 段階的な要素追加パターン

### 📊 データ形式の進化
```
Level 1: テキストファイル（単純な値）
Level 2: CSV（表形式）
Level 3: JSON（構造化データ）
Level 4: YAML（設定ファイル）
Level 5: バイナリ/エンコード（Base64等）
```

### 🔧 処理の複雑化
```
Level 1: 四則演算
Level 2: 累乗、平方根
Level 3: 条件分岐（if-then）
Level 4: ループ処理（集計等）
Level 5: 再帰処理、非同期処理
```

### 📁 構造の深化
```
Level 1: フラット（全て同階層）
Level 2: 1階層（カテゴリ分け）
Level 3: 2階層（サブカテゴリ）
Level 4: 3階層以上（複雑な構造）
Level 5: 動的生成される構造
```

### ✅ 検証の高度化
```
Level 1: ファイル存在確認
Level 2: 値の一致確認
Level 3: 形式妥当性確認
Level 4: 相互整合性確認
Level 5: パフォーマンス測定
```

## 避けるべきパターン

### ❌ 悪い例
```text
【作業指示】
1) フォルダを作る
2) 何かファイルを入れる
3) 適当に計算する
4) まとめる
```
→ 指示が曖昧

### ❌ 悪い例
```text
【作業指示】
1) test1/にREADME.mdを作成...
2) test2/にINSTRUCTIONS.txtを作成...
3) test1/README.mdに追記...
4) test3/のSETUP.mdを参照して...
```
→ 指示が分散している

### ✅ 良い例
```text
【作業指示】
1) 3つのフォルダを作成：folder_A, folder_B, folder_C
2) 各フォルダにresult.txtを作成
3) folder_A: 10+20の結果（30）を記載
   folder_B: 10*20の結果（200）を記載
   folder_C: 10^2の結果（100）を記載
4) summary.txtに全結果を記載
```
→ 明確で具体的