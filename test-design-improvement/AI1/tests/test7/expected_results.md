# Test 7: Expected Results

## Source Data
- **raw_scores.txt**: Math: 87, Science: 92, English: 78, History: 85, Art: 90

## Letter Grade Conversions
- **math_grade.txt**: B (87 is 80-89)
- **science_grade.txt**: A (92 is 90+)
- **english_grade.txt**: C (78 is 70-79)
- **history_grade.txt**: B (85 is 80-89)
- **art_grade.txt**: A (90 is 90+)

## Statistical Calculations
- **total_points.txt**: 432 (87+92+78+85+90)
- **average_score.txt**: 86.4 (432 ÷ 5)

## Grade Analysis
- **count_a.txt**: 2 (Science: A, Art: A)
- **count_b.txt**: 2 (Math: B, History: B)
- **count_c.txt**: 1 (English: C)

## Performance Analysis
- **top_subject.txt**: Science: 92
- **bottom_subject.txt**: English: 78
- **grade_distribution.txt**:
  ```
  A: 2
  B: 2
  C: 1
  D: 0
  F: 0
  ```

- **performance_analysis.txt**:
  ```
  Above Average (86.4): Science (92), Art (90), Math (87)
  Below Average (86.4): History (85), English (78)
  ```

- **subject_ranking.txt**:
  ```
  1. Science: 92
  2. Art: 90
  3. Math: 87
  4. History: 85
  5. English: 78
  ```

- **final_report.txt**:
  ```
  Overall GPA: 3.2
  (Science: A=4.0, Art: A=4.0, Math: B=3.0, History: B=3.0, English: C=2.0)
  Total Grade Points: 16.0
  GPA = 16.0 ÷ 5 = 3.2
  ```

## Directory Structure
```
test7/
├── raw_scores.txt
├── math_grade.txt
├── science_grade.txt
├── english_grade.txt
├── history_grade.txt
├── art_grade.txt
├── total_points.txt
├── average_score.txt
├── count_a.txt
├── count_b.txt
├── count_c.txt
├── top_subject.txt
├── bottom_subject.txt
├── grade_distribution.txt
├── performance_analysis.txt
├── subject_ranking.txt
└── final_report.txt
```