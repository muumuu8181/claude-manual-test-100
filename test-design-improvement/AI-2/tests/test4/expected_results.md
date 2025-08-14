# Test4 期待結果

## 各手順の期待結果

### 手順 1-3
- alpha, beta, gammaの3つのフォルダが作成される

### 手順 4-5
- alpha/config.jsonが作成される
- 内容: {"version": "1.0"}

### 手順 6
- betaがbeta_backupにリネームされる
- betaフォルダは存在しなくなる

### 手順 7
- gamma/config.jsonが作成される
- alphaとgammaの両方にconfig.jsonが存在

### 手順 8
- gamma/config.jsonの内容が{"version": "2.0"}に変更される
- alpha/config.jsonは{"version": "1.0"}のまま

### 手順 9
- alphaフォルダが削除される
- alphaフォルダとその中身が存在しなくなる

### 手順 10
- beta_backupがproductionにリネームされる
- beta_backupは存在しなくなる

## 最終状態

```
gamma/
└── config.json ({"version": "2.0"})

production/
(空フォルダ)
```

## チェックポイント
- alphaフォルダが存在しない
- betaフォルダが存在しない
- beta_backupフォルダが存在しない
- gammaフォルダが存在し、config.jsonの内容が"2.0"
- productionフォルダが存在する