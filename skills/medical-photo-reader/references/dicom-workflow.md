# DICOM Workflow

Use this reference only when the user has original DICOM, NIfTI, or a full medical imaging export. Do not use this workflow for ordinary phone photos of screens, films, or printed images.

## Purpose

The DICOM workflow adds the missing layer between phone-photo reading and medical AI models:

- ingest original DICOM files,
- inspect metadata and series,
- reconstruct ordered slices,
- route studies to a viewer,
- export standardized image volumes for task-specific models,
- preserve uncertainty and clinician review.

## Recommended Tools

### Viewers

- `Slicer/Slicer`: desktop viewer and analysis platform; good for local CT/MRI review, segmentation, registration, and extension workflows.
- `OHIF/Viewers`: browser-based DICOM viewer; good for web apps, DICOMweb, and clinician-facing review.
- `nroduit/Weasis`: clinical-style DICOM/PACS viewer with DICOMweb and PACS integration.

### Programmatic Slice Handling

- `pydicom`: read DICOM metadata and pixel arrays.
- `SimpleITK`: load DICOM series, handle spacing/orientation, convert to volume arrays.
- `dicom2nifti`: convert DICOM series to NIfTI for ML pipelines.
- `nibabel`: read/write NIfTI after conversion.

## Intake Checklist

Before model inference, determine:

- Modality: CT, MR, US, CR/DX, MG, PET, etc.
- Body part and study description.
- Series count and series descriptions.
- Slice thickness, spacing, orientation, and reconstruction kernel.
- Contrast status when visible.
- Whether the study is complete or only partial.
- Whether prior studies or reports are available.

## Safe DICOM Processing Steps

1. **Keep the original DICOM untouched**
   - Work on a copied input directory.
   - Do not overwrite metadata or pixel data.

2. **Group by study and series**
   - Use StudyInstanceUID and SeriesInstanceUID.
   - Avoid mixing series from different phases, windows, or reconstructions.

3. **Sort slices correctly**
   - Prefer ImagePositionPatient and ImageOrientationPatient.
   - Use InstanceNumber only as a fallback.

4. **Check geometry**
   - Confirm slice spacing and orientation.
   - Detect missing slices or irregular spacing.

5. **Choose route**
   - Viewer route: Slicer/OHIF/Weasis for visual review and annotation.
   - Model route: convert validated series to model-required format.

6. **Preserve clinical boundary**
   - Output observations, measurements, segmentation masks, or model scores.
   - Do not present automated output as final diagnosis.

## When To Use A Viewer

Use Slicer/OHIF/Weasis when:

- the user wants to browse CT/MRI slices,
- the user has a DICOM folder or ZIP,
- annotations/measurements are needed,
- a model output mask needs visual verification,
- screenshots need to be generated from original data.

## When To Use Conversion

Use DICOM-to-NIfTI conversion when:

- a MONAI model expects NIfTI,
- spacing/orientation must be standardized,
- a 3D volume model is used,
- batch processing is needed.

Never convert blindly across all series. Pick the correct series for the task.

## Output Template

When reporting DICOM workflow results, use:

1. **Study/series identified**
2. **Data quality and completeness**
3. **Viewer/model route chosen**
4. **What was extracted or processed**
5. **What remains uncertain**
6. **What a clinician should confirm**
