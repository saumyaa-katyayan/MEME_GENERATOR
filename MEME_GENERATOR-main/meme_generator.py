from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk
import os

# Function to wrap text
def wrap_text(text, font, max_width, draw):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and draw.textbbox((0, 0), line + words[0], font=font)[2] <= max_width:
            line = f"{line} {words.pop(0)}".strip()
        lines.append(line)
    return lines

# Function to generate meme
def generate_meme(image_path, top_text, bottom_text, font_path, font_size, top_color, bottom_color, bg_color):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGBA")
        
        # Create a new image with background color
        meme_img = Image.new("RGBA", img.size, bg_color)
        meme_img.paste(img, (0, 0), img)

        draw = ImageDraw.Draw(meme_img)
        font = ImageFont.truetype(font_path, font_size)

        # Get image size
        image_width, image_height = meme_img.size

        # Wrap and add top text
        top_lines = wrap_text(top_text, font, image_width - 20, draw)
        y = 10
        for line in top_lines:
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            x = (image_width - text_width) / 2  # Center alignment
            draw.text((x, y), line, font=font, fill=top_color)
            y += text_bbox[3] - text_bbox[1]

        # Wrap and add bottom text
        bottom_lines = wrap_text(bottom_text, font, image_width - 20, draw)
        y = image_height - len(bottom_lines) * (text_bbox[3] - text_bbox[1]) - 10
        for line in bottom_lines:
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            x = (image_width - text_width) / 2  # Center alignment
            draw.text((x, y), line, font=font, fill=bottom_color)
            y += text_bbox[3] - text_bbox[1]

        # Preview before saving
        meme_img.show()

        # Ask for save location and format
        save_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if save_path:
            meme_img.save(save_path)
            messagebox.showinfo("Success", "Meme generated and saved successfully!")
        else:
            messagebox.showwarning("Canceled", "Save operation canceled.")
    
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", "Failed to generate meme. Ensure the image file or font is valid.")

# Function to open file dialog to select an image
def open_image():
    return filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

# Function to select a font
def select_font():
    return filedialog.askopenfilename(title="Select Font", filetypes=[("Font Files", "*.ttf;*.otf")])

# Function to choose a color
def choose_color():
    color_code = colorchooser.askcolor(title="Choose Text Color")
    return color_code[1] if color_code else "white"

# Function to trigger meme generation
def create_meme():
    top_text = top_text_entry.get()
    bottom_text = bottom_text_entry.get()
    font_size = int(font_size_entry.get())
    bg_color = bg_color_entry.get()
    
    image_path = open_image()
    if image_path:
        font_path = select_font() or "arial.ttf"  # Default to Arial if no font is chosen
        top_color = choose_color()
        bottom_color = choose_color()
        generate_meme(image_path, top_text, bottom_text, font_path, font_size, top_color, bottom_color, bg_color)

# Set up the Tkinter window
window = tk.Tk()
window.title("Advanced Meme Generator")

# Top Text Label and Entry
top_text_label = tk.Label(window, text="Top Text:")
top_text_label.pack()
top_text_entry = tk.Entry(window, width=50)
top_text_entry.pack()

# Bottom Text Label and Entry
bottom_text_label = tk.Label(window, text="Bottom Text:")
bottom_text_label.pack()
bottom_text_entry = tk.Entry(window, width=50)
bottom_text_entry.pack()

# Font Size Label and Entry
font_size_label = tk.Label(window, text="Font Size:")
font_size_label.pack()
font_size_entry = tk.Entry(window, width=10)
font_size_entry.insert(0, "40")  # Default font size
font_size_entry.pack()

# Background Color Label and Entry
bg_color_label = tk.Label(window, text="Background Color (e.g., '#ffffff'):")
bg_color_label.pack()
bg_color_entry = tk.Entry(window, width=20)
bg_color_entry.insert(0, "#000000")  # Default background color (black)
bg_color_entry.pack()

# Generate Meme Button
generate_button = tk.Button(window, text="Generate Meme", command=create_meme)
generate_button.pack()

# Start the Tkinter event loop
window.mainloop()
