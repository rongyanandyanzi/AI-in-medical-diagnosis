# Example Prompts

The skill defaults to Simplified Chinese output unless another language is requested.

## Physical Exam Or Lab Report

```text
Use $medical-photo-reader to read this physical exam report screenshot. Extract the visible values, mark abnormal items, explain them in plain Chinese, and list questions for my doctor.
```

## Radiology Report Photo

```text
Use $medical-photo-reader to explain this CT report photo. Please identify the findings and impression sections, translate the terms into plain language, and tell me what I should confirm with the doctor.
```

## CT/MRI/X-ray Screen Photo

```text
Use $medical-photo-reader to inspect this CT screen photo. Only tell me what visible labels, measurements, arrows, or annotations can be read. Also tell me what cannot be diagnosed from this photo.
```

## Ultrasound Image Or Report

```text
Use $medical-photo-reader for this ultrasound image/report photo. Read visible measurements and labels, explain terms such as nodule/cystic/hypoechoic if present, and prepare doctor questions.
```

## Mixed Bundle

```text
Use $medical-photo-reader on these images. Group them into report pages and scan photos, prioritize the formal report, then summarize what is clear, what is uncertain, and what I should ask my doctor.
```

## Pathology / Biopsy Report

```text
Use $medical-photo-reader to read this pathology report photo. Extract the diagnosis, staging, margin status, lymph node results, and any IHC markers visible. Explain each finding in plain Chinese and list questions I should ask my oncologist.
```

```text
Use $medical-photo-reader on this biopsy report. Tell me what the diagnosis line says, what the grade and Ki-67 mean in simple terms, and what information is missing or unreadable from this photo.
```

## Serial Reports / Comparison Over Time

```text
Use $medical-photo-reader to compare these two lab reports from different dates. Extract each one separately, then show me what changed, what crossed the normal range, and what trend I should ask my doctor about.
```

```text
Use $medical-photo-reader on these two ultrasound reports taken six months apart. For each one, extract the nodule size and assessment category, then tell me what changed between the two and what questions I should ask at my next appointment.
```

## Functional Test Report (ECG / PFT / Sleep Study)

```text
Use $medical-photo-reader to read this ECG report photo. Extract the rhythm, rate, and the doctor's conclusion if visible. Explain any abnormal findings in plain Chinese and list what I should confirm with my cardiologist.
```

```text
Use $medical-photo-reader on this pulmonary function test report. Extract FVC, FEV1, and FEV1/FVC, explain what the pattern means in general terms, and tell me what questions to bring to my respiratory doctor.
```
