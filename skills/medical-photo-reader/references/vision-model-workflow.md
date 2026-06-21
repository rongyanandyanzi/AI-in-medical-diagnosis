# Vision Model Workflow

Use this reference when a base vision/multimodal model is available and the user uploads phone photos, screenshots, report images, or medical image photos.

The vision model is the front door. It decides what the input appears to be and extracts visible, non-diagnostic information before routing to OCR, DICOM tooling, or medical model workflows.

## What The Vision Model Should Do

Allowed:

- Classify the input type: lab report, physical exam report, radiology report, CT/MRI/X-ray/ultrasound photo, mixed bundle, or low-quality/unknown.
- Read visible text if OCR tooling is unavailable or as a first pass.
- Identify layout: table, report section, screenshot, film/screen photo, measurement frame.
- Identify visible labels, arrows, circles, calipers, measurement text, orientation marks, modality names, and body part labels.
- Judge basic image quality: blur, glare, crop, skew, low resolution, missing page/slice.
- Decide the next route: OCR, report parser, DICOM workflow, MONAI/model workflow, or request better input.

Not allowed:

- Diagnose from visual appearance of CT/MRI/ultrasound/X-ray phone photos.
- Infer disease status from a single slice/frame.
- Treat a visual impression as stronger than a formal report.
- Hide uncertainty when the image is cropped or low quality.

## Routing Logic

1. **Report or table photo**
   - Route to OCR/document extraction.
   - Ask for full page if cropped.
   - Extract abnormal flags and reference ranges.

2. **Radiology report photo**
   - Route to OCR and report parsing.
   - Prioritize findings/impression/conclusion.

3. **CT/MRI/X-ray/ultrasound phone photo**
   - Extract visible labels and annotations only.
   - Ask for the formal report and original DICOM if the user wants deeper analysis.
   - Do not run task-specific models on screen photos unless a model is explicitly validated for that exact input type.

4. **Original DICOM or medical image export**
   - Route to DICOM workflow.
   - After series validation, route to MONAI/model workflow if appropriate.

5. **Mixed bundle**
   - Prioritize formal report text.
   - Use scan photos only as supporting context.

## Output Template

For first-pass visual inspection:

1. **Input type**
2. **Visible text/labels**
3. **Visible annotations or measurements**
4. **Image quality limits**
5. **Recommended next route**
6. **What not to infer from this image**

## Good Model Behavior

Say:

- "This appears to be..."
- "The visible text says..."
- "I can see a measurement label, but I cannot verify the measurement from the photo alone."
- "This should be routed to OCR."
- "For actual CT/MRI interpretation, original DICOM and a clinician/radiologist are needed."

Avoid:

- "This lesion is..."
- "The scan is normal..."
- "There is no..."
- "This confirms..."
