# GIF Creator

A simple Python project that creates GIFs from images.  
The user can either **choose pictures interactively** or let the script use a default set of images to generate an `excellent.gif`.

---

## Features
- Choose your own images (via file dialog).
- Automatic default GIF if no images are chosen.
- All frames are resized to the same dimensions automatically.
- Simple and lightweight – built with `imageio`, `Pillow`, and `numpy`.

---

## Usage

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/GIF-creator.git
cd GIF-creator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the script:
```bash
python create_gif.py
```
4. Choose option:
	Press 1 → select your own images (2 or more).
	Press 2 → script will use default files.
