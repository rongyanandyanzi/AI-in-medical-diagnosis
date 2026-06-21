# Input Quality Guidance

Use this when asking the user for better photos or explaining why interpretation is limited.

## For Medical Reports, Lab Reports, And Checkup Forms

Ask for:
- Full page, not cropped.
- Good light without glare.
- Camera parallel to the page.
- High resolution.
- One page per image.
- Include units and reference ranges.
- Upload PDF/export if available.

Acceptable output:
- OCR extraction.
- Plain-language explanation.
- Abnormal-value summary.
- Follow-up questions for doctor.

Common limitations:
- Low contrast.
- Wrinkled paper.
- Tiny table text.
- Missing reference range column.
- Handwritten notes.

## For CT/MRI/X-ray Screen Or Film Photos

Ask for:
- Formal radiology report first.
- Original DICOM if possible.
- Clear full-screen image including labels.
- Multiple continuous adjacent slices, not only one screenshot.
- Window/sequence labels if visible.
- Prior comparison images/report when relevant.

Explain:
- A single phone photo is not the full imaging study.
- CT/MRI interpretation often needs scrolling through the whole series.
- Different windows/sequences reveal different anatomy.
- Glare, blur, angle, and screen compression can hide important findings.

Allowed output:
- Identify visible modality/body part/labels.
- Describe visible annotations such as arrows, circles, measurement calipers.
- Explain what the formal report says if present.
- List what cannot be determined.

Avoid:
- Calling a lesion benign/malignant.
- Ruling in/out cancer, bleeding, fracture, infarct, embolism, or infection.
- Measuring from a phone photo unless the visible measurement label is already present.

## For Ultrasound Photos

Ask for:
- The ultrasound report text.
- All frames with measurement labels.
- Organ/body part and clinical reason for exam.

Explain:
- Ultrasound is operator-dependent.
- A still frame rarely represents the whole exam.
- The report and measurements are more reliable than a single phone photo.

Allowed output:
- Read visible measurements and labels.
- Explain terms such as cystic, solid, hypoechoic, echogenic, nodule, BI-RADS/TI-RADS if present.
- Ask doctor-oriented follow-up questions.
