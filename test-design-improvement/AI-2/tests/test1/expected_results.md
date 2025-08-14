# Test1 期待結果

## 各手順の期待結果

### 手順 1
- `work_folder`という名前のフォルダが作成される
- フォルダは空の状態

### 手順 2
- `work_folder/data.txt`が作成される
- ファイルは空または内容がまだ書き込まれていない

### 手順 3
- `data.txt`に「Hello World」が書き込まれる
- 正確に「Hello World」のみ（引用符なし、余計な空白や改行なし）

### 手順 4
- `work_folder`が`project_folder`にリネームされる
- `work_folder`は存在しなくなる
- `project_folder`が存在し、中に`data.txt`がある

### 手順 5
- `project_folder/info.txt`が作成される
- ファイルは存在する（内容は空でも可）

## 最終状態

```
project_folder/
├── data.txt (Hello World)
└── info.txt (空または任意の内容)
```

## チェックポイント
- work_folderは存在しない
- project_folderが存在する
- data.txtの内容が正確
- info.txtが存在する