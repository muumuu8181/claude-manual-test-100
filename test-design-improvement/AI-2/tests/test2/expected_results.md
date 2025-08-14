# Test2 期待結果

## 各手順の期待結果

### 手順 1
- `main_dir`フォルダが作成される

### 手順 2
- `backup_dir`フォルダが作成される
- main_dirと同階層に存在

### 手順 3
- `main_dir/report.txt`が作成される

### 手順 4
- report.txtに「2025年度」が書き込まれる

### 手順 5
- report.txtに「売上報告」が追記される
- ファイル内容：「2025年度売上報告」または「2025年度\n売上報告」

### 手順 6
- `backup_dir/report.txt`が作成される
- main_dirとbackup_dirの両方にreport.txtが存在
- 両ファイルの内容が同一

### 手順 7
- `main_dir`が`workspace`にリネームされる
- main_dirは存在しなくなる

## 最終状態

```
workspace/
└── report.txt (内容: 2025年度売上報告)

backup_dir/
└── report.txt (内容: 2025年度売上報告)
```

## チェックポイント
- main_dirは存在しない
- workspaceが存在する
- backup_dirが存在する
- 両方のreport.txtが存在し、内容が同じ