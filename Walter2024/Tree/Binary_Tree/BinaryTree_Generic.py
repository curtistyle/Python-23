from cola import Queue

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

    def nearby_search(self, value, key) -> list:
        items=[]
        def __nearby_search(root, value, key):
            if root is not None:
                if str.lower(root.value[key]).startswith(value.lower()):
                    items.append(root.value)
                __nearby_search(root.left, value, key )
                __nearby_search(root.right, value, key)
            return items
        
        if self.root is not None:
            return __nearby_search(self.root, value, key)
        return items

    def replace(self, seek, new_value, key_for_new_value):
        def __search(root, seek):
            if root is not None:
                if root.value[root.key] == seek:
                    # print('lo encontre')
                    return root.value
                elif seek < root.value[root.key]:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, seek)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, seek)
        if self.root is not None:
            old_node = __search(self.root, seek)
        self.delete_node(old_node[self.root.key], self.root.key)
        
        old_node[key_for_new_value] = new_value
        self.insert_node(old_node, self.root.key)  

    def postorden(self, key=None, predicate=None):
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

        def __postorden_predicate(root, key, predicate):
            if root is not None:
                __postorden_predicate(root.right, key, predicate)
                if predicate(root.value):
                    if key is not None:
                        print(root.value[key])
                    else:
                        print(root.value)
                __postorden_predicate(root.left, key, predicate)
                        
        if self.root is not None:
            if predicate is not None:
                __postorden_predicate(self.root, key, predicate)
            elif key is not None:
                __postorden_by_key(self.root, key)
            else:
                __postorden(self.root)

    def delete_node(self, value, key=None):
        def __replace(root):
            if root.right is None:
                #print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                #print('seguir buscando nodo par remplazar a la dercha')
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
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)
        while pendientes.size() > 0:
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

    def where(self, predicate) -> list:
        result = None
        temp = list()
        def __where(root, predicate):
            if root is not None:
                if predicate(root.value) == True:
                    temp.append(root.value)
                __where(root.left, predicate)
                __where(root.right, predicate)
            return temp
            
        if self.root is not None:
            result = __where(self.root, predicate)
        return result

    def select(self, function, sweep="inorden"):
        
        # ! PRE-ORDEN
        def __select_preorden(root, fn):
            if root is not None:
                res = fn(root.value)
                if res is not None:
                    root.value = res
                __select_preorden(root.right, fn)
                __select_preorden(root.left, fn)
            return root
        
        # ! POS-ORDEN
        def __select_posorden(root, fn):
            if root is not None:
                __select_posorden(root.right, fn)
                res = fn(root.value)
                if res is not None:
                    root.value = res
                __select_posorden(root.left, fn)
            return root
        
        # ! IN-ORDEN
        def __select_inorden(root, fn):
            if root is not None:
                __select_inorden(root.left, fn)
                res = fn(root.value)
                if res is not None:
                    root.value = res
                __select_inorden(root.right, fn)
            return root
        
        if self.root is not None:
            if sweep.lower() == "inorden":
                self.root = __select_inorden(self.root, function)
            elif (sweep.lower() == "posorden"):
                self.root = __select_posorden(self.root, function)
            elif (sweep.lower() == "preorden"):
                self.root = __select_preorden(self.root, function)
            else:
                raise ValueError(f"Nombre de barrido {sweep} incorrecto")          
    
    def update(self, seek, key, patche:dict):
        def __change(root, seek, key, patche):
            if root is not None:
               if (seek == root.value[key]):
                   root.value.update(patche)

            __change(root.left, seek, key, patche)        
            __change(root.right, seek, key, patche)        
            return root
        

        if self.root.key in list(patche.keys()):
            raise ValueError("No se puede modificar la clave principal")
        if self.root is not None:
            self.root = __change(self.root, seek, key, patche)

    def forest(self, tree1, tree2, key_compare, key_insert):
        def __forest(root, tree1, tree2, key_compare, key_insert):
            if (root.left is not None):
                __forest(root.left, tree1, tree2, key_compare, key_insert)
            if (root.right is not None):
                __forest(root.right, tree1, tree2, key_compare, key_insert)
            if (root.value[key_compare]):
                tree1.insert_node(root.value, key=key_insert)
            else:
                tree2.insert_node(root.value, key=key_insert)
            return root
        
        if self.root is not None:
            self.root = __forest(self.root, tree1, tree2, key_compare, key_insert)
            
    def show_left_child(self):
        def __show_left_child(root):
            if root is not None:
                print(root.value)
                __show_left_child(root.left)
                __show_left_child(root.right)
            
        
        if self.root is not None:
            __show_left_child(self.root.left)

    def count_nodes(self) -> dict:
        resultado = {"n_nodos" : 0}
        def __count_nodes(root, resultado):
            if root is not None:
                if (root.value) and ((root.left is not None) or (root.right is not None)):
                    resultado["n_nodos"] += 1
                __count_nodes(root.left, resultado)
                __count_nodes(root.right, resultado)
        
        if self.root is not None:
            __count_nodes(self.root, resultado)
        return resultado

    

if __name__=="__main__":
    print("Hello world!")