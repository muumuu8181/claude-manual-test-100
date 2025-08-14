# Test 3: Expected Results

## Source Text
- **source.txt**: "The quick brown fox jumps over the lazy dog"

## Word Extraction
- **word1.txt**: "quick"
- **word2.txt**: "brown"  
- **word3.txt**: "jumps"

## Counting Results
- **char_count.txt**: "43" (total characters including spaces)
- **word_count.txt**: "9" (total words)

## Text Transformations
- **reversed.txt**: "god yzal eht revo spmuj xof nworb kciuq ehT"
- **uppercase.txt**: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

## Summary Report
- **report.txt**: Should contain:
  - Original text: "The quick brown fox jumps over the lazy dog"
  - Character count: 43
  - Word count: 9
  - Confirmation that all files were created successfully

## Directory Structure
```
test3/
├── source.txt
├── word1.txt
├── word2.txt
├── word3.txt
├── char_count.txt
├── word_count.txt
├── reversed.txt
├── uppercase.txt
└── report.txt
```

## Verification Points
- Character count should be exactly 43
- Word count should be exactly 9
- Reversed text should be character-by-character reversal
- All extracted words should match exactly