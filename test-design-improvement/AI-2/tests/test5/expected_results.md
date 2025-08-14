# Test5 期待結果

## 最終的なディレクトリ構造

```
library_system/
├── system_info.txt
├── books/
│   ├── fiction/
│   │   └── book_list.txt
│   ├── non_fiction/
│   │   └── book_list.txt
│   └── reference/
│       └── book_list.txt
├── users/
│   ├── user_001.txt
│   └── user_002.txt
└── logs/
    └── access_log.txt
```

## 各ファイルの内容

### system_info.txt
```
Library Management System v1.0
Created: 2024-01-15
Total Books: 9
Total Users: 2
```

### books/fiction/book_list.txt
```
Harry Potter
Lord of the Rings
The Great Gatsby
```

### books/non_fiction/book_list.txt
```
A Brief History of Time
Sapiens
Educated
```

### books/reference/book_list.txt
```
Oxford Dictionary
Encyclopedia Britannica
Atlas of the World
```

### users/user_001.txt
```
Name: Alice Johnson
ID: 001
Status: Active
```

### users/user_002.txt
```
Name: Bob Smith
ID: 002
Status: Active
```

### logs/access_log.txt
```
2024-01-15 09:30 - User 001 borrowed Harry Potter
2024-01-15 10:15 - User 002 returned Sapiens
```

## 検証項目
- 全フォルダが正しい階層に存在する
- 全ファイルが正しい場所に存在する
- 各ファイルの内容が指定通りである
- ディレクトリ構造が完全に一致する