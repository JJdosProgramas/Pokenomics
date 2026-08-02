import customtkinter
from PIL import Image
import json
import webbrowser

customtkinter.set_appearance_mode("dark")

with open("Cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)["cards"]


app = customtkinter.CTk()
app.geometry("850x650")
app.title("Card Price")


pesquisa = customtkinter.StringVar()

entry = customtkinter.CTkEntry(
    app,
    textvariable=pesquisa,
    placeholder_text="Pesquisar Pokémon..."
)

entry.pack(
    fill="x",
    padx=20,
    pady=15
)


scroll = customtkinter.CTkScrollableFrame(app)
scroll.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


cards_frame = customtkinter.CTkFrame(
    scroll,
    fg_color="transparent"
)

cards_frame.pack(
    expand=True
)


imagens = []


def mostrar_cartas(filtro=""):

    global imagens

    imagens = []

    for widget in cards_frame.winfo_children():
        widget.destroy()


    cartas_filtradas = []

    for card in cards:
        if filtro.lower() in card["card"].lower():
            cartas_filtradas.append(card)


    coluna = 0
    linha = 0


    for card in cartas_filtradas:

        try:
            img = customtkinter.CTkImage(
                Image.open(card["img"]),
                size=(130, 190)
            )

        except:
            continue


        imagens.append(img)


        card_box = customtkinter.CTkFrame(
            cards_frame,
            width=150,
            height=250
        )

        card_box.grid(
            row=linha,
            column=coluna,
            padx=15,
            pady=15
        )


        imagem = customtkinter.CTkLabel(
            card_box,
            image=img,
            text="",
            cursor="hand2"
        )

        imagem.pack(
            padx=10,
            pady=10
        )


        imagem.bind(
            "<Button-1>",
            lambda e, url=card["link"]: webbrowser.open(url)
        )


        nome = customtkinter.CTkLabel(
            card_box,
            text=card["card"] + " " + card["number"],
            font=("Arial", 14),
            wraplength=130,
            cursor="hand2"
        )

        nome.pack(
            pady=5
        )


        nome.bind(
            "<Button-1>",
            lambda e, url=card["link"]: webbrowser.open(url)
        )


        coluna += 1

        if coluna == 4:
            coluna = 0
            linha += 1



def pesquisar(*args):
    mostrar_cartas(pesquisa.get())


pesquisa.trace_add(
    "write",
    pesquisar
)


mostrar_cartas()


app.mainloop()