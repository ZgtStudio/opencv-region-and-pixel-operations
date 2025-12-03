# OpenCV Region and Pixel Operations

This repository contains my second set of computer vision exercises under **Zgt Studio**.  
The goal is to work with individual pixels and regions of interest (ROIs):  
cropping, copying, tinting, drawing rectangles and creating borders.

---

## 1. Exercises

### 1.1 ROI Crop, Copy and Tint

Folder: `OpenCV Taking a Section from a Picture and Applying Effects/`

This example selects a rectangular region of interest (ROI) from the image,  
copies it to another location and then tints the original ROI with a solid color.

**Script:**

- `Taking_Section.py`
  - reads `deer.jpg`,
  - selects a ROI using array slicing,
  - copies the ROI to a new position in the same image,
  - fills the original ROI with a solid BGR color.

**Data:**

- `deer.jpg` – sample image used for ROI operations.

---

### 1.2 Border Types (Reflect, Replicate, Wrap, Constant)

Folder: `OpenCV Image Mirror Repeat Border/`

This example creates different types of borders around the image using  
`cv2.copyMakeBorder`.

**Script:**

- `Mirror_Repeat_Border.py`
  - reads `giraffe.jpg`,
  - creates reflected, replicated, wrapped and constant-color borders,
  - displays each result in a separate window.

**Data:**

- `giraffe.jpg` – sample image used to visualize border types.

---

### 1.3 Highlight ROI with a Rectangle

Folder: `OpenCV Rectangle Roi Highlights/`

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
├─ OpenCV Taking a Section from a Picture and Applying Effects/
│  ├─ deer.jpg
│  └─ Taking_Section.py
├─ OpenCV Image Mirror Repeat Border/
│  ├─ giraffe.jpg
│  └─ Mirror_Repeat_Border.py
├─ OpenCV Rectangle Roi Highlights/
│  ├─ duck.jpg
│  └─ rectangle_roi_highlight.py
└─ README.md
