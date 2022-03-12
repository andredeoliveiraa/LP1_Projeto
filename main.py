from tkinter import *
import time

#----Funções de interface gráfica


# def cadastro_de_notas2():
#     if bt_cadastar:
#
#         n1 = int(ap1.get())
#         n2 = int(ap2.get())
#         n3 = int(ap3.get())
#         mf = (n1 + n2 + n3)/3
#         mediafinal["text"] = ("%.2f" % mf)
#         #print("%.2f" % mf)
#         if mf >= 6:
#             print('Aprovado')
#             legendastatus["text"] = 'Aprovado'
#
#         else:
#             print('Reprovado')
#             legendastatus["text"] = 'Reprovado'

def visualizar_nota_fisica():

    # janela para visualizar as notas

    janela_notas354 = Tk()
    janela_notas354.title("ECA - Notas")
    janela_notas354.geometry("490x560+610+153")
    janela_notas354.resizable(width=0, height=0)
    janela_notas354['bg'] = '#2d8659'

    # ---área do titulo

    titulo_geral935 = Label(janela_notas354, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659', fg='white')
    titulo_geral935.place(width=150, height=45, x=170, y=50)

    # informações básicas do aluno

    titulo_aluno354 = Label(janela_notas354, text='Alexander Sweney De Franca Souza', font=("Calibri", 15), bg='#194d33',
                           fg='white')
    titulo_aluno354.place(width=400, height=45, x=50, y=120)

    # legenda das notas

    legendanota354 = Label(janela_notas354, text='Física I', font=("Calibri bold", 13), bg='#194d33',
                          fg='white')
    legendanota354.place(width=200, height=40, x=140, y=190)
    legendastatus354 = Label(janela_notas354, text='Reprovado', font=("Calibri", 15), bg='#194d33', fg='white')
    legendastatus354.place(width=100, height=45, x=300, y=290)

    # legenda final da pagina
    legendanota2354 = Label(janela_notas354, text='Abreviações', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota2354.place(width=180, height=30, x=150, y=400)
    legendanota3354 = Label(janela_notas354, text='AP - Avaliação Parcial', font=("Calibri", 13), bg='#194d33',
                           fg='white')
    legendanota3354.place(width=180, height=30, x=150, y=430)
    legendanota4354 = Label(janela_notas354, text='MF - Média Final', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota4354.place(width=180, height=30, x=150, y=460)

    # legenda das AP's
    legenda1354 = Label(janela_notas354, text='AP1', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda1354.place(width=45, height=45, x=100, y=240)
    legenda2354 = Label(janela_notas354, text='AP2', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda2354.place(width=45, height=45, x=150, y=240)
    legenda3354 = Label(janela_notas354, text='AP3', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda3354.place(width=45, height=45, x=200, y=240)
    legenda4354 = Label(janela_notas354, text='MF', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda4354.place(width=45, height=45, x=250, y=240)

    # ---área de input de notas

    ap13354 = Label(janela_notas354, bd=0, text='7', font=("Calibri", 15), justify=CENTER)
    ap13354.place(width=45, height=45, x=100, y=290)
    ap23354 = Label(janela_notas354, bd=0, text='4',font=("Calibri", 15), justify=CENTER)
    ap23354.place(width=45, height=45, x=150, y=290)
    ap33354 = Label(janela_notas354, bd=0,text='6', font=("Calibri", 15), justify=CENTER)
    ap33354.place(width=45, height=45, x=200, y=290)
    mediafinal3354 = Label(janela_notas354, bd=0,text='5.66', font=("Calibri", 15), justify=CENTER)
    mediafinal3354.place(width=45, height=45, x=250, y=290)

def visualizar_nota_calculo():
    # janela para visualizar as notas

    global n11, n22, n33, statuss5

    janela_notas35 = Tk()
    janela_notas35.title("ECA - Notas")
    janela_notas35.geometry("490x560+610+153")
    janela_notas35.resizable(width=0, height=0)
    janela_notas35['bg'] = '#2d8659'

    # ---área do titulo

    titulo_geral935 = Label(janela_notas35, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659', fg='white')
    titulo_geral935.place(width=150, height=45, x=170, y=50)

    # informações básicas do aluno

    titulo_aluno35 = Label(janela_notas35, text='Alexander Sweney De Franca Souza', font=("Calibri", 15), bg='#194d33',
                          fg='white')
    titulo_aluno35.place(width=400, height=45, x=50, y=120)

    # legenda das notas

    legendanota35 = Label(janela_notas35, text='Cálculo I', font=("Calibri bold", 13), bg='#194d33',
                         fg='white')
    legendanota35.place(width=200, height=40, x=140, y=190)
    legendastatus35 = Label(janela_notas35, text='', font=("Calibri", 15), bg='#194d33', fg='white')
    legendastatus35.place(width=100, height=45, x=300, y=290)

    # legenda final da pagina
    legendanota235 = Label(janela_notas35, text='Abreviações', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota235.place(width=180, height=30, x=150, y=400)
    legendanota335 = Label(janela_notas35, text='AP - Avaliação Parcial', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota335.place(width=180, height=30, x=150, y=430)
    legendanota435 = Label(janela_notas35, text='MF - Média Final', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota435.place(width=180, height=30, x=150, y=460)

    # legenda das AP's
    legenda135 = Label(janela_notas35, text='AP1', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda135.place(width=45, height=45, x=100, y=240)
    legenda235 = Label(janela_notas35, text='AP2', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda235.place(width=45, height=45, x=150, y=240)
    legenda335 = Label(janela_notas35, text='AP3', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda335.place(width=45, height=45, x=200, y=240)
    legenda435 = Label(janela_notas35, text='MF', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda435.place(width=45, height=45, x=250, y=240)

    # ---área de input de notas

    ap1335 = Label(janela_notas35, bd=0, font=("Calibri", 15), justify=CENTER)
    ap1335.place(width=45, height=45, x=100, y=290)
    ap2335 = Label(janela_notas35, bd=0, font=("Calibri", 15), justify=CENTER)
    ap2335.place(width=45, height=45, x=150, y=290)
    ap3335 = Label(janela_notas35, bd=0, font=("Calibri", 15), justify=CENTER)
    ap3335.place(width=45, height=45, x=200, y=290)
    mediafinal335 = Label(janela_notas35, bd=0, font=("Calibri", 15), justify=CENTER)
    mediafinal335.place(width=45, height=45, x=250, y=290)

    ap1335['text'] = '10'
    ap2335['text'] = n22
    ap3335['text'] = n33
    mediafinal335['text'] = mf111
    legendastatus35['text'] = statuss1

def nota_calculo():

    global ap15, ap25, ap35, mediafinal51, legendastatus5

    janela_notas5 = Tk()
    janela_notas5.title("ECA - Notas")
    janela_notas5.geometry("490x560+610+153")
    janela_notas5.resizable(width=0, height=0)
    janela_notas5['bg'] = '#2d8659'

    # ---área do titulo

    titulo_geral95 = Label(janela_notas5, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659', fg='white')
    titulo_geral95.place(width=150, height=45, x=170, y=50)

    # informações básicas do aluno

    titulo_aluno5 = Label(janela_notas5, text='Alexander Sweney De Franca Souza', font=("Calibri", 15), bg='#194d33',fg='white')
    titulo_aluno5.place(width=400, height=45, x=50, y=120)

    # legenda das notas

    legendanota5 = Label(janela_notas5, text='Cálculo I', font=("Calibri bold", 13), bg='#194d33',fg='white')
    legendanota5.place(width=200, height=40, x=140, y=190)
    legendastatus5 = Label(janela_notas5, text='', font=("Calibri", 15), bg='#194d33', fg='white')
    legendastatus5.place(width=100, height=45, x=300, y=290)

    # legenda final da pagina
    legendanota25 = Label(janela_notas5, text='Abreviações', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota25.place(width=180, height=30, x=10, y=400)
    legendanota35 = Label(janela_notas5, text='AP - Avaliação Parcial', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota35.place(width=180, height=30, x=10, y=430)
    legendanota45 = Label(janela_notas5, text='MF - Média Final', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota45.place(width=180, height=30, x=10, y=460)

    # legenda das AP's
    legenda15 = Label(janela_notas5, text='AP1', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda15.place(width=45, height=45, x=100, y=240)
    legenda25 = Label(janela_notas5, text='AP2', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda25.place(width=45, height=45, x=150, y=240)
    legenda35 = Label(janela_notas5, text='AP3', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda35.place(width=45, height=45, x=200, y=240)
    legenda45 = Label(janela_notas5, text='MF', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda45.place(width=45, height=45, x=250, y=240)

    # ---área de input de notas

    ap15 = Label(janela_notas5, bd=0, text='10', font=("Calibri", 15), justify=CENTER)
    ap15.place(width=45, height=45, x=100, y=290)
    ap25 = Entry(janela_notas5, bd=0, font=("Calibri", 15), justify=CENTER)
    ap25.place(width=45, height=45, x=150, y=290)
    ap35 = Entry(janela_notas5, bd=0, font=("Calibri", 15), justify=CENTER)
    ap35.place(width=45, height=45, x=200, y=290)
    mediafinal51 = Label(janela_notas5, bd=0, font=("Calibri", 15), justify=CENTER)
    mediafinal51.place(width=45, height=45, x=250, y=290)

    # ---a partir daqui tudo pode estar errado

    # Criação de botão para inserir a nota

    bt_cadastar5 = Button(janela_notas5, text='Cadastrar', font=("Calibri", 15), bg='#26734d', justify=CENTER, fg='white',command=calculadora_de_notas2)
    bt_cadastar5.place(width=100, height=45, x=350, y=460)

def janela_de_visualizacao():

    #janela para visualizar as notas

    global n1, n2, n3, statuss

    janela_notas3 = Tk()
    janela_notas3.title("ECA - Notas")
    janela_notas3.geometry("490x560+610+153")
    janela_notas3.resizable(width=0, height=0)
    janela_notas3['bg'] = '#2d8659'

    # ---área do titulo

    titulo_geral93 = Label(janela_notas3, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659', fg='white')
    titulo_geral93.place(width=150, height=45, x=170, y=50)

    # informações básicas do aluno

    titulo_aluno3 = Label(janela_notas3, text='Alexander Sweney De Franca Souza', font=("Calibri", 15), bg='#194d33',
                         fg='white')
    titulo_aluno3.place(width=400, height=45, x=50, y=120)

    # legenda das notas

    legendanota3 = Label(janela_notas3, text='Comunicação e expressão', font=("Calibri bold", 13), bg='#194d33',fg='white')
    legendanota3.place(width=200, height=40, x=140, y=190)
    legendastatus3 = Label(janela_notas3, text='', font=("Calibri", 15), bg='#194d33', fg='white')
    legendastatus3.place(width=100, height=45, x=300, y=290)

    # legenda final da pagina
    legendanota23 = Label(janela_notas3, text='Abreviações', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota23.place(width=180, height=30, x=150, y=400)
    legendanota33 = Label(janela_notas3, text='AP - Avaliação Parcial', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota33.place(width=180, height=30, x=150, y=430)
    legendanota43 = Label(janela_notas3, text='MF - Média Final', font=("Calibri", 13), bg='#194d33', fg='white')
    legendanota43.place(width=180, height=30, x=150, y=460)

    # legenda das AP's
    legenda13 = Label(janela_notas3, text='AP1', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda13.place(width=45, height=45, x=100, y=240)
    legenda23 = Label(janela_notas3, text='AP2', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda23.place(width=45, height=45, x=150, y=240)
    legenda33 = Label(janela_notas3, text='AP3', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda33.place(width=45, height=45, x=200, y=240)
    legenda43 = Label(janela_notas3, text='MF', font=("Calibri", 15), bg='#2d8659', fg='white')
    legenda43.place(width=45, height=45, x=250, y=240)

    # ---área de input de notas

    ap133 = Label(janela_notas3, bd=0, font=("Calibri", 15), justify=CENTER)
    ap133.place(width=45, height=45, x=100, y=290)
    ap233 = Label(janela_notas3, bd=0, font=("Calibri", 15), justify=CENTER)
    ap233.place(width=45, height=45, x=150, y=290)
    ap333 = Label(janela_notas3, bd=0, font=("Calibri", 15), justify=CENTER)
    ap333.place(width=45, height=45, x=200, y=290)
    mediafinal33 = Label(janela_notas3, bd=0, font=("Calibri", 15), justify=CENTER)
    mediafinal33.place(width=45, height=45, x=250, y=290)

    ap133['text'] = n1
    ap233['text'] = n2
    ap333['text'] = n3
    mediafinal33['text'] = mf11
    legendastatus3['text'] = statuss


    # ---a partir daqui tudo pode estar errado

def janela_de_escolha_de_visualizacao_de_notas():

    janela_grade23 = Tk()
    janela_grade23.title("ECA - Grade Curricular - Acadêmico")
    janela_grade23.geometry("490x560+610+153")
    janela_grade23.resizable(width=0, height=0)
    janela_grade23['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral723 = Label(janela_grade23, text='S.A.G.I', font=("Calibri bold", 15), bg='#2d8659',fg = 'white')
    titulo_geral723.place(width=70, height=45, x=210, y=50)

    #----área das grades

    #legenda
    bt_gra23 = Label(janela_grade23, text='Périodo - Disciplina - Nome - Créditos - Carga Horária ', font=("Calibri", 14), bg='#194d33',fg = 'white')
    bt_gra23.place(width=450, height=30, x=20, y=110)


    bt_gra23 = Button(janela_grade23, text='1 - ESTBAS006 - Comunicação e Expressão - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white',command = janela_de_visualizacao)
    bt_gra23.place(width=450, height=45, x=20, y=150)
    bt_gra223 = Button(janela_grade23, text='1 - ESTBAS002 - Cálculo I - 6 - 90 ', font=("Calibri", 14), bg='#26734d',fg = 'white', command = visualizar_nota_calculo)
    bt_gra223.place(width=450, height=45, x=20, y=200)
    bt_gra323 = Button(janela_grade23, text='1 - ESTBAS007 - Física I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white', command = visualizar_nota_fisica)
    bt_gra323.place(width=450, height=45, x=20, y=250)
    bt_gra423 = Button(janela_grade23, text='1 - ESTBAS003 - Introdução à Engenharia - 2 - 30 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra423.place(width=450, height=45, x=20, y=300)
    bt_gra523 = Button(janela_grade23, text='1 - ESTBAS004 - Introdução Às Ciências Do Ambiente - 2 - 30 ', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_gra523.place(width=450, height=45, x=20, y=350)
    bt_gra623 = Button(janela_grade23, text='1 - ESTECP001 - Linguagem De Programação I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra623.place(width=450, height=45, x=20, y=400)
    bt_gra723 = Button(janela_grade23, text='1 - ESTBAS001 - Álgebra Linear I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra723.place(width=450, height=45, x=20, y=450)
    bt_gra823 = Button(janela_grade23, text='1 - ESTBAS017 - Introdução À Economia - 3 - 45 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra823.place(width=450, height=45, x=20, y=500)

def janela_de_escolha_de_disciplinas_para_lançar_nota():

    janela_grade2 = Tk()
    janela_grade2.title("ECA - Lançar/Editar - Notas")
    janela_grade2.geometry("490x560+610+153")
    janela_grade2.resizable(width=0, height=0)
    janela_grade2['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral72 = Label(janela_grade2, text='S.A.G.I', font=("Calibri bold", 15), bg='#2d8659',fg = 'white')
    titulo_geral72.place(width=70, height=45, x=210, y=50)

    #----área das grades

    #legenda
    bt_gra2 = Label(janela_grade2, text='Périodo - Disciplina - Nome - Créditos - Carga Horária ', font=("Calibri", 14), bg='#194d33',fg = 'white')
    bt_gra2.place(width=450, height=30, x=20, y=110)


    bt_gra2 = Button(janela_grade2, text='1 - ESTBAS006 - Comunicação e Expressão - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white',command = janela_de_notas)
    bt_gra2.place(width=450, height=45, x=20, y=150)
    bt_gra22 = Button(janela_grade2, text='1 - ESTBAS002 - Cálculo I - 6 - 90 ', font=("Calibri", 14),fg = 'white', bg='#26734d', command = nota_calculo)
    bt_gra22.place(width=450, height=45, x=20, y=200)
    bt_gra32 = Button(janela_grade2, text='1 - ESTBAS007 - Física I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra32.place(width=450, height=45, x=20, y=250)
    bt_gra42 = Button(janela_grade2, text='1 - ESTBAS003 - Introdução à Engenharia - 2 - 30 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra42.place(width=450, height=45, x=20, y=300)
    bt_gra52 = Button(janela_grade2, text='1 - ESTBAS004 - Introdução Às Ciências Do Ambiente - 2 - 30 ', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_gra52.place(width=450, height=45, x=20, y=350)
    bt_gra62 = Button(janela_grade2, text='1 - ESTECP001 - Linguagem De Programação I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra62.place(width=450, height=45, x=20, y=400)
    bt_gra72 = Button(janela_grade2, text='1 - ESTBAS001 - Álgebra Linear I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra72.place(width=450, height=45, x=20, y=450)
    bt_gra82 = Button(janela_grade2, text='1 - ESTBAS017 - Introdução À Economia - 3 - 45 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra82.place(width=450, height=45, x=20, y=500)

def calculadora_de_notas():

    global n1, n2, n3, statuss, mediafinal,mf11

    #Função do calculo das notas

    n1 = int(ap1.get())
    n2 = int(ap2.get())
    n3 = int(ap3.get())
    mf = (n1 + n2 + n3)/3
    mf11 = ("%.2f"% mf)
    mediafinal["text"] = ("%.2f" % mf)
    print("%.2f" % mf)
    if mf >= 6:
        statuss=('Aprovado')
        print('Aprovado')
        legendastatus["text"] = 'Aprovado'
    else:
        statuss = ('Reprovado')
        print('Reprovado')
        legendastatus["text"] = 'Reprovado'

def calculadora_de_notas2():

    global n11, n22, n33, statuss1, mediafinal51, mf111, ap15, ap25, ap35

    # Função do calculo das notas

    #n11 = int(ap15.get())
    n22 = int(ap25.get())
    n33 = int(ap35.get())
    mf1 = (10 + n22 + n33) / 3
    mf111 = ("%.2f" % mf1)
    mediafinal51["text"] = ("%.2f" % mf1)
    print("%.2f" % mf1)
    if mf1 >= 6:
        statuss1 = ('Aprovado')
        print('Aprovado')
        legendastatus5["text"] = 'Aprovado'
    else:
        statuss1 = ('Reprovado')
        print('Reprovado')
        legendastatus5["text"] = 'Reprovado'

def janela_de_notas():

    global ap1, ap2, ap3, mediafinal, legendastatus

    janela_notas = Tk()
    janela_notas.title("ECA - Notas")
    janela_notas.geometry("490x560+610+153")
    janela_notas.resizable(width=0, height=0)
    janela_notas['bg'] = '#2d8659'


    #---área do titulo

    titulo_geral9 = Label(janela_notas, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white')
    titulo_geral9.place(width=150, height=45, x=170, y=50)

    #informações básicas do aluno

    titulo_aluno = Label(janela_notas, text='Alexander Sweney De Franca Souza', font=("Calibri", 15), bg='#194d33',fg = 'white')
    titulo_aluno.place(width=400, height=45, x=50, y=120)

    #legenda das notas

    legendanota = Label(janela_notas, text='Comunicação e expressão', font=("Calibri bold", 13), bg='#194d33',fg = 'white')
    legendanota.place(width=200, height=40, x=140, y=190)
    legendastatus = Label(janela_notas, text='', font=("Calibri", 15), bg='#194d33',fg = 'white')
    legendastatus.place(width=100, height=45, x=300, y=290)


    #legenda final da pagina
    legendanota2 = Label(janela_notas, text='Abreviações', font=("Calibri", 13), bg='#194d33',fg = 'white')
    legendanota2.place(width=180, height=30, x=10, y=400)
    legendanota3 = Label(janela_notas, text='AP - Avaliação Parcial', font=("Calibri", 13), bg='#194d33',fg = 'white')
    legendanota3.place(width=180, height=30, x=10, y=430)
    legendanota4 = Label(janela_notas, text='MF - Média Final', font=("Calibri", 13), bg='#194d33',fg = 'white')
    legendanota4.place(width=180, height=30, x=10, y=460)

    #legenda das AP's
    legenda1 = Label(janela_notas, text='AP1', font=("Calibri", 15), bg='#2d8659',fg = 'white')
    legenda1.place(width=45, height=45, x=100, y=240)
    legenda2 = Label(janela_notas, text='AP2', font=("Calibri", 15), bg='#2d8659',fg = 'white')
    legenda2.place(width=45, height=45, x=150, y=240)
    legenda3 = Label(janela_notas, text='AP3', font=("Calibri", 15), bg='#2d8659',fg = 'white')
    legenda3.place(width=45, height=45, x=200, y=240)
    legenda4 = Label(janela_notas, text='MF', font=("Calibri", 15), bg='#2d8659',fg = 'white')
    legenda4.place(width=45, height=45, x=250, y=240)

    #---área de input de notas

    ap1 = Entry(janela_notas, bd=0, font=("Calibri", 15), justify=CENTER)
    ap1.place(width=45, height=45, x=100, y=290)
    ap2 = Entry(janela_notas, bd=0, font=("Calibri", 15), justify=CENTER)
    ap2.place(width=45, height=45, x=150, y=290)
    ap3 = Entry(janela_notas, bd=0, font=("Calibri", 15), justify=CENTER)
    ap3.place(width=45, height=45, x=200, y=290)
    mediafinal = Label(janela_notas, bd=0, font=("Calibri", 15), justify=CENTER)
    mediafinal.place(width=45, height=45, x=250, y=290)


    #---a partir daqui tudo pode estar errado

    #Criação de botão para inserir a nota

    bt_cadastar = Button(janela_notas, text='Cadastrar', font=("Calibri",15),bg = '#26734d' , justify=CENTER,fg = 'white', command=calculadora_de_notas)
    bt_cadastar.place(width=100, height=45, x=350, y=460)


    # janela_login['bg'] = '#2d8659' -BACKGROUND e label
    # ,fg = 'white'
    # senha = Label(janela_login, text = 'SENHA', font=("Calibri bold", 10), bg = '#2d8659',fg = 'white' LABEL
    #  bg="#26734d" ---- BOTÃO

def janela_de_academico():

    janela_academico = Tk()
    janela_academico.title("ECA - Acadêmico")
    janela_academico.geometry("490x560+610+153")
    janela_academico.resizable(width=0, height=0)
    janela_academico['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral8 = Label(janela_academico, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white' )
    titulo_geral8.place(width=150, height=45, x=170, y=50)

    #---área de escolha

    texto_aca = Label(janela_academico, text='Nome: Alexander Sweney De Franca Souza', font=("Calibri bold", 15), bg='#26734d',fg = 'white')
    texto_aca.place(width=400, height=45, x=50, y=150)
    texto_aca2 = Label(janela_academico, text='Matricula: 2115180028', font=("Calibri bold", 15), bg='#26734d',fg = 'white')
    texto_aca2.place(width=400, height=45, x=50, y=200)
    texto_aca3 = Label(janela_academico, text='Curso: Engenharia de Controle e Automação', font=("Calibri bold", 15), bg='#26734d',fg = 'white')
    texto_aca3.place(width=400, height=45, x=50, y=250)
    texto_aca4 = Label(janela_academico, text='Semestre: 1º/2021', font=("Calibri bold", 15), bg='#26734d',fg = 'white')
    texto_aca4.place(width=400, height=45, x=50, y=300)
    texto_aca5 = Label(janela_academico, text='Ano de ingresso: 2021', font=("Calibri bold", 15), bg='#26734d',fg = 'white')
    texto_aca5.place(width=400, height=45, x=50, y=350)


    bt_aca = Button(janela_academico, text='Visualizar Notas', font=("Calibri bold", 15), bg='#26734d',fg = 'white', command = janela_de_escolha_de_visualizacao_de_notas)
    bt_aca.place(width=150, height=45, x=280, y=450)

    bt_aca = Button(janela_academico, text='Adicionar Notas', font=("Calibri bold", 15), bg='#26734d',fg = 'white', command = janela_de_escolha_de_disciplinas_para_lançar_nota)
    bt_aca.place(width=150, height=45, x=80, y=450)

def janela_de_discentes():

    janela_discentes = Tk()
    janela_discentes.title("ECA - Discentes")
    janela_discentes.geometry("490x560+610+153")
    janela_discentes.resizable(width=0, height=0)
    janela_discentes['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral6 = Label(janela_discentes, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white')
    titulo_geral6.place(width=150, height=45, x=170, y=50)

    #---área dos botões

    bt_dis = Button(janela_discentes, text='2115180028 - Alexander Sweney De Franca Souza', font=("Calibri", 13), bg='#26734d', command = janela_de_academico,fg = 'white')
    bt_dis.place(width=400, height=45, x=50, y=150)
    bt_dis2 = Button(janela_discentes, text='2115180029 - Amanda Ferreira Das Neves', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis2.place(width=400, height=45, x=50, y=200)
    bt_dis3 = Button(janela_discentes, text='2115180001 - Ana Paula Silva Do Nascimento', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis3.place(width=400, height=45, x=50, y=250)
    bt_dis4 = Button(janela_discentes, text='2115180002 - André De Oliveira Sacramento', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis4.place(width=400, height=45, x=50, y=300)
    bt_dis5 = Button(janela_discentes, text='2115180061 - Carlos Andres Ramos Losada Junior', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis5.place(width=400, height=45, x=50, y=350)
    bt_dis6 = Button(janela_discentes, text='2115180004 - Enzo Vinicius Lima Domingues', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis6.place(width=400, height=45, x=50, y=400)
    bt_dis7 = Button(janela_discentes, text='2115180005 - Fernando Paes Franco', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis7.place(width=400, height=45, x=50, y=450)
    bt_dis7 = Button(janela_discentes, text='2115180030 - Francisco Gomes Do Nascimento Neto', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_dis7.place(width=400, height=45, x=50, y=450)

def janela_de_docentes():
    janela_docentes = Tk()
    janela_docentes.title("ECA - Docentes")
    janela_docentes.geometry("490x560+610+153")
    janela_docentes.resizable(width=0, height=0)
    janela_docentes['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral5 = Label(janela_docentes, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white')
    titulo_geral5.place(width=150, height=45, x=170, y=50)

    #---Legenda dos docentes

    bt_gra1 = Label(janela_docentes, text='Mátricula   -   Nome   -   E-mail', font=("Calibri bold", 14), bg='#194d33', fg = 'white')
    bt_gra1.place(width=450, height=30, x=20, y=110)


    #funções-botões

    bt_doce = Label(janela_docentes, text='10150 - Alessandro de Souza Bezzera - abezerra@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce.place(width=450, height=45, x=20, y=150)
    bt_doce2 = Label(janela_docentes, text='1506 - Alexandra Salerno Pinheiro - aspinheiro@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce2.place(width=450, height=45, x=20, y=200)
    bt_doce3 = Label(janela_docentes, text='1653 - Antonio Geraldo Harb - aharb@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce3.place(width=450, height=45, x=20, y=250)
    bt_doce4 = Label(janela_docentes, text='2885 - Aristides Rivera Torres - artorres@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce4.place(width=450, height=45, x=20, y=300)
    bt_doce5 = Label(janela_docentes, text='4634 - Armando Clóvis Marques De Souza - acmsouza@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce5.place(width=450, height=45, x=20, y=350)
    bt_doce6 = Label(janela_docentes, text='67 - Carly Pinheiro Trindade - ctrindade@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce6.place(width=450, height=45, x=20, y=400)
    bt_doce7 = Label(janela_docentes, text='941 - Claudio Barros Vitor - cvitor@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce7.place(width=450, height=45, x=20, y=450)
    bt_doce8 = Label(janela_docentes, text='963 - Cleto Cavalcante De Souza Leal - cleal@uea.edu.br', font=("Calibri bold", 12), bg='#26734d',fg = 'white')
    bt_doce8.place(width=450, height=45, x=20, y=500)

def janela_de_grade_curricular():
    janela_grade = Tk()
    janela_grade.title("ECA - Grade Curricular")
    janela_grade.geometry("490x560+610+153")
    janela_grade.resizable(width=0, height=0)
    janela_grade['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral7 = Label(janela_grade, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white')
    titulo_geral7.place(width=150, height=45, x=170, y=50)


    #----área das grades

    #legenda
    bt_gra1 = Label(janela_grade, text='Período - Código - Nome - Créditos - Carga Horária ', font=("Calibri bold", 14), bg='#194d33', fg = 'white')
    bt_gra1.place(width=450, height=30, x=20, y=110)


    bt_gra = Label(janela_grade, text='1 - ESTBAS006 - Comunicação e Expressão - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra.place(width=450, height=45, x=20, y=150)
    bt_gra2 = Label(janela_grade, text='1 - ESTBAS002 - Cálculo I - 6 - 90 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra2.place(width=450, height=45, x=20, y=200)
    bt_gra3 = Label(janela_grade, text='1 - ESTBAS007 - Física I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra3.place(width=450, height=45, x=20, y=250)
    bt_gra4 = Label(janela_grade, text='1 - ESTBAS003 - Introdução à Engenharia - 2 - 30 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra4.place(width=450, height=45, x=20, y=300)
    bt_gra5 = Label(janela_grade, text='1 - ESTBAS004 - Introdução Às Ciências Do Ambiente - 2 - 30 ', font=("Calibri", 13), bg='#26734d',fg = 'white')
    bt_gra5.place(width=450, height=45, x=20, y=350)
    bt_gra6 = Label(janela_grade, text='1 - ESTECP001 - Linguagem De Programação I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra6.place(width=450, height=45, x=20, y=400)
    bt_gra7 = Label(janela_grade, text='1 - ESTBAS001 - Álgebra Linear I - 4 - 60 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra7.place(width=450, height=45, x=20, y=450)
    bt_gra8 = Label(janela_grade, text='1 - ESTBAS017 - Introdução À Economia - 3 - 45 ', font=("Calibri", 14), bg='#26734d',fg = 'white')
    bt_gra8.place(width=450, height=45, x=20, y=500)

def controle_e_automacao():
    janela_automacao = Tk()
    janela_automacao.title("Engenharia de Controle e Automação")
    janela_automacao.geometry("490x560+610+153")
    janela_automacao.resizable(width=0, height=0)
    janela_automacao['bg'] = '#2d8659'

    #---área do titulo

    titulo_geral4 = Label(janela_automacao, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659',fg = 'white')
    titulo_geral4.place(width=150, height=45, x=170, y=50)

    #funções-botões

    bt_automacao2 = Label(janela_automacao, text='ENGENHARIA DE CONTROLE E AUTOMAÇÃO', font=("Calibri bold", 17), bg='#2d8659',fg = 'white')
    bt_automacao2.place(width=490, height=50, x=5, y=150)
    bt_automacao3 = Button(janela_automacao, text='DISCENTES', font=("Calibri bold", 15), bg='#26734d',fg = 'white', command = janela_de_discentes)
    bt_automacao3.place(width=400, height=50, x=50, y=230)
    bt_automacao4 = Button(janela_automacao, text='DOCENTES', font=("Calibri bold", 15), bg='#26734d',fg = 'white',command = janela_de_docentes)
    bt_automacao4.place(width=400, height=50, x=50, y=310)
    bt_automacao5 = Button(janela_automacao, text='GRADE CURRICULAR', font=("Calibri bold ", 15), bg='#26734d',fg = 'white', command = janela_de_grade_curricular)
    bt_automacao5.place(width=400, height=50, x=50, y=390)

def janela_de_graduacao():


    janela_graducao = Tk()
    janela_graducao.title("Graduação")
    janela_graducao.geometry("490x560+610+153")
    janela_graducao.resizable(width=0, height=0)
    janela_graducao['bg'] = '#2d8659'


    #---área de titulo

    titulo_geral3 = Label(janela_graducao, text='S.A.G.I', font=("Calibri bold", 15), bg='#2d8659', fg='white')
    titulo_geral3.place(width=70, height=45, x=210, y=50)

    #---área do curso

    bt_automacao = Button(janela_graducao, text='ENGENHARIA DE CONTROLE E AUTOMAÇÃO', font=("Calibri", 15), bg='#26734d' ,fg = 'white', command = controle_e_automacao)
    bt_automacao.place(width=400, height=45, x=50, y=100)
    bt_computacao = Button(janela_graducao, text='ENGENHARIA DA COMPUTAÇÃO', font=("Calibri ", 15), bg='#26734d',fg = 'white')
    bt_computacao.place(width=400, height=45, x=50, y=150)
    bt_civil = Button(janela_graducao, text='ENGENHARIA CIVIL', font=("Calibri ", 15), bg='#26734d',fg = 'white')
    bt_civil.place(width=400, height=45, x=50, y=200)
    bt_eletrica = Button(janela_graducao, text='ENGENHARIA ELÉTRICA', font=("Calibri ", 15), bg='#26734d',fg = 'white')
    bt_eletrica.place(width=400, height=45, x=50, y=250)
    bt_eletronica = Button(janela_graducao, text='ENGENHARIA ELETRÔNICA', font=("Calibri", 15), bg='#26734d',fg = 'white')
    bt_eletronica.place(width=400, height=45, x=50, y=300)
    bt_mecanica = Button(janela_graducao, text='ENGENHARIA MECÂNICA', font=("Calibri", 15), bg='#26734d',fg = 'white')
    bt_mecanica.place(width=400, height=45, x=50, y=350)
    bt_naval = Button(janela_graducao, text='ENGENHARIA NAVAL', font=("Calibri", 15), bg='#26734d',fg = 'white')
    bt_naval.place(width=400, height=45, x=50, y=400)
    bt_producao = Button(janela_graducao, text='ENGENHARIA PRODUÇÃO', font=("Calibri", 15), bg='#26734d',fg = 'white')
    bt_producao.place(width=400, height=45, x=50, y=450)

def janela_de_pos():

    janela_pos = Tk()
    janela_pos.title("Pós-graduação")
    janela_pos.geometry("490x560+610+153")
    janela_pos.resizable(width=1, height=1)
    janela_pos['bg'] = '#2d8659'

    #----área de imagens e label

    titulo_geral2 = Label(janela_pos, text='S.A.G.I', font=("Calibri bold", 30), bg='#2d8659', fg='white')
    titulo_geral2.place(width=150, height=45, x=170, y=50)

    texto_esp = Button(janela_pos, text = "ESPECIALIZAÇÃO" , bg = "#26734d" , font=("Calibri bold", 15),fg='white', justify=CENTER)
    texto_esp.place(width=392, height=45, x=49, y=200)

    texto_mes = Button(janela_pos, text="MESTRADO", bg = "#26734d" , font=("Calibri bold", 15),fg='white', justify=CENTER)
    texto_mes.place(width=392, height=45, x=49, y=250)

    texto_dou = Button(janela_pos, text="DOUTORADO", bg = "#26734d" , font=("Calibri bold", 15), fg='white', justify=CENTER)
    texto_dou.place(width=392, height=45, x=49, y=300)

def teste_de_acesso():

    login = en_email.get()
    senha = (en_senha.get())
    if login == 'mario.bessa@uea.edu.br' and senha == '2021':

        #janela_login.destroy()
        time.sleep(0.3)

        janela_modalidade = Tk()
        janela_modalidade.title("Modalidade")
        janela_modalidade.geometry("490x560+610+153")
        janela_modalidade.resizable(width=1, height=1)
        janela_modalidade['bg'] = '#2d8659'

        titulo_geral = Label(janela_modalidade, text='S.A.G.I', font=("Calibri bold", 30), fg='white', bg='#2d8659')
        titulo_geral.place(width=150, height=45, x=170, y=50)

        # ----área dos botôes
        bt_entrar2 = Button(janela_modalidade, text='GRADUAÇÃO', font=("Calibri bold", 15), bg='#26734d', fg='white', command = janela_de_graduacao)
        bt_entrar2.place(width=272, height=56, x=110, y=190)
        bt_entrar3 = Button(janela_modalidade, text='PÓS-GRADUAÇÃO', font=("Calibri bold", 15), bg='#26734d', fg='white', command=janela_de_pos)
        bt_entrar3.place(width=272, height=56, x=110, y=315)
    else:
        if login == 'mario.bessa@uea.edu.br' and senha != '2021':
            titulo_geral = Label(janela_login, text='Senha incorreta', font=("Calibri", 15), bg='white')
            titulo_geral.place(width=250, height=30, x=120, y=380)
        else:
            if senha == '2021' and login != 'mario.bessa@uea.edu.br':
                titulo_geral = Label(janela_login, text='E-mail incorreto', font=("Calibri", 15), bg='white')
                titulo_geral.place(width=250, height=30, x=120, y=380)
            else:
                titulo_geral = Label(janela_login, text='E-mail ou senha incorretos', font=("Calibri", 15), bg='white')
                titulo_geral.place(width=250, height=30, x=120, y=380)

#----Tela de Login------------------

#---Janeça de Login

janela_login = Tk()
janela_login.title("Login")
janela_login.geometry("490x560+610+153")
janela_login.resizable(width=0, height=0)
janela_login['bg'] = '#2d8659'


#----Label

titulo = Label(janela_login, text = 'SISTEMA ACADÊMICO DE GESTÃO INTEGRADA', font=("Calibri bold", 18), bg = '#2d8659', fg='white', )
titulo.place(width=480, height=45, x=5, y=100)

email = Label(janela_login, text = 'E-MAIL', font=("Calibri bold", 10), bg = '#2d8659', fg = 'white')
email.place(width=45, height=45, x=1, y=205)

senha = Label(janela_login, text = 'SENHA', font=("Calibri bold", 10), bg = '#2d8659',fg = 'white')
senha.place(width=45, height=45, x=1, y=315)

#----Senha
esconda_senha = StringVar()

#----Entrada de dados de login

en_email = Entry(janela_login, bd=2, font=("Calibri", 15), justify=CENTER)
en_email.place(width=392, height=45, x=49, y=205)

en_senha = Entry(janela_login, textvariable=esconda_senha, show="*", bd=2, font=("Calibri " , 15), justify=CENTER)
en_senha.place(width=392, height=45, x=49, y=315)

#----Botão de login

bt_entrar = Button(janela_login, text = 'ENTRAR', font=("Calibri bold", 20), bg="#26734d", fg = 'white', command = teste_de_acesso)
bt_entrar.place(width=118, height=64, x=186, y=434)

janela_login.mainloop()





