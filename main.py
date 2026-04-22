import customtkinter as ctk
from database.db import criar_tabela
from ui.main_window import App
from ui.splash_screen import SplashScreen

if __name__ == "__main__":
    criar_tabela()

    root = App()
    root.withdraw()  # esconde a janela principal

    splash = SplashScreen(root)

    def abrir_app():
        if splash.winfo_exists():
            root.after(100, abrir_app)
        else:
            root.deiconify()  # mostra a janela principal

    root.after(100, abrir_app)
    root.mainloop()