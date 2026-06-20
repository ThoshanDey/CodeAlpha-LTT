import tkinter as tk
from tkinter import ttk, messagebox
import deepl
from gtts import gTTS
import os

API_KEY = "9307aba8-6fd4-4e3d-b8ac-f98504041526:fx"

translator = deepl.Translator(API_KEY)

languages = {
    "English": "EN",
    "French": "FR",
    "Spanish": "ES",
    "German": "DE",
    "Italian": "IT",
    "Japanese": "JA",
    "Korean": "KO",
    "Chinese": "ZH",
    "Hindi": "HI"
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    source_lang = languages[source_combo.get()]
    target_lang = languages[target_combo.get()]

    try:
        result = translator.translate_text(
            text,
            source_lang=source_lang,
            target_lang=target_lang
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Success", "Text copied to clipboard!")


def speak_text():
    translated = output_text.get("1.0", tk.END).strip()

    if not translated:
        messagebox.showwarning("Warning", "No translated text found.")
        return

    try:
        tts_langs = {
            "English": "en",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese": "zh-cn",
            "Hindi": "hi"
        }

        selected_language = target_combo.get()

        tts = gTTS(
            text=translated,
            lang=tts_langs[selected_language]
        )

        tts.save("speech.mp3")

        os.system("start speech.mp3")

    except Exception as e:
        messagebox.showerror("Speech Error", str(e))

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

tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 11)
).pack()

input_text = tk.Text(
    root,
    height=8,
    width=75
)
input_text.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(
    frame,
    text="Source Language"
).grid(row=0, column=0, padx=20)

source_combo = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
source_combo.grid(row=1, column=0)
source_combo.set("English")

tk.Label(
    frame,
    text="Target Language"
).grid(row=0, column=1, padx=20)

target_combo = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
target_combo.grid(row=1, column=1)
target_combo.set("French")

translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="lightblue",
    width=20
)
translate_btn.pack(pady=10)

tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 11)
).pack()

output_text = tk.Text(
    root,
    height=8,
    width=75
)
output_text.pack(pady=5)

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

root.mainloop()