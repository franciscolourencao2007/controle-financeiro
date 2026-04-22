import customtkinter as ctk

FUNDO  = "#1a1a2e"
CARD   = "#16213e"
BORDA  = "#0f3460"
TEXTO  = "#e0e0e0"
VERDE  = "#2ecc71"

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Configuração da janela
        largura, altura = 420, 280
        x = (self.winfo_screenwidth()  // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura  // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")
        self.overrideredirect(True)   # sem borda
        self.configure(fg_color=FUNDO)
        self.lift()
        self.attributes("-topmost", True)

        # Borda decorativa
        border = ctk.CTkFrame(self, fg_color=BORDA, corner_radius=16)
        border.place(relx=0, rely=0, relwidth=1, relheight=1)

        inner = ctk.CTkFrame(border, fg_color=FUNDO, corner_radius=14)
        inner.place(relx=0.008, rely=0.012, relwidth=0.984, relheight=0.976)

        # Ícone + título
        ctk.CTkLabel(
            inner, text="💳",
            font=("Segoe UI", 48)
        ).pack(pady=(35, 0))

        ctk.CTkLabel(
            inner, text="Controle Financeiro",
            font=("Segoe UI", 22, "bold"),
            text_color=TEXTO
        ).pack(pady=(8, 2))

        ctk.CTkLabel(
            inner, text="Carregando...",
            font=("Segoe UI", 11),
            text_color="#a0a0b0"
        ).pack()

        # Barra de progresso
        self.progress = ctk.CTkProgressBar(
            inner, width=300, height=8,
            fg_color=CARD, progress_color=VERDE,
            corner_radius=4
        )
        self.progress.set(0)
        self.progress.pack(pady=(20, 0))

        self._animar(0)

    def _animar(self, valor):
        if valor <= 1.0:
            self.progress.set(valor)
            self.after(18, self._animar, round(valor + 0.02, 2))
        else:
            self.destroy()