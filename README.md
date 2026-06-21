# Medical Photo Reader Skill

A Codex skill for safely reading phone photos or screenshots of medical reports, lab reports, radiology reports, ultrasound reports, and CT/MRI/X-ray screen photos.

This project does **not** turn a language model into a doctor or radiologist. It provides a structured workflow for:

- extracting visible text from medical report photos,
- explaining medical terms in plain language,
- summarizing abnormal lab/checkup values,
- describing visible labels and annotations in scan screenshots,
- identifying uncertainty and missing source material,
- preparing practical questions for a clinician.

The default response language is **Simplified Chinese**, unless the user explicitly requests another language.

## Why This Exists

People often have medical information in messy forms:

- a phone photo of a physical exam report,
- a screenshot from a hospital mini-program,
- a lab report table,
- a radiology report image,
- a CT/MRI/ultrasound screen photo,
- a partial scan image shared through chat.

General models may overstate what they can infer from those images. This skill gives the model a safer, repeatable workflow: classify the input, extract what is visible, explain only what is supported, and clearly separate uncertainty from evidence.

## What It Can Do

- Read visible text, values, units, reference ranges, report conclusions, and recommendations.
- Explain terms such as LDL-C, eGFR, BI-RADS, TI-RADS, nodule, cystic, hypoechoic, impression, findings, and follow-up.
- Summarize abnormal or borderline report items.
- Identify that a CT/MRI/ultrasound photo is incomplete or low quality.
- Ask for the right missing materials: formal report, full-page photo, original DICOM, more adjacent slices, prior comparison, symptoms/history.
- Generate a doctor question checklist.

## What It Must Not Do

- Diagnose cancer, bleeding, fracture, embolism, infarct, infection, or benign/malignant status from phone photos.
- Overrule a formal radiology report.
- Treat one CT/MRI/ultrasound frame as the whole study.
- Pretend OCR is perfect when the image is blurry, cropped, reflective, or incomplete.

## Repository Layout

```text
medical-photo-reader-skill/
├── external/
│   └── skills/kimi-vision/      # optional submodule, Kimi OCR/vision skill reference
├── skills/
│   └── medical-photo-reader/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
│           ├── input-quality.md
│           └── repo-stack.md
├── docs/
│   ├── architecture.md
│   └── safety.md
├── examples/
│   └── prompts.md
├── .github/ISSUE_TEMPLATE/
│   ├── bug_report.md
│   └── feature_request.md
├── LICENSE
└── README.md
```

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/medical-photo-reader ~/.codex/skills/medical-photo-reader
```

Or run the included installer:

```bash
bash scripts/install.sh
```

Restart or refresh Codex if needed, then invoke it with:

```text
Use $medical-photo-reader to extract and explain this phone photo of a medical report in Simplified Chinese.
```

## Example Usage

```text
Use $medical-photo-reader to read this physical exam report screenshot. Tell me which values are abnormal, explain them simply in Chinese, and give me questions to ask my doctor.
```

```text
Use $medical-photo-reader on this CT screen photo. Tell me what visible text and markers can be read, what cannot be determined, and what source files I should ask the hospital for.
```

```text
Use $medical-photo-reader to explain this ultrasound report photo in Chinese. Do not diagnose; list what I should confirm with my doctor.
```

## Suggested GitHub Component Stack

This skill is an orchestration layer. If you want to build a runnable product around it, combine:

- A vision/multimodal model adapter for first-pass image classification and visible label reading. This repo includes `external/skills/kimi-vision` as an optional submodule reference.
- `PaddlePaddle/PaddleOCR` for OCR.
- OpenCV/Pillow for image cleanup and quality checks.
- Rule-based parsers for lab values and report sections.
- 3D Slicer, OHIF, or Weasis when original DICOM is available.
- MONAI/MONAI Label for validated task-specific medical image models.
- Medical VLM projects only as research or secondary assistance, never as sole diagnostic authority.

See [docs/architecture.md](docs/architecture.md) and [skills/medical-photo-reader/references/repo-stack.md](skills/medical-photo-reader/references/repo-stack.md).

## Medical Safety Notice

This repository is for information extraction, explanation, and workflow assistance. It is not a medical device and does not provide diagnosis or treatment advice. Always consult a qualified clinician for medical decisions.

## Validate

```bash
python3 scripts/validate.py
```

## External Skill Submodules

This repository may include external skill references under `external/skills/`.

Currently included:

- [`zzj2004/kimi-vision`](https://github.com/zzj2004/kimi-vision): a Kimi/Moonshot API OCR and image recognition skill. It is useful as a reference for the vision-model adapter layer, but it requires a `KIMI_API_KEY` and should not be used as a medical diagnostic authority.

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/rongyanandyanzi/AI-in-medical-diagnosis.git
```

Or initialize after cloning:

```bash
git submodule update --init --recursive
```
