
import os
import webbrowser
import tkinter as tk
from datetime import datetime

BG = "#071426"
PANEL = "#0d213b"
BLUE = "#168cff"
TEXT = "#eaf4ff"
MUTED = "#8da9c7"


class Jarvis:
    def __init__(self, root):
        self.root = root
        root.title("JARVIS AI Assistant")
        root.geometry("900x620")
        root.minsize(700, 500)
        root.configure(bg=BG)

        tk.Label(
            root, text="J.A.R.V.I.S",
            bg=BG, fg=BLUE,
            font=("Segoe UI", 30, "bold")
        ).pack(anchor="w", padx=30, pady=(25, 0))

        tk.Label(
            root, text="PERSONAL AI DESKTOP ASSISTANT",
            bg=BG, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=32)

        status = tk.Frame(root, bg=PANEL, padx=18, pady=15)
        status.pack(fill="x", padx=30, pady=25)

        tk.Label(
            status, text="● SYSTEM ONLINE",
            bg=PANEL, fg="#45e6a5",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        tk.Label(
            root, text="WHAT CAN I DO FOR YOU?",
            bg=BG, fg=TEXT,
            font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", padx=32)

        self.command = tk.Entry(
            root, bg=PANEL, fg=TEXT,
            insertbackground=TEXT,
            relief="flat", font=("Segoe UI", 14)
        )
        self.command.pack(fill="x", padx=30, pady=12, ipady=14)
        self.command.bind("<Return>", lambda event: self.execute())

        tk.Button(
            root, text="EXECUTE COMMAND",
            command=self.execute,
            bg=BLUE, fg="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=20, pady=12
        ).pack(anchor="w", padx=30)

        tk.Label(
            root, text="JARVIS ACTIVITY LOG",
            bg=BG, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=32, pady=(25, 8))

        self.log = tk.Text(
            root, bg=PANEL, fg=TEXT,
            relief="flat", font=("Consolas", 10),
            height=12, state="disabled"
        )
        self.log.pack(fill="both", expand=True, padx=30, pady=(0, 25))

        self.write_log("JARVIS initialized. Type help to see commands.")

    def write_log(self, message):
        self.log.configure(state="normal")
        self.log.insert(
            "end",
            f"[{datetime.now():%H:%M:%S}] {message}\n"
        )
        self.log.see("end")
        self.log.configure(state="disabled")

    def execute(self):
        command = self.command.get().strip()
        if not command:
            return

        self.write_log("YOU: " + command)
        self.command.delete(0, "end")
        c = command.lower()

        if c in ["hello", "hi", "hey jarvis"]:
            answer = "Hello! JARVIS is online and ready."

        elif c == "help":
            answer = (
                "Commands: hello, time, date, "
                "open notepad, open calculator, "
                "open explorer, open browser, "
                "search <topic>, exit."
            )

        elif c == "time":
            answer = datetime.now().strftime(
                "The time is %I:%M %p."
            )

        elif c == "date":
            answer = datetime.now().strftime(
                "Today is %A, %d %B %Y."
            )

        elif c == "open notepad":
            os.system("start notepad")
            answer = "Opening Notepad."

        elif c == "open calculator":
            os.system("start calc")
            answer = "Opening Calculator."

        elif c in ["open explorer", "open file explorer"]:
            os.startfile(os.path.expanduser("~"))
            answer = "Opening File Explorer."

        elif c in ["open browser", "open google"]:
            webbrowser.open("https://www.google.com")
            answer = "Opening your browser."

        elif c.startswith("search "):
            query = command[7:].strip()
            webbrowser.open(
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )
            answer = "Searching for " + query

        elif c in ["exit", "quit"]:
            self.root.destroy()
            return

        else:
            answer = "Command not recognized. Type help."

        self.write_log("JARVIS: " + answer)


if __name__ == "__main__":
    root = tk.Tk()
    app = Jarvis(root)
    root.mainloop()
