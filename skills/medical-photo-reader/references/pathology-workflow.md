# Pathology Report Workflow

Use this reference when the user uploads a photo or screenshot of a pathology report, biopsy report, surgical pathology report, or cytology report.

## What Pathology Reports Are

Pathology reports describe tissue or cell samples examined under a microscope. They are written by a pathologist, not a radiologist. Common types:

- Surgical pathology: tissue removed during surgery (tumor resection, organ removal).
- Biopsy report: core needle biopsy, excisional biopsy, punch biopsy.
- Cytology report: fine needle aspiration (FNA), cervical smear (Pap), pleural or ascites fluid.
- Frozen section: intraoperative rapid diagnosis — always followed by a final paraffin report, which is definitive.
- Immunohistochemistry (IHC) addendum: protein marker testing on tumor tissue, sometimes issued as a separate addendum after the main report.

## What To Extract

From a pathology report photo, extract:

- Patient and specimen information if visible: date, specimen type, body part, clinical history.
- Gross description: size, shape, color, margins as described in the report text.
- Microscopic description: cell type, differentiation, necrosis, vascular or perineural invasion if mentioned.
- Diagnosis line: the formal diagnostic statement.
- Staging if present: TNM (T, N, M values), AJCC stage, Gleason score, FIGO stage, or equivalent.
- Margin status: positive, negative, close, distance to margin in millimeters.
- Lymph node status: number examined, number positive.
- IHC results: marker name and result (positive/negative/score/percentage), e.g., ER, PR, HER2, Ki-67, PD-L1, ALK, EGFR, KRAS.
- Any note about pending addenda or results not yet returned.

Mark any field that is unreadable due to blur, crop, or poor photo quality.

## Key Terms: Plain-Language Explanations

Explain these terms if they appear:

- **分化程度 / Grade**: how closely tumor cells resemble normal cells. Well differentiated (低级别) means cells still look fairly normal and tend to grow slower. Poorly differentiated (高级别) means cells look very abnormal.
- **Ki-67**: a marker of how fast tumor cells are dividing. Higher percentage means faster proliferation rate.
- **切缘 / Margin**: the edge of the removed tissue. Negative margin (阴性) means no tumor cells at the cut edge — the surrounding tissue was clear. Positive margin (阳性) means tumor cells reach the edge and re-excision may be discussed.
- **淋巴结 / Lymph node**: nodes involved in immune filtering. Positive lymph nodes mean cancer cells were found there, which affects staging and treatment planning.
- **TNM 分期**: T = size or extent of primary tumor; N = regional lymph node involvement; M = distant metastasis (M0 = none found, M1 = found).
- **Gleason 评分**: prostate cancer only. Scores 6–10; higher scores indicate more aggressive disease.
- **ER / PR / HER2**: hormone receptor and growth factor receptor markers for breast cancer. Positive or negative status guides treatment — explain what the value says, do not recommend a treatment.
- **PD-L1 / ALK / EGFR / KRAS / ROS1**: molecular markers used for targeted therapy or immunotherapy selection. Their significance depends on cancer type and current guidelines; explain the value only in general terms.
- **原位 / In situ**: cancer cells are confined to the original tissue layer and have not invaded surrounding tissue.
- **浸润性 / Invasive**: cancer cells have grown beyond the original tissue layer into surrounding tissue.
- **冰冻切片 / Frozen section**: a rapid intraoperative result; the final paraffin report issued days later is the definitive diagnosis.

## Safety Boundary

Allowed:
- Extract and explain the visible diagnosis, staging, margin status, lymph node status, and IHC results.
- Explain what each term means in general language.
- Summarize what the report says plainly.
- Note missing, pending, or unreadable fields.
- Prepare questions for the oncologist, surgeon, or pathologist.

Not allowed:
- Predict prognosis, survival rate, or curability from a single report.
- Recommend or adjust a treatment regimen.
- Interpret IHC results beyond what the report explicitly states.
- State that a diagnosis is wrong or that a second opinion would definitely change it (though seeking one is always the patient's right).
- Comment on whether staging is accurate without seeing the full clinical picture.

## Interpretation Mode

If only the pathology report is present:
- Extract the diagnosis, staging, and key markers.
- Explain each section in plain language.
- List what is unclear or unreadable.
- Generate a doctor question checklist.

If the pathology report accompanies imaging (CT/MRI/ultrasound):
- Treat the pathology report as the definitive tissue diagnosis.
- Use imaging to provide anatomical context only.
- Do not use imaging alone to override or adjust the pathology diagnosis.

If the report includes IHC results:
- List each marker and its result.
- Explain what the marker is in general terms.
- Do not recommend a targeted therapy; note only that the oncologist will use these results to guide treatment options.

If the report is a frozen section:
- Note that it is preliminary.
- Remind the user to wait for the final paraffin/permanent section report before drawing conclusions.

## Output Structure For Pathology Reports

1. **资料类型** — Pathology report type (biopsy, surgical, cytology, IHC addendum) and specimen source.
2. **我能读到的信息** — Diagnosis, staging, margin status, lymph node results, IHC markers.
3. **通俗解释** — Plain-language meaning of each finding.
4. **不能确定的地方** — Unreadable fields, pending IHC, staging components not shown, frozen vs. final.
5. **建议补充** — Full report if cropped, IHC addendum if pending, imaging reports for anatomical context.
6. **建议问医生的问题** — Questions for the oncologist, surgeon, or pathologist.

## Example Doctor Questions

- 这份病理报告是最终结果，还是还有补充报告（比如免疫组化）待出？
- 切缘阴性，但距离是多少毫米？这个距离足够安全，还是需要再切除？
- Ki-67 / HER2 / PD-L1 这个结果对我的治疗方案有什么具体影响？
- 淋巴结有转移，接下来还需要做哪些检查来确认分期？
- 这个分期对应的标准治疗方案是什么？需要化疗、放疗还是靶向治疗？
- 是否建议做基因检测（NGS 或基因组分析）来指导后续治疗？
- 我是否需要请病理科医生会诊，或者到上级医院复核这份报告？
