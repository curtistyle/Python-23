

class Node:
    def __init__(self, value, left=None, right=None, key=None):
        self.value = value
        self.left= left
        self.right= right
        self.key = key

class BinaryTree:
    @staticmethod
    def list_to_tree(tree, collection : list) -> None:
        for item in collection:
            tree.insert_node(item)

    def __init__(self):
        self.root = None
     
    def insert_node(self, node):
        def __insert(root : Node, value):
            if root is None:
                # print("New Root")
                return Node(value)
            elif value < root.value:
                # print("Insert on the left")
                root.left = __insert(root.left, value)
            else:
                # print("Insert on the right")
                root.right = __insert(root.right, value)
            return root  
        self.root = __insert(self.root, node)

    # def indert_node(self, node, key):
    #     def __insert(root, value, key):
    #         if root is None:
    #             return Node(node, key)
    #         elif (value[key] > root.value[key]):

    #     self.root = __insert(self.root, node, key)
        

    def search(self, key):
        """Busquena binaria"""
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    print("found")
                    return root
                elif (key < root.value):
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
            else:
                print("not found")
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
            return aux

    def preorden(self):
        """
        Barrido PRE-ORDEN
        -----------
        En el recorrido preorden, se sigue este patrón:

        primero:
            * Visitar primero el nodo raíz.
        segundo: 
            * Recorre el subárbol izquierdo.
        tercero:
            * Recorre el subárbol derecho.
        """
        def __preorden(root):
            if root is not None:
                print(root.value)
                # input()
                # print(f"Izquierda de {root.value}")
                __preorden(root.left)
                # print(f"Derecha de {root.value}")
                __preorden(root.right)
        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        """
        Barrido IN-ORDEN (ascendente)
        ------------
        En el recorrido inorden, se sigue este patrón:

        primero: 
            * Recorrer primero el subárbol izquierdo.
        segundo:
            * Visitar el nodo raíz.
        tercero:
            * Recorrer el subárbol derecho
        """
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)
        if self.root is not None:
            __inorden(self.root)

    def posorden(self):
        """
        Barrido POS-ORDEN (descendente)
        ----------
        En el recorrido posorden, se sigue este patrón:

        primero:
            * Recorrer primero el subárbol izquierdo.
        segundo:
            * Recorrer el subárbol derecho.
        tercero:
            * Visitar el nodo raíz al final.
        """
        def __posorden(root):
            if root is not None:
                __posorden(root.right)
                print(root.value)
                __posorden(root.left)
        if self.root is not None:
            __posorden(self.root)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplazar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value_delete
                
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value

    def select(self, predicate):
        result = None
        temp = list()
        def __select(root, predicate):
            if root is not None:
                if predicate(root.value) is True:
                    temp.append(root.value)
                __select(root.left, predicate)
                __select(root.right, predicate)
            return temp
            
        if self.root is not None:
            result = __select(self.root, predicate)
        return result
            

tree = BinaryTree()

tree.insert_node(19)
tree.insert_node(7)
tree.insert_node(31)
tree.insert_node(11)
tree.insert_node(10)
tree.insert_node(45)
tree.insert_node(22)
tree.insert_node(27)

tree.delete_node(7)

    
    