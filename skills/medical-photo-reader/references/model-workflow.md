# Medical Model Workflow

Use this reference when connecting MONAI, MONAI Label, or other task-specific medical image models. This workflow is only appropriate for original DICOM, NIfTI, or standardized medical image exports, not phone photos of screens or films.

## Principle

Medical AI models are task-specific tools. A model that works for one modality, anatomy, or disease should not be reused for another without validation.

Before running a model, match:

- modality: CT, MRI, X-ray, ultrasound, pathology, etc.
- anatomy: chest, abdomen, brain, spine, breast, thyroid, etc.
- task: segmentation, detection, classification, retrieval, report generation.
- input format: DICOM, NIfTI, PNG/JPEG, spacing, orientation, intensity normalization.
- intended output: mask, bounding box, label, probability, embedding, draft report.
- validation evidence: dataset, metric, external validation, known limitations.

## Recommended Repos

### Framework

- `Project-MONAI/MONAI`: PyTorch-based healthcare imaging framework.
- `Project-MONAI/MONAILabel`: AI-assisted annotation and active learning, integrates with 3D Slicer and OHIF.

### View/Annotation Integration

- `Slicer/Slicer`: use for local annotation, segmentation masks, and visual verification.
- `OHIF/Viewers`: use for web-based review and DICOMweb workflows.

### Research Models

- `ibrahimethemhamamci/CT2Rep`: 3D CT report generation research.
- `wang-zhanyu/R2GenGPT`: radiology report generation research.
- `ttanida/rgrg`: region-guided radiology report generation research.
- `mbzuai-oryx/XrayGPT`: chest X-ray vision-language research.
- `richard-peng-xia/MMed-RAG`: multimodal medical RAG research.

Treat research models as experiments unless validated for the exact target workflow.

## Safe Model Selection Checklist

Ask:

- What question is the model supposed to answer?
- What modality and anatomy was the model trained for?
- Does the input match the expected format and preprocessing?
- Does the model require 2D slices or 3D volumes?
- Does it output a mask, score, label, or draft text?
- What are the failure modes?
- How will a human verify the output?

If the answer is unclear, do not run or trust the model for clinical interpretation.

## MONAI Route

1. Convert or load the correct series.
2. Apply model-specific transforms.
3. Run inference.
4. Save outputs separately from original data.
5. Visualize masks/scores in Slicer/OHIF.
6. Produce a cautious explanation with uncertainty.

## MONAI Label Route

Use MONAI Label when the goal is interactive annotation:

- start a MONAI Label server with a selected app/model,
- connect 3D Slicer or OHIF,
- request segmentation/detection suggestions,
- allow human correction,
- iterate on labels or active learning.

This is best for segmentation support, not direct final diagnosis.

## Output Rules

Model outputs should be phrased as:

- "The model marked..."
- "The segmentation suggests..."
- "This score would need clinical review..."
- "This is not a diagnosis."

Avoid:

- "The patient has..."
- "No disease is present..."
- "This proves..."
- "This rules out..."

## When To Refuse Or Defer

Defer to clinician/manual review when:

- only phone photos are available,
- the modality/anatomy does not match the model,
- the input is incomplete,
- preprocessing cannot be verified,
- model validation is unknown,
- the user asks for a definitive diagnosis.
