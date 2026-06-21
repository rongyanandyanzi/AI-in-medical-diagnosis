# Architecture

This repository packages the Medical Photo Reader workflow as a Codex skill. The skill can be used by itself as a prompt/workflow layer, or as the policy layer for a future application.

## Recommended Pipeline

1. **Input intake**
   - Accept phone photos, screenshots, PDFs, and optional DICOM exports.
   - Preserve the original files.
   - Detect likely material type: report, lab table, radiology report, scan screenshot, ultrasound frame, mixed bundle.

2. **Vision model first pass**
   - Use a vision/multimodal model to classify the uploaded image type.
   - Extract visible labels, annotations, arrows, circles, calipers, and obvious report text.
   - Decide whether the next route is OCR, DICOM tooling, MONAI/model workflow, or "ask for better input."
   - Do not let this layer make a diagnosis from medical image appearance.

3. **Image quality check**
   - Check crop, skew, blur, glare, resolution, missing pages, missing slices, and missing labels.
   - Ask for better images when OCR or visual interpretation is unreliable.

4. **OCR/document extraction**
   - Use PaddleOCR as the preferred OCR engine.
   - Use OpenCV/Pillow for preprocessing.
   - Preserve units and reference ranges.
   - Mark unreadable text explicitly.

5. **Report parsing**
   - Extract sections such as findings, impression, conclusion, recommendation.
   - For lab/checkup reports, extract item name, value, unit, reference range, and abnormal flag.
   - Keep original terms for traceability.

6. **DICOM and slice handling**
   - For phone photos of CT/MRI/X-ray/ultrasound: extract visible text, labels, arrows, circles, and measurements only.
   - For original DICOM: inspect study/series metadata, sort slices, check geometry, and route to Slicer/OHIF/Weasis.
   - Convert to NIfTI or model-ready tensors only after the correct series is identified.

7. **Task-specific medical model workflow**
   - Use MONAI/MONAI Label or a validated model only when modality, anatomy, input format, and task match.
   - Visualize model output in a viewer before explanation.
   - Present model output as assisted analysis, not final diagnosis.

8. **LLM explanation**
   - Explain the extracted text in plain language.
   - Separate supported statements from uncertainty.
   - Produce missing-material requests and doctor questions.

9. **Safety gate**
   - Do not diagnose from phone photos.
   - Do not overrule formal reports.
   - Escalate urgent symptom reports to urgent medical care.

## MVP Scope

The minimum useful product is:

- PaddleOCR for report photos.
- Vision-model first pass for image classification and visible label extraction.
- Basic image quality checks.
- Lab value and report-section parsing.
- The `medical-photo-reader` skill as the explanation and safety layer.

## Future Scope

- OCR confidence display.
- Table reconstruction for lab reports.
- Chinese/English medical terminology glossary.
- DICOM upload path with pydicom/SimpleITK/dicom2nifti.
- MONAI/MONAI Label integration for validated task-specific models.
- Prior-report comparison.
- Clinician-facing export format.
