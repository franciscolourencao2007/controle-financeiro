import customtkinter as ctk
from tkinter import messagebox, ttk
from datetime import datetime
from models.transacao import Transacao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

VERDE        = "#2ecc71"
VERDE_HOVER  = "#27ae60"
VERMELHO     = "#e74c3c"
VERMELHO_HOVER = "#c0392b"
FUNDO        = "#1a1a2e"
CARD         = "#16213e"
BORDA        = "#0f3460"
TEXTO        = "#e0e0e0"
TEXTO_FRACO  = "#a0a0b0"

DESCRICOES = [
    "Salário", "Freelance", "Bônus", "Rendimento",
    "Aluguel", "Condomínio", "IPTU",
    "Luz", "Água", "Gás", "Internet", "Telefone",
    "Supermercado", "Açougue", "Padaria",
    "Restaurante", "iFood / Delivery",
    "Transporte", "Combustível", "Estacionamento", "Uber / 99",
    "Cartão de Crédito", "Empréstimo", "Financiamento",
    "Plano de Saúde", "Farmácia", "Consulta Médica",
    "Educação", "Curso", "Livros",
    "Lazer", "Streaming", "Academia",
    "Roupas", "Calçados", "Eletrônicos",
    "Outros"
]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Controle Financeiro")
        self.geometry("1050x850")
        self.resizable(True, True)
        self.minsize(1000, 800)
        self.configure(fg_color=FUNDO)
        self.transacao_id = None
        self._build_header()
        self._build_cards()
        self._build_form()
        self._build_filtro()
        self._build_footer()   # ← footer ANTES da tabela
        self._build_table()    # ← tabela por último
        self.carregar_transacoes()
        self.atualizar_saldo()

    # ───────────────────────────── HEADER ─────────────────────────────
    def _build_header(self):
        frame = ctk.CTkFrame(self, fg_color=CARD, corner_radius=0, height=70)
        frame.pack(fill="x")
        frame.pack_propagate(False)

        ctk.CTkLabel(
            frame,
            text="💳  Controle Financeiro",
            font=("Segoe UI", 22, "bold"),
            text_color=TEXTO
        ).pack(side="left", padx=25, pady=15)

        self.data_label = ctk.CTkLabel(
            frame,
            text=datetime.now().strftime("%d/%m/%Y"),
            font=("Segoe UI", 13),
            text_color=TEXTO_FRACO
        )
        self.data_label.pack(side="right", padx=25)

    # ───────────────────────────── CARDS ─────────────────────────────
    def _build_cards(self):
        frame = ctk.CTkFrame(self, fg_color=FUNDO)
        frame.pack(fill="x", padx=20, pady=(15, 5))
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        self.card_saldo   = self._card(frame, "Saldo Atual", "R$ 0,00", "#3498db")
        self.card_entrada = self._card(frame, "Entradas",    "R$ 0,00", VERDE)
        self.card_saida   = self._card(frame, "Saídas",      "R$ 0,00", VERMELHO)

        self.card_saldo.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        self.card_entrada.grid(row=0, column=1, sticky="ew", padx=8)
        self.card_saida.grid(row=0, column=2, sticky="ew", padx=(8, 0))

    def _card(self, parent, titulo, valor, cor):
        frame = ctk.CTkFrame(parent, fg_color=CARD, corner_radius=12)
        ctk.CTkLabel(frame, text=titulo, font=("Segoe UI", 11), text_color=TEXTO_FRACO).pack(pady=(14, 2))
        lbl = ctk.CTkLabel(frame, text=valor, font=("Segoe UI", 22, "bold"), text_color=cor)
        lbl.pack(pady=(0, 14))
        frame._valor_label = lbl
        return frame

    # ───────────────────────────── FORMULÁRIO ─────────────────────────
    def _build_form(self):
        outer = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        outer.pack(fill="x", padx=20, pady=10)

        for i in range(5):
            outer.columnconfigure(i, weight=1)

        ctk.CTkLabel(
            outer, text="Nova Transação",
            font=("Segoe UI", 13, "bold"),
            text_color=TEXTO
        ).grid(row=0, column=0, columnspan=5, sticky="w", padx=15, pady=(12, 4))

        ctk.CTkLabel(outer, text="Descrição", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=0, padx=15, pady=(0, 2), sticky="w")
        self.descricao_entry = ctk.CTkComboBox(
            outer, values=DESCRICOES,
            fg_color="#0d1b2a", border_color=BORDA,
            button_color=BORDA, dropdown_fg_color=CARD,
            text_color=TEXTO
        )
        self.descricao_entry.set("Selecione ou digite")
        self.descricao_entry.grid(row=2, column=0, padx=15, pady=(0, 12), sticky="ew")

        ctk.CTkLabel(outer, text="Valor (R$)", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=1, padx=10, pady=(0, 2), sticky="w")
        self.valor_entry = ctk.CTkEntry(
            outer, placeholder_text="0,00",
            fg_color="#0d1b2a", border_color=BORDA, text_color=TEXTO
        )
        self.valor_entry.grid(row=2, column=1, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkLabel(outer, text="Tipo", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=2, padx=10, pady=(0, 2), sticky="w")
        self.tipo_option = ctk.CTkOptionMenu(
            outer, values=["Entrada", "Saída"],
            fg_color=BORDA, button_color="#0f3460",
            text_color=TEXTO, dropdown_fg_color=CARD
        )
        self.tipo_option.set("Entrada")
        self.tipo_option.grid(row=2, column=2, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkButton(
            outer, text="＋ Registrar",
            fg_color=VERDE, hover_color=VERDE_HOVER,
            font=("Segoe UI", 12, "bold"), text_color="white",
            command=self.registrar_transacao
        ).grid(row=2, column=3, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkButton(
            outer, text="✎ Atualizar",
            fg_color=BORDA, hover_color="#1a4a80",
            font=("Segoe UI", 12, "bold"), text_color=TEXTO,
            command=self.atualizar_transacao
        ).grid(row=2, column=4, padx=(0, 15), pady=(0, 12), sticky="ew")

    # ───────────────────────────── FILTRO ─────────────────────────────
    def _build_filtro(self):
        outer = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        outer.pack(fill="x", padx=20, pady=(0, 8))

        for i in range(5):
            outer.columnconfigure(i, weight=1)

        ctk.CTkLabel(
            outer, text="Filtrar Transações",
            font=("Segoe UI", 13, "bold"),
            text_color=TEXTO
        ).grid(row=0, column=0, columnspan=5, sticky="w", padx=15, pady=(12, 4))

        ctk.CTkLabel(outer, text="Data Inicial (dd/mm/aaaa)", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=0, padx=15, pady=(0, 2), sticky="w")
        self.data_ini_entry = ctk.CTkEntry(
            outer, placeholder_text="01/01/2024",
            fg_color="#0d1b2a", border_color=BORDA, text_color=TEXTO
        )
        self.data_ini_entry.grid(row=2, column=0, padx=15, pady=(0, 12), sticky="ew")

        ctk.CTkLabel(outer, text="Data Final (dd/mm/aaaa)", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=1, padx=10, pady=(0, 2), sticky="w")
        self.data_fim_entry = ctk.CTkEntry(
            outer, placeholder_text="31/12/2024",
            fg_color="#0d1b2a", border_color=BORDA, text_color=TEXTO
        )
        self.data_fim_entry.grid(row=2, column=1, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkLabel(outer, text="Tipo", font=("Segoe UI", 11), text_color=TEXTO_FRACO)\
            .grid(row=1, column=2, padx=10, pady=(0, 2), sticky="w")
        self.filtro_tipo = ctk.CTkOptionMenu(
            outer, values=["Todos", "Entrada", "Saída"],
            fg_color=BORDA, button_color="#0f3460",
            text_color=TEXTO, dropdown_fg_color=CARD
        )
        self.filtro_tipo.set("Todos")
        self.filtro_tipo.grid(row=2, column=2, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkButton(
            outer, text="🔍  Filtrar",
            fg_color="#3498db", hover_color="#2176ae",
            font=("Segoe UI", 12, "bold"), text_color="white",
            command=self.aplicar_filtro
        ).grid(row=2, column=3, padx=10, pady=(0, 12), sticky="ew")

        ctk.CTkButton(
            outer, text="✕  Limpar Filtro",
            fg_color=BORDA, hover_color="#1a4a80",
            font=("Segoe UI", 12, "bold"), text_color=TEXTO,
            command=self.limpar_filtro
        ).grid(row=2, column=4, padx=(0, 15), pady=(0, 12), sticky="ew")

    # ───────────────────────────── FOOTER ─────────────────────────────
    def _build_footer(self):
        frame = ctk.CTkFrame(self, fg_color=CARD, corner_radius=0, height=52)
        frame.pack(fill="x", side="bottom")
        frame.pack_propagate(False)

        ctk.CTkButton(
            frame, text="🗑  Excluir Selecionado", width=200,
            fg_color=VERMELHO, hover_color=VERMELHO_HOVER,
            font=("Segoe UI", 12, "bold"), text_color="white",
            command=self.excluir_transacao
        ).pack(side="right", padx=(10, 20), pady=10)

        ctk.CTkButton(
            frame, text="🧹  Limpar Histórico", width=200,
            fg_color="#7f3f3f", hover_color="#6b2f2f",
            font=("Segoe UI", 12, "bold"), text_color="white",
            command=self.limpar_historico
        ).pack(side="right", padx=10, pady=10)

        ctk.CTkLabel(
            frame, text="Selecione uma linha para editar",
            font=("Segoe UI", 11), text_color=TEXTO_FRACO
        ).pack(side="left", padx=20)

    # ───────────────────────────── TABELA ─────────────────────────────
    def _build_table(self):
        outer = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        outer.pack(fill="both", expand=True, padx=20, pady=(0, 8))

        ctk.CTkLabel(
            outer, text="Histórico de Transações",
            font=("Segoe UI", 13, "bold"),
            text_color=TEXTO
        ).pack(anchor="w", padx=15, pady=(12, 6))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
            background=CARD, foreground=TEXTO,
            fieldbackground=CARD, rowheight=34,
            font=("Segoe UI", 11), borderwidth=0
        )
        style.configure("Custom.Treeview.Heading",
            background=BORDA, foreground=TEXTO,
            font=("Segoe UI", 11, "bold"), relief="flat"
        )
        style.map("Custom.Treeview",
            background=[("selected", "#1a4a80")],
            foreground=[("selected", "white")]
        )

        colunas = ("ID", "Descrição", "Valor", "Tipo", "Data")
        self.tree = ttk.Treeview(
            outer, columns=colunas, show="headings",
            style="Custom.Treeview", selectmode="browse"
        )

        self.tree.column("ID",        anchor="center", width=60,  minwidth=50,  stretch=False)
        self.tree.column("Descrição", anchor="center", width=300, minwidth=200, stretch=True)
        self.tree.column("Valor",     anchor="center", width=150, minwidth=120, stretch=True)
        self.tree.column("Tipo",      anchor="center", width=120, minwidth=80,  stretch=False)
        self.tree.column("Data",      anchor="center", width=120, minwidth=100, stretch=False)

        for col in colunas:
            self.tree.heading(col, text=col)

        scroll = ttk.Scrollbar(outer, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=(0, 10))
        scroll.pack(side="right", fill="y", padx=(0, 5), pady=(0, 10))

        self.tree.bind("<<TreeviewSelect>>", self.selecionar_transacao)
        self.tree.tag_configure("entrada", foreground=VERDE)
        self.tree.tag_configure("saida",   foreground=VERMELHO)

    # ───────────────────────────── LÓGICA ─────────────────────────────
    def registrar_transacao(self):
        descricao = self.descricao_entry.get().strip()
        valor_texto = self.valor_entry.get().strip()
        tipo = self.tipo_option.get()
        data = datetime.now().strftime("%d/%m/%Y")

        if not descricao or descricao == "Selecione ou digite" or not valor_texto:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        try:
            valor = float(valor_texto.replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Use vírgula ou ponto.")
            return

        Transacao(descricao, valor, tipo, data).salvar()
        self.limpar_campos()
        self.carregar_transacoes()
        self.atualizar_saldo()

    def selecionar_transacao(self, event):
        selecionado = self.tree.selection()
        if not selecionado:
            return
        valores = self.tree.item(selecionado)["values"]
        self.transacao_id = valores[0]
        self.descricao_entry.set(valores[1])
        valor = str(valores[2]).replace("R$", "").replace(".", "").replace(",", ".").strip()
        self.valor_entry.delete(0, "end")
        self.valor_entry.insert(0, valor)
        self.tipo_option.set(valores[3])

    def atualizar_transacao(self):
        if self.transacao_id is None:
            messagebox.showwarning("Aviso", "Selecione uma transação na tabela.")
            return
        descricao = self.descricao_entry.get().strip()
        valor_texto = self.valor_entry.get().strip()
        tipo = self.tipo_option.get()
        try:
            valor = float(valor_texto.replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")
            return
        Transacao.atualizar(self.transacao_id, descricao, valor, tipo)
        self.limpar_campos()
        self.carregar_transacoes()
        self.atualizar_saldo()

    def excluir_transacao(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma transação.")
            return
        transacao_id = self.tree.item(selecionado)["values"][0]
        if messagebox.askyesno("Confirmar exclusão", "Deseja excluir esta transação?"):
            Transacao.excluir(transacao_id)
            self.limpar_campos()
            self.carregar_transacoes()
            self.atualizar_saldo()

    def limpar_historico(self):
        if messagebox.askyesno(
            "Confirmar",
            "Tem certeza que deseja apagar TODAS as transações?\nEssa ação não pode ser desfeita."
        ):
            import sqlite3
            conn = sqlite3.connect("finance.db")
            conn.execute("DELETE FROM transacoes")
            conn.commit()
            conn.close()
            self.limpar_campos()
            self.carregar_transacoes()
            self.atualizar_saldo()
            messagebox.showinfo("Concluído", "Histórico apagado com sucesso!")

    def aplicar_filtro(self):
        data_ini = self.data_ini_entry.get().strip()
        data_fim = self.data_fim_entry.get().strip()
        tipo     = self.filtro_tipo.get()

        fmt = "%d/%m/%Y"
        try:
            di = datetime.strptime(data_ini, fmt) if data_ini else None
            df = datetime.strptime(data_fim, fmt) if data_fim else None
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. Use o formato dd/mm/aaaa.")
            return

        registros = Transacao.listar()
        filtrados = []
        for reg in registros:
            try:
                data_reg = datetime.strptime(reg[4], fmt)
            except ValueError:
                continue
            if di and data_reg < di:
                continue
            if df and data_reg > df:
                continue
            if tipo != "Todos" and reg[3] != tipo:
                continue
            filtrados.append(reg)

        self._preencher_tabela(filtrados)

    def limpar_filtro(self):
        self.data_ini_entry.delete(0, "end")
        self.data_fim_entry.delete(0, "end")
        self.filtro_tipo.set("Todos")
        self.carregar_transacoes()

    def carregar_transacoes(self):
        self._preencher_tabela(Transacao.listar())

    def _preencher_tabela(self, registros):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for reg in registros:
            valor_fmt = f"R$ {reg[2]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            tag = "entrada" if reg[3] == "Entrada" else "saida"
            self.tree.insert("", "end", values=(reg[0], reg[1], valor_fmt, reg[3], reg[4]), tags=(tag,))

    def atualizar_saldo(self):
        import sqlite3
        conn = sqlite3.connect("finance.db")
        cur = conn.cursor()

        cur.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Entrada'")
        entradas = cur.fetchone()[0] or 0.0

        cur.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Saída'")
        saidas = cur.fetchone()[0] or 0.0

        conn.close()
        saldo = entradas - saidas

        def fmt(v):
            return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        self.card_saldo._valor_label.configure(
            text=fmt(saldo),
            text_color="#3498db" if saldo >= 0 else VERMELHO
        )
        self.card_entrada._valor_label.configure(text=fmt(entradas))
        self.card_saida._valor_label.configure(text=fmt(saidas))

    def limpar_campos(self):
        self.transacao_id = None
        self.descricao_entry.set("Selecione ou digite")
        self.valor_entry.delete(0, "end")
        self.tipo_option.set("Entrada")
        