# Test3 期待結果

## 各手順の期待結果

### 手順 1-2
- `documents`と`images`フォルダが作成される

### 手順 3-8
- documents内に3つのファイルが作成される
- 各ファイルに指定された内容が書き込まれる

### 手順 9
- note2.txtがdocumentsからimagesに移動される
- documentsにはnote2.txtが存在しなくなる

## 最終状態

```
documents/
├── note1.txt (First)
└── note3.txt (Third)

images/
└── note2.txt (Second)
```

## チェックポイント
- documentsにnote1.txtとnote3.txtのみ
- imagesにnote2.txtが存在
- 各ファイルの内容が正確