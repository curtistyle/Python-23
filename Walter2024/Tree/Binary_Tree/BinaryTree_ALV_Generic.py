from cola import Queue

class Node:
    def __init__(self, value, left=None, right=None, key=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.key = key
        self.height = 0

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def height(self, root):
        """Altura actual del nodo"""
        if root is None:
            return -1
        else:
            return root.height
        
    def update_height(self, root):
        """Actualiza la altura del Nodo"""
        if root is not None:
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura izq {left_height} altura der {right_height}')
            # print(f'altura de {root.value} es {root.height}')
        
    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root
    
    def balancing(self, root):
        if root is not None:
            # ! key is None
            if self.height(root.left) - self.height(root.right) == 2:
                #print('desbalanceado a la izquierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    #print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    #print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                #print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    #print('rotar simple izquierda')
                    root = self.simple_rotation(root, False)
                else:
                    #print('rotar doble izquierda')
                    root = self.double_rotation(root, False)
        return root
    
    def insert_node(self, value, key=None):
        def __insert_by_key(root, value, key):
            if root is None:
                return Node(value, key=key)
            elif value[key] < root.value[key]:
                root.left = __insert_by_key(root.left, value, key)
            else:
                root.right = __insert_by_key(root.right, value, key)
                
            root = self.balancing(root)
            self.update_height(root)
            return root

        def __insert(root, value):
            if root is None:
                return Node(value)
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
    
    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.key is None:
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
                            # return root, value_delete
                        root = self.balancing(root)
                        self.update_height(root)
                else:
                    if root.value[root.key] > value:
                        # print(f'buscar  a la izquierda de {root.value}')
                        root.left, value_delete = __delete(root.left, value)
                    elif root.value[root.key] < value:
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
                            # return root, value_delete
                        root = self.balancing(root)
                        self.update_height(root)
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value
    
    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)    
                
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

    def update_any(self, seek, key, patche:dict):
        """Actualiza un Nodo de tipo `dict()`"""
        def __update_any(root, seek, key, patche):
            if root is not None:
                if (seek == root.value[key]):
                    root.value.update(patche)
                __update_any(root.left, seek, key, patche)        
                __update_any(root.right, seek, key, patche)        
            return root
        
        if self.root.key in list(patche.keys()):
            raise ValueError("No se puede modificar la clave principal")
        if self.root is not None:
            self.root = __update_any(self.root, seek, key, patche)
    
    def group_and_count(self, key):
        count = {}
        def __group_and_count(root, key):
            if root is not None:
                value = root.value[key]
                if value is not None:
                    if count.get(value) == None:
                        count[value] = 1
                    else:
                        count[value] = count[value] + 1

                __group_and_count(root.left, key)
                __group_and_count(root.right, key)
        
        if self.root is not None:
            __group_and_count(self.root, key)
        
        def _item(value):
            return value[1]
        in_orden = dict(sorted(count.items(), key=_item, reverse=True))
        
        return in_orden
            
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