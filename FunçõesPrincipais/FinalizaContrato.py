from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from tinydb import Query
import pandas as pd

Cliente = Query()

#retira o cliente do DB.json e coloca suas informaçoes principais em um arquivo .csv
def finalizaContrato(interface, id, interfacePrincipal):
    interface.withdraw()
    listaNome = []
    listaEndC = []
    listaEndO = []
    listaCpf = []
    listaCnpj = []
    try:
        dadosCliente = db.get(Cliente.id == int(id))
        listaNome.append(dadosCliente['nome'])
        listaEndC.append(dadosCliente['addresClient'])
        listaEndO.append(dadosCliente['addresObra'])
        listaCpf.append(dadosCliente['cpf'])
        listaCnpj.append(dadosCliente['cnpj'])
        db.remove(Cliente.id == int(id))
        mostraMensagem("Ação bem sucessida!", "Contrato foi finalizado com sucesso!\nSuas informaçoes estão no arquivo Clientes Finalizados!")
        
        df = pd.DataFrame(zip(listaNome, listaEndC, listaEndO, listaCpf, listaCnpj), columns = ["NomeCliente", "EndereçoCliente", "EndereçoObra", "CPF", "CNPJ"])
        if(os.path.exists("C:\\Users\\Pichau\\Documents\\VSCODE\\ProjetoLocadora\\Projeto-Alugadora-De-Itens\\ClientesFinalizados\\ClienteFinalizados.xlsx") == False):
            df.to_excel("C:\\Users\\Pichau\\Documents\\VSCODE\\ProjetoLocadora\\Projeto-Alugadora-De-Itens\\ClientesFinalizados\\ClienteFinalizados.xlsx", index = False)
        else:
            df2 = pd.read_excel("C:\\Users\\Pichau\\Documents\\VSCODE\\ProjetoLocadora\\Projeto-Alugadora-De-Itens\\ClientesFinalizados\\ClienteFinalizados.xlsx")
            df_concat = pd.concat([df2, df])
            df_concat.to_excel("C:\\Users\\Pichau\\Documents\\VSCODE\\ProjetoLocadora\\Projeto-Alugadora-De-Itens\\ClientesFinalizados\\ClienteFinalizados.xlsx", index = False)
        resetaIds = 1
        bd = db.all()
        for cliente in bd:
            db.update({'id': resetaIds}, Cliente.id == cliente['id'])
            resetaIds += 1
        interfacePrincipal.deiconify()
    except TypeError:
        interfacePrincipal.deiconify()