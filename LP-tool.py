import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# -----------------------------
# Translate Function
# -----------------------------
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    source_lang = source_combo.get()
    target_lang = target_combo.get()

    try:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# Copy Function
# -----------------------------
def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Copied", "Text copied to clipboard!")


# -----------------------------
# Text To Speech Function
# -----------------------------
def speak_text():
    translated = output_text.get("1.0", tk.END).strip()

    if not translated:
        messagebox.showwarning("Warning", "Nothing to speak.")
        return

    try:
        tts = gTTS(text=translated, lang=languages[target_combo.get()])
        tts.save("speech.mp3")

        os.system("start speech.mp3")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# Supported Languages
# -----------------------------
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Hindi": "hi",
    "Bengali": "bn",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Korean": "ko",
    "Arabic": "ar"
}


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# -----------------------------
# Input Text
# -----------------------------
tk.Label(root, text="Enter Text:").pack()

input_text = tk.Text(root, height=8, width=70)
input_text.pack(pady=5)

# -----------------------------
# Language Selection
# -----------------------------
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Source Language").grid(row=0, column=0, padx=20)

source_combo = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
source_combo.grid(row=1, column=0)
source_combo.set("English")

tk.Label(frame, text="Target Language").grid(row=0, column=1, padx=20)

target_combo = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
target_combo.grid(row=1, column=1)
target_combo.set("Bengali")

# -----------------------------
# Translate Button
# -----------------------------
translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="lightblue",
    width=20
)
translate_btn.pack(pady=10)

# -----------------------------
# Output Text
# -----------------------------
tk.Label(root, text="Translated Text:").pack()

output_text = tk.Text(root, height=8, width=70)
output_text.pack(pady=5)

# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_btn = tk.Button(
    button_frame,
    text="Copy Text",
    command=copy_text,
    width=15
)
copy_btn.grid(row=0, column=0, padx=10)

speak_btn = tk.Button(
    button_frame,
    text="Text To Speech",
    command=speak_text,
    width=15
)
speak_btn.grid(row=0, column=1, padx=10)

# -----------------------------
# Run Program
# -----------------------------
root.mainloop()