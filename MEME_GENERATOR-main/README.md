# 🖼️ Meme Generator

A GUI-based Meme Generator built using Python, Tkinter, and Pillow (PIL). Add custom top and bottom text to any image with style, color, and font options.

---

## 🚀 Features

- Select any image from your computer
- Add top and bottom meme text
- Choose font, font size, and text color
- Background color support
- Supports `.png`, `.jpg`, `.jpeg` images
- Preview before saving
- Save meme in PNG or JPEG format

---

## 🛠️ Requirements

- Python 3.6+
- `Pillow` (PIL)
- `tkinter` (comes pre-installed with Python)

Install requirements:

```bash
pip install Pillow
```

---

## 📂 Project Structure

```
meme-generator/
│
├── meme_generator.py       # Main Python script
├── templates/              # Folder with base meme templates
│   ├── sample-template.png
│   └── another-template.jpg
├── output/                 # Folder for saved/generated memes
├── fonts/                  # Font files (e.g., Impact, Arial)
│   └── Impact.ttf
├── README.md               # Project documentation
```

---

## 🎨 How It Works

1. Launch the GUI.
2. Enter top and bottom text.
3. Choose font and text color.
4. Select an image.
5. Preview and save the meme!

---

📸 Screenshots
![meme1](https://github.com/user-attachments/assets/8a14af92-4160-463a-8fed-dd5c4de86e91)


![meme2](https://github.com/user-attachments/assets/52ca2c85-2b94-4e9e-a9b7-9494f531ebbe)


## 📘 License

MIT License

---

## 🙌 Credits

- GUI: Tkinter
- Image editing: Pillow
- Fonts: Google Fonts / system fonts

---

## 💡 Future Improvements

- Drag-and-drop image support
- Font preview dropdown
- Auto-save history
- Dark mode UI
