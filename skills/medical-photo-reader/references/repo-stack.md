# Repo Stack For Medical Photo Reader

This reference maps the user-facing need to GitHub components.

## Best Combined Architecture

### Layer 1: Vision Model First Pass

Purpose: use a vision/multimodal model to classify uploaded images and extract visible, non-diagnostic information before routing.

Relevant skill/submodule:
- `zzj2004/kimi-vision` - optional Codex skill reference for OCR and image recognition through Kimi/Moonshot API. Requires `KIMI_API_KEY`; not a medical diagnostic model.

Relevant medical VLM research:
- `mbzuai-oryx/XrayGPT` - chest radiograph summarization research.
- `richard-peng-xia/MMed-RAG` - multimodal medical RAG research.
- `yezanting/Med-VLM-Bench-Summary` - benchmark/index for medical VLMs.

Recommended use:
- Classify whether the upload is a report, lab table, radiology report, phone photo of a scan, or DICOM-related export.
- Extract visible labels, annotations, and obvious text.
- Route to OCR, DICOM workflow, or model workflow.
- Never use this layer alone for diagnosis.

### Layer 2: Input Intake

Purpose: accept phone photos, screenshots, PDF exports, report images, and optional DICOM files.

Required behavior:
- Detect document vs medical image vs mixed bundle.
- Keep original files.
- Record source quality: blur, glare, crop, skew, resolution, missing pages/slices.

Suggested implementation:
- OpenCV for blur/glare/skew checks and cleanup.
- Pillow for basic image handling.

### Layer 3: OCR And Document Understanding

Primary repo:
- `PaddlePaddle/PaddleOCR` - best general OCR choice for multilingual medical reports, checkup reports, screenshots, and PDFs.

Useful smaller references:
- `binfen/medical_report_OCR` - Chinese medical report phone-photo OCR idea; small and not mature.
- `tayade-aniket/Medical-Report-OCR-YOLO-Tesseract` - YOLO text detection plus Tesseract extraction, useful as a prototype pattern.
- `spj114/Medical-Document-Ocr` - FastAPI, OpenCV, Tesseract web/API pattern.
- `lakshan64/lab-report-ocr-api` - lab-report OCR API pattern.

Recommended use:
- Use PaddleOCR as the production-grade OCR engine.
- Use smaller repos for layout ideas only.
- Post-process OCR with deterministic parsing before asking an LLM to explain it.

### Layer 4: Medical Report Parsing

Relevant repos:
- `MoMarky/radiology-report-extraction` - extracts findings and impression sections from radiology reports.
- `ehtbanton/RadCount` - radiology report extraction and annotation tool.

Recommended fields:
- Patient/report metadata if visible.
- Exam name and modality.
- Body part.
- Findings.
- Impression/conclusion.
- Recommendations.
- Measurements.
- Abnormal lab values with units and reference ranges.

### Layer 5: DICOM Viewing And Slice Processing

Use only when original DICOM or a real medical image export is available.

Relevant repos:
- `Slicer/Slicer` - best local desktop viewer and analysis platform.
- `OHIF/Viewers` - best web DICOM viewer.
- `nroduit/Weasis` - clinical-style DICOM/PACS viewer.
- `Project-MONAI/MONAILabel` - AI-assisted labeling integrated with Slicer/OHIF.

Programmatic tools:
- `pydicom` - DICOM metadata and pixel access.
- `SimpleITK` - DICOM series loading and geometry-aware image processing.
- `dicom2nifti` - DICOM series to NIfTI conversion.
- `nibabel` - NIfTI read/write.

Do not use these as primary tools for phone photos of screens or films. For phone photos, they can at most inspire UI/workflow.

### Layer 6: Medical AI Models

For DICOM or standardized medical images:
- `Project-MONAI/MONAI` - model framework.
- `Project-MONAI/MONAILabel` - annotation and segmentation workflows.

For research report generation:
- `ibrahimethemhamamci/CT2Rep` - 3D CT report generation research.
- `wang-zhanyu/R2GenGPT` - report generation with frozen LLMs.
- `ttanida/rgrg` - region-guided radiology report generation.

For medical vision-language research:
- `mbzuai-oryx/XrayGPT` - chest radiograph summarization research.
- `richard-peng-xia/MMed-RAG` - multimodal medical RAG research.
- `yezanting/Med-VLM-Bench-Summary` - benchmark/index for medical VLMs.

Recommended use:
- Treat these as research/secondary components.
- Do not use them to diagnose from phone photos.
- Validate by task, modality, dataset, and clinical workflow before any serious use.

## Practical Product Pipeline

1. Upload images/PDFs.
2. Classify input type.
3. Run vision-model first pass for visible labels/annotations and routing.
4. Run image quality check.
5. If document/report: run OCR and parse sections.
6. If phone photo of CT/MRI/ultrasound/X-ray: extract visible labels and annotations only.
7. If original DICOM: route to Slicer/OHIF/Weasis plus pydicom/SimpleITK/dicom2nifti as needed.
8. If model task matches validated inputs: run MONAI/MONAI Label or task-specific model.
9. LLM produces safety-aware explanation.
10. Output doctor questions and missing-material checklist.

## Minimal MVP

For the user's current goal, the MVP is:
- PaddleOCR
- OpenCV preprocessing
- LLM explanation prompt following `SKILL.md`
- Report parser for findings/impression/lab values

Do not start with CT2Rep or MONAI unless original DICOM and a specific validated task are available.
