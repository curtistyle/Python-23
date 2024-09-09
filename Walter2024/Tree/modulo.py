def by_level(self):
    pendientes = Queue()
    if self.root is not None:
        pendientes.arrive(self.root)
    while pendientes.size() > 0:
        node = pendientes.attention()
        print(node.value)
        # * si el hijo izquierdo no esta vacio
        if node.left is not None:
            pendientes.arrive(node.left)
        # * si el hijo derecho no esta vacio
        if node.right is not None:
            pendientes.arrive(node.right)