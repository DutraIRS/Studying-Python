import pandas as pd

inventario = pd.DataFrame(columns=["ID", "Nome", "Preço", "Quantidade Estoque"])

def listar_inventario():
    """Imprime no console os itens do inventário
    
    >>> listar_inventario()
    <BLANKLINE>
    ID                         2
    Nome                  Flauta
    Preço                   90.3
    Quantidade Estoque        20
    """
    for indice, linha in inventario.iterrows():
        print('\n', linha.to_string(), sep='')

    
def add_item(id: int, nome: str, preco: float, qtstck: int):
    """Adiciona item ao inventário
    
    :param id: Índice (único) do item
    :type id: int
    :param nome: Nome do item
    :type nome: str
    :param preco: Preço do item
    :type preco: float
    :param qtstck: Quantidade do item disponível no estoque
    :type qtstck: int
    :return: Booleano indicando se a operação foi bem-sucedida
    :rtype: bool
    
    >>> add_item(2, "Flauta", 90.3, 20)
    True
    """
    global inventario
    add = pd.DataFrame(data=[[id, nome, preco, qtstck]], columns=["ID", "Nome", "Preço", "Quantidade Estoque"])
    novo_inventario = pd.concat([inventario, add], axis=0)
    bem_sucedido = not novo_inventario.equals(inventario)
    inventario = novo_inventario
    return bem_sucedido
    
def rem_item(id: int):
    """Remove item do inventário
    
    :param id: Índice (único) do item
    :type id: int
    :return: Booleano indicando se a operação foi bem-sucedida
    :rtype: bool
    
    >>> rem_item(1)
    False
    """
    global inventario
    novo_inventario = inventario[inventario["ID"] != id]
    bem_sucedido = not novo_inventario.equals(inventario)
    inventario = novo_inventario
    return bem_sucedido
    
def busca_item():
    """Retorna os itens que possuem o parâmetro especificado
    
    :param attr: Atributo que será buscado, deve ser uma das colunas do DataFrame inventário
    :type attr: str
    :param value: Valor a ser buscado
    :type value: str
    :return: Dataframe dos itens encontrados
    :rtype: pandas.core.frame.DataFrame
    :raises:
        ValueError: Se attr não é coluna do DataFrame
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)