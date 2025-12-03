# OpenCV Region and Pixel Operations

This repository contains my second set of computer vision exercises under **Zgt Studio**.  
The goal is to work with individual pixels and regions of interest (ROIs):  
cropping, copying, tinting, drawing rectangles and creating borders.

---

## 1. Exercises

### 1.1 ROI Crop, Copy and Tint

Folder: `01_roi_crop_copy_tint/`

This example selects a rectangular region of interest (ROI) from the image,  
copies it to another location and then tints the original ROI with a solid color.

**Script:**

- `roi_crop_copy_tint.py`
  - reads `deer.jpg`,
  - selects a ROI using array slicing,
  - copies the ROI to a new position in the same image,
  - fills the original ROI with a solid BGR color.

**Data:**

- `deer.jpg` – sample image used for ROI operations.

---

### 1.2 Border Types (Reflect, Replicate, Wrap, Constant)

Folder: `02_border_types/`

This example creates different types of borders around the image using  
`cv2.copyMakeBorder`.

**Script:**

- `border_types.py`
  - reads `giraffe.jpg`,
  - creates reflected, replicated, wrapped and constant-color borders,
  - displays each result in a separate window.

**Data:**

- `giraffe.jpg` – sample image used to visualize border types.

---

### 1.3 Highlight ROI with a Rectangle

Folder: `03_rectangle_roi_highlight/`

This example highlights a region of interest by drawing a rectangle around it.

**Script:**

- `rectangle_roi_highlight.py`
  - reads `duck.jpg`,
  - draws a rectangle around a selected region,
  - displays the result.

**Data:**

- `duck.jpg` – sample image used to demonstrate rectangle drawing.

---

## 2. Project structure

```text
opencv-region-and-pixel-operations/
├─ 01_roi_crop_copy_tint/
│  ├─ deer.jpg
│  └─ roi_crop_copy_tint.py
├─ 02_border_types/
│  ├─ giraffe.jpg
│  └─ border_types.py
├─ 03_rectangle_roi_highlight/
│  ├─ duck.jpg
│  └─ rectangle_roi_highlight.py
└─ README.md
