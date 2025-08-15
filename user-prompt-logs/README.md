# ユーザープロンプト記録システム

**Version: 0.1**  
**作成日: 2025-08-15**  
**設計者: Quality Checker**

## 📖 概要
ユーザーからの指示・発言内容をそのまま記録・保存するシステムです。

## 📁 フォルダ構成

```
user-prompt-logs/
├── README.md              # このファイル
├── daily/                 # 日別ログ
│   ├── 20250815.md
│   └── [YYYY-MM-DD].md
├── by-role/               # 役割別ログ
│   ├── pm-prompts.md
│   ├── checker-prompts.md
│   └── evaluator-prompts.md
└── raw-logs/              # 生ログファイル
    ├── 20250815.txt
    └── [YYYY-MM-DD].txt
```

## 📝 記録フォーマット

### 基本情報
- 日時: YYYY-MM-DD HH:MM:SS
- 役割: [PM/Checker/Evaluator]
- 対象タスク: [テスト番号や作業内容]

### プロンプト内容
[ユーザーの発言をそのまま記録]

### 関連情報
- 前後の文脈
- 生成された回答の要約
- 作業結果へのリンク

## 🔍 アクセス方法

```bash
# 今日のプロンプトを確認
cat user-prompt-logs/daily/$(date +%Y%m%d).md

# 特定の役割のプロンプトを確認
cat user-prompt-logs/by-role/pm-prompts.md

# 生ログを確認
tail -50 user-prompt-logs/raw-logs/$(date +%Y%m%d).txt
```

## 📋 使用方法

### PM・Checkerが記録する場合
1. ユーザーからの指示受領時
2. user-prompt-logs/daily/[今日の日付].md に追記
3. 該当する役割別ファイルにも追記

### 自動記録（将来実装予定）
- log_prompt.py による自動記録
- work_history.log との連携

---

**最終更新: 2025-08-15 13:23**  
**更新者: Project Manager**