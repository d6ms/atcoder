class AvlTree(object):

    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.balance = "Even"

    def __contains__(self, key):
        """ key in avl としてboolを返す O(logN) """
        node = self
        while node is not None:
            if node.key == key:
                return True
            if node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        return False

    def search_lower(self, key, default=None):
        """ x より小さいものの中で最も大きいものを出力 O(logN) """
        node = self
        if node.key is None:
            return default
        ans = default
        while node is not None:
            if node.key < key:
                if ans < node.key:
                    ans = node.key
                node = node.right
            elif node.key >= key:
                node = node.left
        return ans

    def search_higher(self, key, default=None):
        """ x より大きいものの中で最も小さいものを出力 O(logN) """
        node = self
        if node.key is None:
            return default
        ans = default
        while node is not None:
            if node.key > key:
                if ans > node.key:
                    ans = node.key
                node = node.left
            elif node.key <= key:
                node = node.right
        return ans

    def _double_right_rotation(self):
        tl = self.left
        self.left = tl.right.right
        tl.right.right = self  # selfはそのノード
        tlr = tl.right
        tl.right = tlr.left
        tlr.left = tl
        if tlr.balance == "Left":
            tlr.right.balance = "Right"
            tlr.left.balance = "Even"
        elif tlr.balance == "Right":
            tlr.right.balance = "Even"
            tlr.left.balance = "Left"
        elif tlr.balance == "Even":
            tlr.right.balance = "Even"
            tlr.left.balance = "Even"
        tlr.balance = "Even"
        return tlr

    def _double_left_rotation(self):
        tr = self.right
        self.right = tr.left.left
        tr.left.left = self
        trl = tr.left
        tr.left = trl.right
        trl.right = tr
        if trl.balance == "Right":
            trl.left.balance = "Left"
            trl.right.balance = "Even"
        elif trl.balance == "Left":
            trl.left.balance = "Even"
            trl.right.balance = "Right"
        elif trl.balance == "Even":
            trl.left.balance = "Even"
            trl.right.balance = "Even"
        trl.balance = "Even"
        return trl

    def _single_left_rotation(self):
        tr = self.right
        tr.balance = "Even"
        self.balance = "Even"
        self.right = tr.left
        tr.left = self
        return tr

    def _single_right_rotation(self):
        tl = self.left
        tl.balance = "Even"
        self.balance = "Even"
        self.left = tl.right
        tl.right = self
        return tl

    def replace(self, p, v):  # 親ノードpの下にある自分(self)をvに置き換える。
        if p.left == self:
            p.left = v
        else:
            p.right = v

    def insert(self, key):  # rootでのみ呼ばれる挿入
        if self.key is None:  # rootを含むrotationはしないことにする。
            self.key = key
            return self
        if key < self.key:
            if self.left is None:
                self.left = AvlTree(key)
            else:
                self.left._insertx(self, key)
        elif key > self.key:
            if self.right is None:
                self.right = AvlTree(key)
            else:
                self.right._insertx(self, key)

    def _insertx(self, p, key):  # replaceを呼ぶために一つ上の親を持っているinsert
        node = self
        s = []
        while True:
            if node.key > key:
                s.append((node, -1))
                if node.left is None:
                    node.left = AvlTree(key)
                    node = node.left
                    break
                else:
                    node = node.left
            elif node.key < key:
                s.append((node, 1))
                if node.right is None:
                    node.right = AvlTree(key)
                    node = node.right
                    break
                else:
                    node = node.right
        while len(s) != 0:
            node, direct = s.pop()
            if len(s) != 0:
                par = s[-1][0]
            else:
                par = p
            if direct == -1:
                if node.balance == "Right":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Left"
                elif node.balance == "Left":
                    if node.left.balance == "Right":
                        node.replace(par, node._double_right_rotation())
                    elif node.left.balance == "Left":
                        node.replace(par, node._single_right_rotation())
                    break
            elif direct == 1:
                if node.balance == "Left":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Right"
                elif node.balance == "Right":
                    if node.right.balance == "Left":
                        node.replace(par, node._double_left_rotation())
                    elif node.right.balance == "Right":
                        node.replace(par, node._single_left_rotation())
                    break

    def to_s(self):
        return self.key

    def left_s(self):
        if self.left is None:
            return None
        return self.left.key

    def right_s(self):
        if self.right is None:
            return None
        return self.right.key
