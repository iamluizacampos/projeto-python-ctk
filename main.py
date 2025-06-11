#importação das bibliotecas
import customtkinter as ctk

#função para centralizar as telas
def centralizar(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

#função para validar login
def validar():
    usuario = usuarioe.get()
    senha = senhae.get()

#if para testar o login e abrir menu
    if usuario == "usuario" and senha == "123":
        resultado.configure(text="Login feito com sucesso!", text_color="green")

        #desabilitar a visualização da janela de login após validar o usuário
        login.withdraw()

        #criação da tela de menu
        menu = ctk.CTkToplevel(login)
        menu.geometry("650x450")
        menu.title("Tela de Menu")
        centralizar(menu, 650, 450)
        menu.configure(fg_color="#8bbf7a")

        #função do botão guia (menu)
        def guiamenu():

            #frames da aba guia
            cadframe = ctk.CTkFrame(menu, width=700, height=700, fg_color="#8bbf7a", )
            cadframe.place(x=100, y=70)

            guiamenuframe1 = ctk.CTkFrame(menu, width=340, height=160, corner_radius=22, fg_color="#fcfcf2")
            guiamenuframe1.place(x=100, y=85)

            guiamenuframe2 = ctk.CTkFrame(menu, width=160, height=160, corner_radius=22, fg_color="#c0f0b0")
            guiamenuframe2.place(x=460, y=85)

            guiamenuframe3 = ctk.CTkFrame(menu, width=160, height=160, corner_radius=22, fg_color="#dcf2d5")
            guiamenuframe3.place(x=100, y=272)

            guiamenuframe4 = ctk.CTkFrame(menu, width=160, height=160, corner_radius=22, fg_color="#dcf2d5")
            guiamenuframe4.place(x=280, y=272)

            guiamenuframe5 = ctk.CTkFrame(menu, width=160, height=160, corner_radius=22, fg_color="#dcf2d5")
            guiamenuframe5.place(x=460, y=272)

            #botões de icones da aba guia
            guiaicon = ctk.CTkButton(menu, text="⚙️", font=ctk.CTkFont(size=12), width=40, height=40, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=guiamenu)
            guiaicon.place(x=110, y=92)

            alunoicon = ctk.CTkButton(menu, text="✏️", font=ctk.CTkFont(size=12), width=40, height=40, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#dcf2d5", text_color="#fcfcf2", command=guiamenu)
            alunoicon.place(x=108, y=280)

            notasicon = ctk.CTkButton(menu, text="💯", font=ctk.CTkFont(size=16), width=40, height=40, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#dcf2d5", text_color="#fcfcf2", command=guiamenu)
            notasicon.place(x=288, y=280)

            consultaicon = ctk.CTkButton(menu, text="🔍", font=ctk.CTkFont(size=16), width=40, height=40, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#dcf2d5", text_color="#fcfcf2", command=guiamenu)
            consultaicon.place(x=468, y=280)

            sairicon = ctk.CTkButton(menu, text="🚪", font=ctk.CTkFont(size=16), width=40, height=40, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#c0f0b0", text_color="#fcfcf2", command=guiamenu)
            sairicon.place(x=470, y=92)

            #label titulo da aba guia
            tpguialabel = ctk.CTkLabel(menu, text="Guia Rápido", font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"), text_color="#fcfcf2")
            tpguialabel.place(x=100, y=32)

            #label explicando os botões 
            tguialabel = ctk.CTkLabel(menu, text="Guia Rápido", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), bg_color="#fcfcf2", text_color="#77a468")
            tguialabel.place(x=158, y=100)
            guialabel = ctk.CTkLabel(menu, text="Encontre aqui as informações essenciais para começar\n a usar o sistema de forma rápida e eficiente. Esta seção\n foi criada para oferecer um resumo prático das principais\n funcionalidades e etapas iniciais, ideal para novos\n usuários ou para quem precisa de uma consulta rápida.", bg_color="#fcfcf2", font=ctk.CTkFont(family="Arial", size=13), text_color="#56441D")
            guialabel.place(x=108, y=140)

            tsairlabel = ctk.CTkLabel(menu, text="Sair", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), bg_color="#c0f0b0", text_color="#77a468")
            tsairlabel.place(x=518, y=100)
            sairlabel = ctk.CTkLabel(menu, text="Use este botão para en-\ncerrar sua sessão e sair\n com segurança do sistema.", bg_color="#c0f0b0", font=ctk.CTkFont(family="Arial", size=13), text_color="#56441D")
            sairlabel.place(x=460, y=140)

            talunolabel = ctk.CTkLabel(menu, text="Aluno", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), bg_color="#dcf2d5", text_color="#77a468")
            talunolabel.place(x=158, y=290)
            alunolabel = ctk.CTkLabel(menu, text="Nesta aba, você pode re-\ngistrar novos alunos no sis-\ntema. Preencha as informa-\nções necessárias, como\n nome completo e outros\n dados importantes.", bg_color="#dcf2d5", font=ctk.CTkFont(family="Arial", size=13), text_color="#56441D")
            alunolabel.place(x=104, y=325)

            tnotaslabel = ctk.CTkLabel(menu, text="Notas", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), bg_color="#dcf2d5", text_color="#77a468")
            tnotaslabel.place(x=335, y=290)
            notaslabel = ctk.CTkLabel(menu, text="Nesta aba, você pode lan-\nçar e editar as notas dos\n alunos. Selecione a turma e\n o aluno desejado e in-\nforme as avaliações.", bg_color="#dcf2d5", font=ctk.CTkFont(family="Arial", size=13), text_color="#56441D")
            notaslabel.place(x=280, y=325)

            tconsultalabel = ctk.CTkLabel(menu, text="Consulta", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), bg_color="#dcf2d5", text_color="#77a468")
            tconsultalabel.place(x=518, y=290)
            consultalabel = ctk.CTkLabel(menu, text="Utilize esta aba para\n buscar e visualizar infor-\nmações já cadastradas no\n sistema. É possível fil-\ntrar dados por matrícula,\n facilitando o acesso rápido.", bg_color="#dcf2d5", font=ctk.CTkFont(family="Arial", size=13), text_color="#56441D")
            consultalabel.place(x=460, y=325)
        
        #função do botão de cadastro de alunos (menu)
        def cadastraaluno():
            #label com título da aba
            tpcadastrolabel = ctk.CTkLabel(menu, text="Cadastro        ", font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"), text_color="#fcfcf2")
            tpcadastrolabel.place(x=100, y=32)

            #frame da cor de fundo da aba
            cadframe = ctk.CTkFrame(menu, width=700, height=700, fg_color="#8bbf7a", )
            cadframe.place(x=100, y=70)

            #frames
            framenome = ctk.CTkFrame(menu, width=160, height=80, corner_radius=22, fg_color="#fcfcf2")
            framenome.place(x=130, y=132)

            framematricula = ctk.CTkFrame(menu, width=160, height=80, corner_radius=22, fg_color="#fcfcf2")
            framematricula.place(x=130, y=250)

            framesalva = ctk.CTkFrame(menu, width=80, height=50, corner_radius=15, fg_color="#fcfcf2")
            framesalva.place(x=500, y=132)

            framedeleta = ctk.CTkFrame(menu, width=80, height=50, corner_radius=15, fg_color="#fcfcf2")
            framedeleta.place(x=500, y=202)

            #label de campos de cadastro
            nomelabel = ctk.CTkLabel(menu, text="Nome:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
            nomelabel.place(x=145, y=138)

            matriculalabel = ctk.CTkLabel(menu, text="Matrícula:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
            matriculalabel.place(x=145, y=256)

            #campos para entrada de dados
            nomeentry = ctk.CTkEntry(menu, placeholder_text="Insira o Nome", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
            nomeentry.place(x=142, y=172)

            matriculaentry = ctk.CTkEntry(menu, placeholder_text="Insira a Matrícula", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
            matriculaentry.place(x=142, y=292)

            #botões
            salvarbt = ctk.CTkButton(menu, text="Salvar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2")
            salvarbt.place(x=510, y=145)

            apagarbt = ctk.CTkButton(menu, text="Deletar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2")
            apagarbt.place(x=508, y=216)

        #função para botão de notas (menu)
        def notas():

            #frames
            cadframe = ctk.CTkFrame(menu, width=700, height=700, fg_color="#8bbf7a", )
            cadframe.place(x=100, y=70)

            framematricula2 = ctk.CTkFrame(menu, width=160, height=80, corner_radius=22, fg_color="#fcfcf2")
            framematricula2.place(x=130, y=112)

            framedisciplina = ctk.CTkFrame(menu, width=160, height=80, corner_radius=22, fg_color="#fcfcf2")
            framedisciplina.place(x=130, y=230)

            framenota = ctk.CTkFrame(menu, width=160, height=80, corner_radius=22, fg_color="#fcfcf2")
            framenota.place(x=130, y=348)

            framesalva2 = ctk.CTkFrame(menu, width=80, height=50, corner_radius=15, fg_color="#fcfcf2")
            framesalva2.place(x=500, y=132)

            frameatualiza = ctk.CTkFrame(menu, width=80, height=50, corner_radius=15, fg_color="#fcfcf2")
            frameatualiza.place(x=500, y=202)

            frameapaga = ctk.CTkFrame(menu, width=80, height=50, corner_radius=15, fg_color="#fcfcf2")
            frameapaga.place(x=500, y=278)

            #label
            tpnotaslabel = ctk.CTkLabel(menu, text="Notas          ", font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"), text_color="#fcfcf2")
            tpnotaslabel.place(x=100, y=32)

            matriculalabel2 = ctk.CTkLabel(menu, text="Matrícula:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
            matriculalabel2.place(x=145, y=118)
            
            disciplinalabel = ctk.CTkLabel(menu, text="Disciplina:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
            disciplinalabel.place(x=145, y=236)
            
            notalabel = ctk.CTkLabel(menu, text="Notas:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
            notalabel.place(x=145, y=354)

            #campos para entrada de dados
            matriculaentry2 = ctk.CTkEntry(menu, placeholder_text="Insira a Matrícula", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
            matriculaentry2.place(x=142, y=155)

            disciplinaentry = ctk.CTkEntry(menu, placeholder_text="Insira a Disciplina", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
            disciplinaentry.place(x=142, y=275)

            notaentry = ctk.CTkEntry(menu, placeholder_text="Insira a Nota", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
            notaentry.place(x=142, y=390)

            #botões
            salvarbt = ctk.CTkButton(menu, text="Salvar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2")
            salvarbt.place(x=508, y=144)

            atualizarbt = ctk.CTkButton(menu, text="Atualizar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2")
            atualizarbt.place(x=502, y=214)

            deletarbt = ctk.CTkButton(menu, text="Apagar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2")
            deletarbt.place(x=506, y=290)

        #função para botão de consulta (menu)
        def consulta():
            #frames
            cadframe = ctk.CTkFrame(menu, width=700, height=700, fg_color="#8bbf7a", )
            cadframe.place(x=100, y=70)

            tpconsultalabel = ctk.CTkLabel(menu, text="Consulta      ", font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"), text_color="#fcfcf2")
            tpconsultalabel.place(x=100, y=32)

        #função que configura o botão de sair
        def sairmenu():
            login.deiconify()
            menu.withdraw()

        #frames para separar as informações do menu
        menubarframe = ctk.CTkFrame(menu, width=70, height=420, corner_radius=22, fg_color="#fcfcf2")
        menubarframe.place(x=15, y=14)

        #botões para cada aba do menu
        guiabt = ctk.CTkButton(menu, text="⚙️", font=ctk.CTkFont(size=15), width=45, height=45, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=guiamenu)
        guiabt.place(x=27, y=32)

        alunobt = ctk.CTkButton(menu, text="✏️", font=ctk.CTkFont(size=15), width=45, height=45, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=cadastraaluno)
        alunobt.place(x=27, y=132)

        notasbt = ctk.CTkButton(menu, text="💯", font=ctk.CTkFont(size=19), width=45, height=45, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=notas)
        notasbt.place(x=27, y=202)

        consultabt = ctk.CTkButton(menu, text="🔍", font=ctk.CTkFont(size=19), width=45, height=45, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=consulta)
        consultabt.place(x=27, y=272)

        sairbt = ctk.CTkButton(menu, text="🚪", font=ctk.CTkFont(size=19), width=45, height=45, hover_color="#b6dfaa", corner_radius=12,fg_color="#9fc294", border_color="#77a468", border_width=2, bg_color="#fcfcf2", text_color="#fcfcf2", command=sairmenu)
        sairbt.place(x=27, y=370)

        #labels para dividir botões
        divisao1 = ctk.CTkLabel(menu, text="________", text_color="#8bbf7a", bg_color="#fcfcf2", font=ctk.CTkFont(weight='bold'))
        divisao1.place(x=24, y=82)

        divisao2 = ctk.CTkLabel(menu, text="________", text_color="#8bbf7a", bg_color="#fcfcf2", font=ctk.CTkFont(weight='bold'))
        divisao2.place(x=24, y=326)

    else:
        resultado.configure(text="Usuário ou login incorretos!", text_color="red")    

#if para habilitar a visualização
def versenha():
    if mostrasenha.get():
        senhae.configure(show="")
    else:
        senhae.configure(show="*")

#criação da tela de login
login = ctk.CTk()
ctk.set_appearance_mode("light")
login.geometry("350x450")
centralizar(login, 350, 450)
login.title("Tela de Login")
login.configure(fg_color="#8bbf7a")

#inserindo campos para o login
#label de título
bvindo = ctk.CTkLabel(login, text="Log In", font=ctk.CTkFont(family="Helvetica", size=28, weight='bold'), text_color="#fcfcf2")
bvindo.place(x=135, y=16)

#frame para separar as informações
loginframe = ctk.CTkFrame(login, width=320, height=380, corner_radius=20, fg_color="#fcfcf2")
loginframe.place(x=15, y=60)

#usuário - entry e label
usuariol = ctk.CTkLabel(login, text="Usuário:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
usuariol.place(x=110, y=130)
usuarioe = ctk.CTkEntry(login, placeholder_text="Insira o Usuário", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
usuarioe.place(x=110, y=160)

#senha
senhal = ctk.CTkLabel(login, text="Senha:", font=ctk.CTkFont(family="Arial", size=14), text_color="#77a468", bg_color="#fcfcf2")
senhal.place(x=110, y=230)

#checkbox - habilitar visualização de senha
mostrasenha = ctk.BooleanVar()
senhackb = ctk.CTkCheckBox(login, text="", fg_color="#77a468", hover_color="#b6dfaa" ,corner_radius=20, border_color="#77a468",  variable=mostrasenha, command=versenha, bg_color="#fcfcf2")
senhackb.place(x=260, y=262)

#senha pt2
senhae = ctk.CTkEntry(login, placeholder_text="Insira a Senha", corner_radius=20, border_color="#77a468", fg_color="#cad7bb", placeholder_text_color="#fcfcf2", text_color="#77a468", height=30, bg_color="#fcfcf2")
senhae.place(x=110, y=260)

btabre = ctk.CTkButton(login, text="Entrar", font=ctk.CTkFont(family="Arial", size=12), hover_color="#b6dfaa", text_color="#fcfcf2", corner_radius=40, width=40, height=28, fg_color="#9fc294", border_color="#77a468", border_width=2, command=validar, bg_color="#fcfcf2")
btabre.place(x=150, y=330)

#resultado da validação de login
resultado = ctk.CTkLabel(login, text="", bg_color="#fcfcf2")
resultado.place(x=105, y=380)

#manter o programa aberto
login.mainloop()