import time
import tkinter as tk
from tkinter import messagebox

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест скорости набора текста")

        self.prompt_label = tk.Label(root, text="Введите текст:")
        self.prompt_label.pack()

        self.text_entry = tk.Text(root, height=10, width=50)
        self.text_entry.pack()

        self.start_button = tk.Button(root, text="Начать тест", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.start_time = time.time()
        self.text_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.text_entry.bind("<Key>", self.check_completion)

    def check_completion(self, event):
        typed_text = self.text_entry.get("1.0", tk.END)
        if len(typed_text.split()) >= 30:  # Остановить тест после ввода 30 слов
            self.end_time = time.time()
            self.calculate_speed()

    def calculate_speed(self):
        typed_text = self.text_entry.get("1.0", tk.END)
        typed_words = typed_text.split()
        elapsed_time = self.end_time - self.start_time
        words_per_minute = len(typed_words) / (elapsed_time / 60)
        accuracy = self.calculate_accuracy(typed_words)

        messagebox.showinfo("Результаты теста",
                            f"Скорость набора: {words_per_minute:.2f} слов в минуту\n"
                            f"Точность: {accuracy:.2f}%\n"
                            f"Количество набранных слов: {len(typed_words)}")

    def calculate_accuracy(self, typed_words):
        original_text = ""
        original_words = original_text.split()
        correct_count = sum(1 for typed, original in zip(typed_words, original_words) if typed == original)
        accuracy = (correct_count / len(original_words)) * 100
        return accuracy

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()