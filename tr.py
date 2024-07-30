import tkinter as tk
from googletrans import Translator, LANGUAGES

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.translator = Translator()

        self.src_lang_label = tk.Label(root, text="Source Language:")
        self.src_lang_label.pack()
        self.src_lang_var = tk.StringVar()
        self.src_lang_menu = tk.OptionMenu(root, self.src_lang_var, *LANGUAGES.keys())
        self.src_lang_menu.pack()

        self.src_text_label = tk.Label(root, text="Source Text:")
        self.src_text_label.pack()
        self.src_text_entry = tk.Text(root, height=10, width=40)
        self.src_text_entry.pack()

        self.dst_lang_label = tk.Label(root, text="Destination Language:")
        self.dst_lang_label.pack()
        self.dst_lang_var = tk.StringVar()
        self.dst_lang_menu = tk.OptionMenu(root, self.dst_lang_var, *LANGUAGES.keys())
        self.dst_lang_menu.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack()

        self.dst_text_label = tk.Label(root, text="Translated Text:")
        self.dst_text_label.pack()
        self.dst_text_entry = tk.Text(root, height=10, width=40)
        self.dst_text_entry.pack()

    def translate(self):
        src_text = self.src_text_entry.get("1.0", "end-1c")
        src_lang = self.src_lang_var.get()
        dst_lang = self.dst_lang_var.get()

        try:
            result = self.translator.translate(src_text, src=src_lang, dest=dst_lang)
            self.dst_text_entry.delete("1.0", "end")
            self.dst_text_entry.insert("1.0", result.text)
        except ValueError as e:
            self.dst_text_entry.delete("1.0", "end")
            self.dst_text_entry.insert("1.0", str(e))

root = tk.Tk()
app = LanguageTranslator(root)
root.mainloop()