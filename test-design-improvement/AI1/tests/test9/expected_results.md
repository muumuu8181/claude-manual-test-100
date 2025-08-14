# Test 9: Expected Results

## Source Data
- **survey_responses.txt**: Q1: 4,5,3,4,5,2,4,3,5,4 | Q2: 3,4,4,3,5,3,4,4,2,4 | Q3: 5,4,3,5,4,4,3,5,4,4

## Question Response Files
- **q1_responses.txt**: 4,5,3,4,5,2,4,3,5,4
- **q2_responses.txt**: 3,4,4,3,5,3,4,4,2,4
- **q3_responses.txt**: 5,4,3,5,4,4,3,5,4,4

## Basic Statistics
### Totals
- **q1_total.txt**: 39 (4+5+3+4+5+2+4+3+5+4)
- **q2_total.txt**: 36 (3+4+4+3+5+3+4+4+2+4)
- **q3_total.txt**: 41 (5+4+3+5+4+4+3+5+4+4)

### Averages
- **q1_average.txt**: 3.9 (39÷10)
- **q2_average.txt**: 3.6 (36÷10)
- **q3_average.txt**: 4.1 (41÷10)

### Min/Max Values
- **q1_max.txt**: 5
- **q1_min.txt**: 2
- **q2_max.txt**: 5
- **q2_min.txt**: 2
- **q3_max.txt**: 5
- **q3_min.txt**: 3

## Response Count Distribution

### Q1 Counts
- **q1_fives.txt**: 3
- **q1_fours.txt**: 4
- **q1_threes.txt**: 2
- **q1_twos.txt**: 1
- **q1_ones.txt**: 0

### Q2 Counts
- **q2_fives.txt**: 1
- **q2_fours.txt**: 5
- **q2_threes.txt**: 3
- **q2_twos.txt**: 1
- **q2_ones.txt**: 0

### Q3 Counts
- **q3_fives.txt**: 3
- **q3_fours.txt**: 5
- **q3_threes.txt**: 2
- **q3_twos.txt**: 0
- **q3_ones.txt**: 0

## Comparative Analysis
- **best_question.txt**: Q3 (average: 4.1)
- **worst_question.txt**: Q2 (average: 3.6)
- **overall_average.txt**: 3.87 (116÷30)

## Summary Reports
- **response_distribution.txt**:
  ```
  Rating 5: 7 responses (3+1+3)
  Rating 4: 14 responses (4+5+5)
  Rating 3: 7 responses (2+3+2)
  Rating 2: 2 responses (1+1+0)
  Rating 1: 0 responses (0+0+0)
  ```

- **question_comparison.txt**:
  ```
  Q1: Average=3.9, Max=5, Min=2, Total=39
  Q2: Average=3.6, Max=5, Min=2, Total=36
  Q3: Average=4.1, Max=5, Min=3, Total=41
  ```

- **survey_analysis_report.txt**: Comprehensive analysis including all statistics, distribution patterns, and insights about response patterns

## Directory Structure
```
test9/
├── survey_responses.txt
├── q1_responses.txt, q2_responses.txt, q3_responses.txt
├── q1_total.txt, q2_total.txt, q3_total.txt
├── q1_average.txt, q2_average.txt, q3_average.txt
├── q1_max.txt, q1_min.txt, q2_max.txt, q2_min.txt, q3_max.txt, q3_min.txt
├── q1_fives.txt through q1_ones.txt (5 files)
├── q2_fives.txt through q2_ones.txt (5 files)
├── q3_fives.txt through q3_ones.txt (5 files)
├── best_question.txt, worst_question.txt
├── overall_average.txt
├── response_distribution.txt
├── question_comparison.txt
└── survey_analysis_report.txt
```