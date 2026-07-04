# NASA-TLX (Task Load Index) Survey Instructions

**Administered:** End of each sprint (Friday afternoon)
**Duration:** ~10 minutes per developer
**Confidential:** Individual responses, no team discussion

## Part 1: Raw Score Assessment

Rate each dimension on a scale of 0-100.

### Mental Demand
**Question:** How mentally demanding was the sprint work?
- 0 = Very Low (minimal cognitive effort)
- 50 = Moderate (reasonable concentration needed)
- 100 = Very High (intense focus required)

**Your Rating: _____ (0-100)**

### Physical Demand
**Question:** How physically demanding was the sprint work?
- 0 = Very Low (minimal physical effort)
- 50 = Moderate (some physical activity)
- 100 = Very High (heavy physical demands)

**Your Rating: _____ (0-100)**

### Temporal Demand
**Question:** How hurried or rushed was the pace of work?
- 0 = Very Low (plenty of time)
- 50 = Moderate (some deadline pressure)
- 100 = Very High (very tight deadlines)

**Your Rating: _____ (0-100)**

### Performance
**Question:** How successful were you in accomplishing what you were asked to do?
- 0 = Perfect (achieved all goals)
- 50 = Moderate (some goals achieved)
- 100 = Failure (failed to meet most objectives)

**Your Rating: _____ (0-100)**

### Effort
**Question:** How hard did you have to work to accomplish your level of performance?
- 0 = Very Low (minimal effort)
- 50 = Moderate (reasonable effort)
- 100 = Very High (exhausting effort)

**Your Rating: _____ (0-100)**

### Frustration
**Question:** How insecure, discouraged, irritated, stressed were you?
- 0 = Very Low (confident and satisfied)
- 50 = Moderate (some frustration)
- 100 = Very High (highly frustrated and stressed)

**Your Rating: _____ (0-100)**

## Part 2: Pairwise Comparisons

For each pair below, mark which dimension was MORE IMPORTANT in contributing to your overall workload:

| Pair | Question | Choose |
|------|----------|--------|
| 1 | Mental Demand vs. Physical Demand | ☐ MD / ☐ PD |
| 2 | Mental Demand vs. Temporal Demand | ☐ MD / ☐ TD |
| 3 | Mental Demand vs. Performance | ☐ MD / ☐ Perf |
| 4 | Mental Demand vs. Effort | ☐ MD / ☐ Effort |
| 5 | Mental Demand vs. Frustration | ☐ MD / ☐ Frust |
| 6 | Physical Demand vs. Temporal Demand | ☐ PD / ☐ TD |
| 7 | Physical Demand vs. Performance | ☐ PD / ☐ Perf |
| 8 | Physical Demand vs. Effort | ☐ PD / ☐ Effort |
| 9 | Physical Demand vs. Frustration | ☐ PD / ☐ Frust |
| 10 | Temporal Demand vs. Performance | ☐ TD / ☐ Perf |
| 11 | Temporal Demand vs. Effort | ☐ TD / ☐ Effort |
| 12 | Temporal Demand vs. Frustration | ☐ TD / ☐ Frust |
| 13 | Performance vs. Effort | ☐ Perf / ☐ Effort |
| 14 | Performance vs. Frustration | ☐ Perf / ☐ Frust |
| 15 | Effort vs. Frustration | ☐ Effort / ☐ Frust |

## Part 3: Weight Calculation

Count how many times each dimension was chosen:

| Dimension | Times Chosen | Weight = Chosen / 15 |
|-----------|--------------|----------------------|
| Mental Demand | [__] | [__ / 15] = |
| Physical Demand | [__] | [__ / 15] = |
| Temporal Demand | [__] | [__ / 15] = |
| Performance | [__] | [__ / 15] = |
| Effort | [__] | [__ / 15] = |
| Frustration | [__] | [__ / 15] = |

## Part 4: Final Score Calculation

**Formula:**
```
Overall Workload = (MD_raw × MD_weight + PD_raw × PD_weight + 
                    TD_raw × TD_weight + Perf_raw × Perf_weight + 
                    Effort_raw × Effort_weight + Frust_raw × Frust_weight) / 15
```

**Example:**
- MD: 75 × 0.33 = 24.75
- PD: 15 × 0.07 = 1.05
- TD: 45 × 0.20 = 9.00
- Perf: 25 × 0.13 = 3.25
- Effort: 70 × 0.27 = 18.90
- Frust: 40 × 0.00 = 0.00
- **Sum: 56.95 / 15 = 3.80** (on 0-100 scale)

## Interpretation

- **0-30:** Low workload — manageable, low stress
- **30-50:** Moderate workload — reasonable demand
- **50-70:** High workload — significant cognitive demands
- **70-100:** Very high workload — exhausting, high stress

---
**Submit results to Scrum Master by end of Friday.**
