# 🧠 Infoware Edu Prototype (PDF to Slides & Short Video)

**Goal:**
Convert an input PDF (e.g., one chapter or article) into:

* A short **slide deck** (`slides.pptx`) that visually explains key concepts
* A short **animated explainer video** (`video.mp4`, ~30–90s)

---

## 🎯 Project Overview

This prototype automates the conversion of educational PDFs into short visual explainers.
Given a single PDF input, the script:

1. Extracts and summarizes key sections
2. Builds a clean PowerPoint (or PDF) slide deck
3. Generates a short animated video with visuals and transitions

---

## 🧩 Key Deliverables

| Output                | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| `outputs/slides.pptx` | Auto-generated slide deck (6–12 slides). Each slide contains a title, 1–2 short points, and an image/visual. |
| `outputs/video.mp4`   | Short animated explainer video (30–90s), created from the slides.                                            |

---

## 🏗️ Functional Scope

### 1. PDF Ingestion & Text Extraction

* Reads PDF using `pdfplumber`.
* Falls back to **OCR via Tesseract** for image-based PDFs.
* Extracts headings, sections, and text content.

### 2. Content Summarization & Slide Text

* Automatically identifies 6–10 major sections.
* Produces short titles (6–20 words) and 1–2 bullets per slide.
* Generates speaker notes (or placeholder narration text).

### 3. Visual Generation

* Each slide includes:

  * A clean background and consistent layout
  * A text area for title and content
  * Optionally a generated or placeholder image

### 4. Slide Assembly

* Built using **`python-pptx`**
* Styled fonts, colors, and structure for clarity and consistency.

### 5. Video Generation

* Converts slides into an MP4 video using **MoviePy**
* Adds transitions, fade-ins, and smooth per-slide duration (3–5s)
* Background color & header bar mimic Canva-style layouts
* Optional music/narration support (extendable)

---

## ⚙️ Tech Stack

| Component              | Library                                  |
| ---------------------- | ---------------------------------------- |
| **Language**           | Python 3.9+                              |
| **PDF Parsing**        | `pdfplumber`, `pdf2image`, `pytesseract` |
| **Text Summarization** | Basic keyword + structure extraction     |
| **Slides Creation**    | `python-pptx`                            |
| **Video Assembly**     | `moviepy`, `PIL`                         |
| **TTS (optional)**     | `pyttsx3` or any cloud TTS (extendable)  |

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<itsmemauliii>/infooware-edu-prototype.git
cd infooware-edu-prototype
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add a PDF to the root directory

Example: `resume.pdf` or `sample_chapter.pdf`

### 4️⃣ Run the pipeline

```bash
python run_pipeline.py --input "resume.pdf" --outdir outputs
```

### 5️⃣ View your results

* 📑 `outputs/slides.pptx`
* 🎬 `outputs/video.mp4`

---

## 📂 Folder Structure

```
infooware-edu-prototype/
│
├── run_pipeline.py
├── sample.pdf
│
├── src/
│   ├── summarizer.py
│   ├── video_maker.py
│
├── outputs/
│   ├── slides.pptx
│   ├── video.mp4
│
└── README.md
```

---

## 📘 Example Workflow

| Step | Input        | Output                           |
| ---- | ------------ | -------------------------------- |
| 1    | `sample.pdf` | Extracted key text sections      |
| 2    | —            | `slides.pptx` generated          |
| 3    | —            | `video.mp4` (animated slideshow) |

Run example:

```bash
python run_pipeline.py --input "sample.pdf" --outdir outputs/
```

---

## 🧱 Architecture Overview

```text
PDF (Text or Image)
   │
   ├──> summarizer.py → Extracts & structures text
   │
   ├──> run_pipeline.py → Builds slides & triggers video
   │
   └──> video_maker.py → Renders visuals → MP4
```

---

## 💡 Future Enhancements

* Add automatic narration via Text-to-Speech (TTS)
* Integrate smooth zoom/pan animations (Ken Burns)
* Generate AI-based visuals (Stable Diffusion / DALL·E)
* Improve NLP-based keyphrase extraction

---

## 🧾 Credits

* Developed under **Infoware Edu Prototype Internship**
* Author: *Intern (Infoware R&D)*
* Guided by: *Infooware Edu AI Systems Team*
