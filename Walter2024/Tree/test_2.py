from Binary_Tree.cola import Queue



class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, key=None):
            self.value = value
            self.left = left
            self.right = right
            self.key = key

    def __init__(self):
        self.root = None

    def insert_node(self, value, key=None):
        def __insert_by_key(root, value, key):
            if root is None:
                return BinaryTree.__Node(value, key=key)
            elif value[key] < root.value[key]:
                root.left = __insert_by_key(root.left, value, key)
            else:
                root.right = __insert_by_key(root.right, value, key)
            return root

        def __insert(root, value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)
            return root

        if key is not None:
            self.root = __insert_by_key(self.root, value, key)
        else:
            self.root = __insert(self.root, value)


    def search(self, value, key=None):
        # ! search by key
        def __search_ky_key(root, value, key):
            if root is not None:
                if root.value[key] == value:
                    # print('lo encontre')
                    return root
                elif value < root.value[key]:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search_ky_key(root.left, value, key=key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search_ky_key(root.right, value, key=key)
            # else:
            #     print('no hay nada')
        
        
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    # print('lo encontre')
                    return root
                elif value < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, value, key=key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, value, key=key)
            # else:
            #     print('no hay nada')

        aux = None
        if self.root is not None:
            if key is not None:
                aux = __search_ky_key(self.root, value, key)    
            else:
                aux = __search(self.root, value, key)    
        return aux

    def preorden(self, key=None):
        def __preorden(root):
            if root is not None:
                print("root value: ", root.value)
                # a = input()
                # print(f'izquierda de {root.value}')
                __preorden(root.right)
                __preorden(root.left)
                # print(f'derecha de {root.value}')

        def __preorden_by_key(root, key):
            if root is not None:
                print(root.value[key])
                __preorden_by_key(root.left, key=key)
                __preorden_by_key(root.right, key=key)

        if self.root is not None:
            if key is not None:
                __preorden_by_key(self.root, key)
            else:    
                __preorden(self.root)

    def inorden(self, key=None):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        def __inorden_by_key(root, key):
            if root is not None:
                __inorden_by_key(root.left, key)
                print(root.value[key])
                __inorden_by_key(root.right, key)

        if self.root is not None:
            if key is not None:
                __inorden_by_key(self.root, key)
            else:
                __inorden(self.root)

    def postorden(self, key=None):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)
        
        def __postorden_by_key(root, key):
            if root is not None:
                __postorden_by_key(root.right, key)
                print(root.value[key])
                __postorden_by_key(root.left, key)

        if self.root is not None:
            if key is not None:
                __postorden_by_key(self.root, key)
            else:
                __postorden(self.root)

    def delete_node(self, value, key=None):
        def __replace(root):
            if root.right is None:
                print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                print('seguir buscando nodo par remplazar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete_by_key(root, value, key):
            value_delete = None
            if root is not None:
                if root.value[key] > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete_by_key(root.left, value, key)
                elif root.value[key] < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete_by_key(root.right, value, key)
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
            if key is not None:
                self.root, delete_value = __delete_by_key(self.root, value, key)
            else:
                self.root, delete_value = __delete(self.root, value)
        return delete_value

    def by_level(self, key=None):
        def Contador(msg, inc=[0]):
            inc[0] = inc[0] + 1
            print(msg, inc[0])
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)
        while pendientes.size() > 0:
            if pendientes.size() == 1: Contador(msg="Nivel ")
            node = pendientes.attention()
            if key is not None:
                print(node.value[key])
            else:
                print(node.value)
            # * si el hijo izquierdo no esta vacio
            if node.left is not None:
                pendientes.arrive(node.left)
            # * si el hijo derecho no esta vacio
            if node.right is not None:
                pendientes.arrive(node.right)
            

people = [
    {'name':'Santiago', 'age': 33, 'country': 'Aldea San Antonio'},
    {'name':'Pedro', 'age': 42, 'country': 'Aldea San Juan'},
    {'name':'Marcos', 'age': 43, 'country': 'Concepcion del Uruguay'},
    {'name':'Cristian', 'age': 12, 'country': 'Rosario'},
    {'name':'Waldo', 'age': 32, 'country': 'Federacion'},
    {'name':'Agustin', 'age': 22, 'country': 'Gualeguaychu'},
    {'name':'Luis', 'age': 31, 'country': 'Gualeguaychu'},
    {'name':'Franco', 'age': 12, 'country': 'Parana'},
    {'name':'Walter', 'age': 40, 'country': 'Rosario'},
    {'name':'Maria', 'age': 17, 'country': 'Aldea San Juan'},
    {'name':'Soledad', 'age': 21, 'country': 'Concepcion del Uruguay'},
]



tree = BinaryTree()

for person in people:
    tree.insert_node(person, key='name')

print(f"PREORDEN: ")
tree.preorden(key='name')
print(f"\nIRORDEN: ")
tree.inorden(key='name')
print(f"\nPOSORDEN: ")
tree.postorden(key='name')

eliminar = "Franco"

print(f"Buscar {eliminar}: ", tree.search(eliminar, 'name').value)

tree.delete_node(eliminar, key='name')

print(f"\n Se Elimino \'{eliminar}\' IRORDEN: ")
tree.inorden(key='name')

print(f"\n Barrido por nivel: ")
tree.by_level(key="name")

# tree.insert_node(19)
# tree.insert_node(7)
# tree.insert_node(31)
# tree.insert_node(11)
# tree.insert_node(10)
# tree.insert_node(45)
# tree.insert_node(22)
# tree.insert_node(27)

# pos = tree.search(27)
# if pos:
#     print('lo encontre', pos.value)
# else:
#     print('no esta')

# tree.delete_node(7)
# tree.delete_node(11)
# tree.delete_node(31)
# tree.delete_node(27)
# tree.delete_node(45)
# tree.delete_node(22)
# tree.delete_node(19)
# tree.delete_node(10)
# tree.insert_node(27)

# print(tree.delete_node(100))

