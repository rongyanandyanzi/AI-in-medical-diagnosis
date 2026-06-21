---
name: medical-photo-reader
description: Use this skill when the user uploads or asks about phone photos or screenshots of medical checkup reports, lab reports, radiology reports, ultrasound images, CT/MRI/X-ray screen photos, or other patient-facing medical documents, and wants help extracting text, explaining findings, organizing uncertainty, or preparing questions for a clinician. This skill is for OCR-style extraction, non-diagnostic visual description, safety-aware explanation, and triage of what additional source material is needed; it must not produce a definitive diagnosis from phone photos of medical images.
---

# Medical Photo Reader

## Purpose

Use this skill to help with phone-captured medical materials: physical exam reports, lab reports, radiology reports, ultrasound reports, CT/MRI/X-ray screen photos, printouts, and screenshots.

The goal is not to turn the model into a radiologist. The goal is to extract readable information, explain medical wording, separate what can and cannot be inferred, and produce a useful checklist for the user's doctor.

## Safety Boundary

Never give a definitive diagnosis from a phone photo of CT, MRI, ultrasound, X-ray, or a monitor/film screenshot. State uncertainty clearly.

Allowed:
- Read visible text, labels, measurements, arrows, circles, dates, modality names, report conclusions, and obvious annotations.
- Explain terms from a formal medical report.
- Summarize abnormal values or report impressions.
- Describe visible non-diagnostic image features at a high level.
- Ask for the formal report, original DICOM, more slices, or clearer images when needed.
- Prepare questions for a clinician.

Not allowed:
- Declare cancer/no cancer, bleeding/no bleeding, fracture/no fracture, benign/malignant, or emergency/no emergency based only on phone photos.
- Overrule the formal radiology report.
- Pretend a single CT/MRI slice or ultrasound frame represents the whole study.
- Treat OCR output as perfect when the image is blurry, skewed, cropped, reflective, or partially blocked.

If the user reports urgent symptoms such as severe chest pain, stroke-like symptoms, severe breathing difficulty, new weakness/numbness, heavy bleeding, severe trauma, or altered consciousness, advise urgent medical care rather than continuing image interpretation.

## Workflow

### 1. Classify the Input

First identify the material type:
- Medical report photo: printed or screenshot text report.
- Lab/checkup report: tables with test names, values, reference ranges.
- Radiology report: findings/impression text for CT/MRI/X-ray/ultrasound.
- Medical image phone photo: CT/MRI/X-ray/ultrasound image captured from screen, film, or paper.
- Mixed bundle: report plus images.
- Unknown/low-quality image.

If there are multiple files, group them by type before interpreting.

### 2. Extract What Is Visible

For report/document photos:
- Extract exam type, body part, date, facility if visible, findings, impression/conclusion, recommendations, abnormal values, units, and reference ranges.
- Preserve original key terms when useful; translate/explain afterward.
- Mark unreadable fields as unreadable rather than guessing.

For CT/MRI/X-ray/ultrasound photos:
- Extract visible modality, body part, orientation marks, series/window labels, measurements, arrows/circles, captions, and timestamps.
- Describe whether the image is a photo of a screen/film/report page.
- Note quality problems: glare, blur, angle, crop, low resolution, missing slices, missing window/sequence information.

### 3. Choose The Interpretation Mode

If a formal report is present:
- Treat the formal report as the primary source.
- Explain the report in plain language.
- Use image photos only to orient the user to what the report may be referring to.

If only medical image photos are present:
- Give a non-diagnostic explanation of what can be read from the visible labels and obvious annotations.
- State that complete interpretation requires original DICOM and a radiologist/clinician.
- Ask for the formal report or DICOM export.

If original DICOM or a full imaging export is present:
- Switch from "phone photo reading" to the DICOM workflow.
- Use DICOM viewers/slice tooling to inspect metadata, series, windowing, and representative frames.
- Only use task-specific medical AI models when the modality, anatomy, task, and model validation match.
- Keep outputs framed as assisted analysis or structured observations, not final diagnosis.

If only lab/checkup report photos are present:
- Summarize abnormal or borderline items.
- Explain likely meaning at a general level.
- Avoid diagnosing; recommend discussing with a clinician, especially for serious or repeated abnormalities.

### 4. Output Format

Use this structure by default:

1. **资料类型**
   - What the upload appears to be.

2. **我能读到的信息**
   - Key visible text, values, labels, measurements, and report conclusions.

3. **通俗解释**
   - Plain-language explanation of report terms or visible annotations.

4. **不能确定的地方**
   - What cannot be inferred from this image quality or limited slice/frame.

5. **建议补充**
   - Formal report, original DICOM, clearer photo, more continuous slices, ultrasound report text, prior comparison study, symptoms/history.

6. **建议问医生的问题**
   - Concrete questions tailored to the report/image.

When the user asks for a shorter answer, collapse to: `结论摘要`, `需要确认`, `问医生的问题`.

## Component Stack

For implementation or product planning, use this combined stack:
- Vision/multimodal model: classify the image type, read visible layout/labels/annotations, and decide whether OCR, DICOM, or model workflow is needed.
- OCR/document extraction: PaddleOCR first; Tesseract/OpenCV only as a simple fallback.
- Medical report extraction: regular expressions and section parsing for findings/impression/conclusion/reference ranges.
- Image preprocessing: crop, deskew, denoise, contrast enhancement, glare/blur quality checks.
- DICOM viewers/slice processing: 3D Slicer, OHIF, Weasis, pydicom, SimpleITK, and dicom2nifti only when original DICOM is available.
- Medical AI frameworks: MONAI/MONAI Label only for task-specific validated models, never raw phone photos.
- Medical VLMs: use only as research/secondary assistance; never as a sole diagnostic source.

Read `references/repo-stack.md` when the user asks which GitHub repos to combine or how to build the pipeline.
Read `references/input-quality.md` when the user asks how to photograph reports or medical images.
Read `references/vision-model-workflow.md` when the user asks how the base vision model should inspect uploaded phone photos, screenshots, or scan images before OCR/DICOM routing.
Read `references/dicom-workflow.md` when the user provides original DICOM, asks about CT/MRI slice handling, or wants 3D Slicer/OHIF/Weasis integration.
Read `references/model-workflow.md` when the user asks how to connect MONAI/MONAI Label or task-specific medical image models.

## Response Tone

Be calm, practical, and explicit about limits. The user may be anxious. Do not exaggerate risk, but do not minimize uncertainty. Prefer useful next steps over dramatic warnings.
