from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesEntrada import *
from FunçõesPrincipais.DefineId import *
from Interface.MostraEstoqueDisponivel import *
from FunçõesPrincipais.ValoresProdutos import *
from datetime import date
from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesEstoque import *
from tinydb import Query
Cliente = Query()

def insereClientes(interface):
    interface.withdraw()
    try:
        while True:
            nomeCliente = criaPerguntas("Inserir Cliente", "Digite o nome do cliente: ", verificaçãoNome)

            endereçoCliente = criaPerguntasSemFunçao("Inserir Cliente", "Digite o endereço do cliente: ")

            endereçoObra = criaPerguntasSemFunçao("Inserir Cliente", "Digite o endereço da obra: ")

            cpf = criaPerguntas("Inserir Cliente", "Digite o CPF do cliente: ", verificaçãoCPF)

            idCliente = defineId()

            cnpj = criaPerguntas("Inserir Cliente", "Digite o cnpj do cliente: \nCaso nao queira colocar o cnpj, digite conforme abaixo:\nn/a", verificaçãoCNPJ)
            
            verificacaoEscoras = None
            if(mostraEstoqueDisponivel(escoras, "quantity") == 0):
                verificacaoEscoras = verificaçãoEstoque(escoras, 'quantity', "escoras")
            else:
                valorEscora = criaPerguntas("Inserir Cliente", "Digite o valor da escora(1 Unidade): ", verificaçãoNUMERO)

                tamanhoEscora = criaPerguntas("Inserir Cliente", "Digite o tamanho da escora: ", verificaçãoNUMERO)
                
                quantidadeEscora = criaPerguntas("Inserir Cliente", "Digite a quantidade de escoras que serão alugadas: \nNo estoque estao disponíveis {} escoras.".format(mostraEstoqueDisponivel(escoras, "quantity")), verificaçãoNUMERO)
                if(int(quantidadeEscora) > mostraEstoqueDisponivel(escoras, "quantity")):
                    mostraMensagem("Erro de Alugamento", "Não foi possível alugar as escoras, pois você colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break

            if(verificacaoEscoras == 2):
                break
            elif(verificacaoEscoras == 1):
                tamanhoEscora = 0
                quantidadeEscora = 0
                valorEscora = 0

            diaAtual = date.today().strftime('%d/%m/%Y')

            duraçaoContrato = criaPerguntas("Inserir Cliente", "Selecione a data em que o contrato irá vencer: \nExemplo de data:\n11/09/2023\n03/11/2024", verificaçãoDATA)

            formaPagamento = criaPerguntasSemFunçao("Inserir Cliente", "Qual a forma de pagamento(INICIO/VENCIMENTO): ").lower()
            
            verificacaoAndaimes = None
            if(mostraEstoqueDisponivel(andaimes, "quantityAndaimes") == 0):
                verificacaoAndaimes = verificaçãoEstoque(andaimes, 'quantityAndaimes', "andaimes")
            else:
                valorAndaime = criaPerguntas("Inserir Cliente", "Digite o preço do andaime(1 Unidade): ", verificaçãoNUMERO)
                quantidadeAndaime = criaPerguntas("Inserir Cliente", "Digite a quantidade de andaimes que serão alugados: \nNo estoque estao disponíveis {} andaimes.".format(mostraEstoqueDisponivel(andaimes, "quantityAndaimes")), verificaçãoNUMERO)
                if(int(quantidadeAndaime) > int(mostraEstoqueDisponivel(andaimes, "quantityAndaimes"))):
                    mostraMensagem("Erro de Alugamento", "Não foi possivei alugar os andaimes, pois voce colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break

            if(verificacaoAndaimes == 2):
                break
            elif(verificacaoAndaimes == 1):
                quantidadeAndaime = 0
                valorAndaime = 0

            verificacaoBetoneiras = None
            if(mostraEstoqueDisponivel(betoneiras, "quantityBetoneira") == 0):
                verificacaoBetoneiras = verificaçãoEstoque(betoneiras, 'quantityBetoneira', "betoneiras")
            else:
                valorBetoneira = criaPerguntas("Inserir Cliente", "Digite o preço da betoneira(1 Unidade): ", verificaçãoNUMERO)
                quantidadeBetoneira = criaPerguntas("Inserir Cliente", "Digite a quantidade de betoneiras que serão alugadas: \nNo estoque estao disponíveis {} betoneiras.".format(mostraEstoqueDisponivel(betoneiras, "quantityBetoneira")), verificaçãoNUMERO)
                if(int(quantidadeBetoneira) > int(mostraEstoqueDisponivel(betoneiras, "quantityBetoneira"))):
                    mostraMensagem("Erro de Alugamento", "Não foi possivei alugar a(s) betoneira(s), pois voce colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break

            if(verificacaoBetoneiras == 2):
                break
            elif(verificacaoBetoneiras == 1):
                quantidadeBetoneira = 0
                valorBetoneira = 0

            verificacaoRoldanas = None
            if(mostraEstoqueDisponivel(roldanas, "quantityRoldana") == 0):
                verificacaoRoldanas = verificaçãoEstoque(roldanas, 'quantityRoldana', "roldanas")
            else:
                valorRoldana = criaPerguntas("Inserir Cliente", "Digite o preço da roldana(1 Unidade): ", verificaçãoNUMERO)
                quantidadeRoldana = criaPerguntas("Inserir Cliente", "Digite a quantidade de roldanas que serão alugadas: \nNo estoque estao disponíveis {} roldanas.".format(mostraEstoqueDisponivel(roldanas, "quantityRoldana")), verificaçãoNUMERO)
                if(int(quantidadeRoldana) > int(mostraEstoqueDisponivel(roldanas, "quantityRoldana"))):
                    mostraMensagem("Erro de Alugamento", "Não foi possivei alugar as roldanas, pois voce colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break

            if(verificacaoRoldanas == 2):
                break
            elif(verificacaoRoldanas == 1):
                quantidadeRoldana = 0
                valorRoldana = 0

            verificacaoReguladores = None
            if(mostraEstoqueDisponivel(reguladores, "quantityRegulador") == 0):
                verificacaoReguladores = verificaçãoEstoque(reguladores, 'quantityRegulador', "reguladores")
            else:
                valorRegulador = criaPerguntas("Inserir Cliente", "Digite o preço do regulador(1 Unidade): ", verificaçãoNUMERO)
                quantidadeRegulador = criaPerguntas("Inserir Cliente", "Digite a quantidade de reguladores que serão alugados: \nNo estoque estao disponíveis {} reguladores.".format(mostraEstoqueDisponivel(reguladores, "quantityRegulador")), verificaçãoNUMERO)
                if(int(quantidadeRegulador) > int(mostraEstoqueDisponivel(reguladores, "quantityRegulador"))):
                    mostraMensagem("Erro de Alugamento", "Não foi possivei alugar os reguladores, pois voce colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break
            
            if(verificacaoReguladores == 2):
                break
            elif(verificacaoReguladores == 1):
                quantidadeRegulador = 0
                valorRegulador = 0

            verificacaoPlataformas = None
            if(mostraEstoqueDisponivel(plataformas, "quantityPlataforma") == 0):
                verificacaoPlataformas = verificaçãoEstoque(plataformas, 'quantityPlataforma', "plataformas")
            else:
                valorPlataforma = criaPerguntas("Inserir Cliente", "Digite o preço da plataforma(1 Unidade): ", verificaçãoNUMERO)
                tamanhoPlataforma = criaPerguntas("Inserir Cliente", "Digite o tamanho da plataforma: ", verificaçãoNUMERO)
                quantidadePlataforma = criaPerguntas("Inserir Cliente", "Digite a quantidade de plataformas que serão alugadas: \nNo estoque estao disponíveis {} plataformas.".format(mostraEstoqueDisponivel(plataformas, "quantityPlataforma")), verificaçãoNUMERO)
                if(int(quantidadePlataforma) > int(mostraEstoqueDisponivel(plataformas, "quantityPlataforma"))):
                    mostraMensagem("Erro de Alugamento", "Não foi possivei alugar as plataformas, pois voce colocou número maior que o disponível no estoque!")
                    interface.deiconify()
                    break

            if(verificacaoPlataformas == 2):
                break
            elif(verificacaoPlataformas == 1):
                tamanhoPlataforma = 0
                quantidadePlataforma = 0
                valorPlataforma = 0

            pagamentoTotal = ((float(valorEscora) * float(quantidadeEscora)) + ((float(quantidadeAndaime) * float(valorAndaime)) + (float(quantidadeBetoneira) * float(valorBetoneira)) + (float(quantidadePlataforma) * float(valorPlataforma)) + (float(quantidadeRegulador) * float(valorRegulador)) + (float(quantidadeRoldana) * float(valorRoldana))))

            db.insert(
                {
                    'nome': nomeCliente,
                    'addresClient': endereçoCliente,
                    'addresObra': endereçoObra,
                    'cpf': cpf,
                    'cnpj': cnpj,
                    'valueEscora': valorEscora,
                    'sizeEscora': tamanhoEscora,
                    'quantity': quantidadeEscora,
                    'paymentAmount': pagamentoTotal,
                    'todayDate': diaAtual,
                    'paymentDate': duraçaoContrato,
                    'formPayment': formaPagamento,
                    'quantityAndaimes': quantidadeAndaime,
                    'valueAndaimes': valorAndaime,
                    'id': idCliente,
                    'quantityBetoneira': quantidadeBetoneira,
                    'valueBetoneira': valorBetoneira,
                    'quantityRoldana': quantidadeRoldana,
                    'valueRoldana': valorRoldana,
                    'quantityRegulador': quantidadeRegulador,
                    'valueRegulador': valorRegulador,
                    'quantityPlataforma': quantidadePlataforma,
                    'valuePlataforma': valorPlataforma,
                    'sizePlataforma': tamanhoPlataforma,
                    'statePayment': "Pago" if formaPagamento=="inicio" else "Pendente"
                }
            )
            mostraMensagem("Açao bem-sucedida!", "O cliente foi cadastrado com sucesso!")
            interface.deiconify()
            break
    except TypeError:
        interface.deiconify()
    except AttributeError:
        interface.deiconify()
        
    resetaIds = 1
    bd = db.all()
    for cliente in bd:
        db.update({'id': resetaIds}, Cliente.id == cliente['id'])
        resetaIds += 1