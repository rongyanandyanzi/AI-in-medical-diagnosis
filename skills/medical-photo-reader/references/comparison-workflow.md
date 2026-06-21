# Comparison And Serial Study Workflow

Use this reference when the user uploads reports or images from more than one time point and wants to track changes, compare results over time, or understand trends.

## When To Use This Workflow

- User uploads two or more lab reports from different dates and asks whether anything has changed.
- User uploads CT/MRI reports or screen photos from before and after treatment.
- User shows a series of ultrasound reports tracking a nodule or lesion over time.
- User asks whether a tumor marker or lab value is going up or down.
- User has results from one hospital and a second-opinion report or repeat test from another.

## Step 1: Inventory All Inputs

Before comparing, list all uploaded materials:

- Date of each report or image (from visible header, watermark, or filename).
- Report type for each (lab, radiology, pathology, ultrasound, functional test).
- Source facility if visible.

If dates are not visible or the order is unclear, ask the user to confirm before proceeding.

Note: pathology diagnoses do not "improve over time" in the way lab values do. For pathology, use `pathology-workflow.md` to explain the report; only use this workflow if comparing surgical staging reports from pre- and post-treatment contexts, which requires caution.

## Step 2: Extract Each Report Separately

Process each report independently before comparing:

- Do not mix findings from different dates in the extraction step.
- For lab reports: extract each item name, value, unit, and reference range per date.
- For radiology/imaging reports: extract findings and impression per date.
- For ultrasound serial tracking: extract all lesion measurements, character descriptions, and assessment categories per date.

## Step 3: Compare And Highlight Changes

After separate extraction, produce a structured comparison.

### For Lab/Checkup Reports

Build a side-by-side summary:

| 项目 | 第一次（日期） | 第二次（日期） | 变化 |
|------|--------------|--------------|------|
| 示例指标 | X 单位 | Y 单位 | ↑ / ↓ / → |

Flag:
- Values that crossed from within reference range to outside, or back.
- Values with a large absolute or percentage change.
- Consistent trends across three or more time points.

Caveat: different laboratories may use different reference ranges, calibration standards, and measurement methods. A numerical change may partly reflect lab-to-lab variability rather than a real biological change. Note this clearly when the facility or test platform changed.

### For Radiology/Imaging Reports

Summarize what changed between dates using the formal report text:

- New findings not mentioned in the earlier report.
- Findings that resolved or were no longer described.
- Size or character changes for described lesions (e.g., "nodule increased from 8 mm to 11 mm").
- Changes in impression or conclusion wording.

Important: do not attempt to compare measurements directly from phone photos of CT/MRI screens. Screen photo measurements are unreliable. Only compare measurements that appear explicitly in the formal report text.

### For Ultrasound Serial Tracking

Common use case: thyroid nodule, breast nodule, liver lesion, or ovarian cyst follow-up.

Extract for each date:
- Lesion size (all dimensions if visible).
- Character description (solid/cystic/mixed, echogenicity, margins, internal vascularity).
- Assessment category (TI-RADS, BI-RADS, or equivalent) if stated.
- Recommendation (follow-up interval, biopsy, or discharge).

Highlight if:
- The assessment category changed (e.g., TI-RADS 3 → TI-RADS 4).
- Size changed beyond typical measurement variability (generally ≥ 2 mm increase or ≥ 20% volume increase is clinically noted, but the clinician interprets significance).
- Character changed (e.g., new internal vascularity, calcification, irregular margins).

### For Tumor Marker Trends

Tumor markers (CEA, CA125, CA19-9, AFP, PSA, etc.) are most meaningful as trends, not single values.

- Extract each value with date and units.
- Note the reference range shown at the time of each test.
- Describe the direction of change across time points.
- Do not interpret the clinical significance of the trend — that depends on treatment history, clinical context, and specific cancer type. Generate a question for the clinician instead.

## Step 4: Limitations To State Clearly

Always include:

- Comparison is only as reliable as the readability of each uploaded report.
- Different facilities, machines, or operators introduce variability that can look like a change.
- Apparent stability does not mean the condition is resolved.
- Apparent worsening or improvement in a number needs clinical context to interpret.
- Do not use "improving" or "worsening" as a conclusion — state what the numbers show and let the clinician interpret.

## Output Structure For Comparison

1. **资料清单** — All uploads listed with date, type, and facility if visible.
2. **各次结果摘要** — Brief separate extraction from each time point.
3. **变化对比** — Side-by-side table or structured change summary.
4. **需要注意的变化** — Items that crossed thresholds, changed substantially, or show a consistent trend.
5. **不确定因素** — Different labs or machines, unreadable dates, missing time points, measurement variability.
6. **建议问医生的问题** — Trend-specific questions for the clinician.

## Example Doctor Questions

- 这两次检查结果相比，您认为这些变化有临床意义吗？
- 这个指标持续偏高（或持续上升），是需要治疗还是继续观察？
- 两次报告的描述措辞有变化，是病情真的变了，还是不同医生描述方式不同？
- 结节从 X mm 变成 Y mm，这个变化在测量误差范围内吗？
- 不同医院的检验结果直接对比合理吗，还是需要考虑参考范围的差异？
- 我应该多久复查一次来追踪这个指标或病灶？
