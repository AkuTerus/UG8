class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
    def add(self, data):
        if self.root.left is None and data%2 != 0:
            self.root.left = Node(data,self.root)
        elif self.root.right is None and data%2 == 0:
            self.root.right = Node(data,self.root)
        else:
            if data%2 != 0:
                self.root.left.insert(data)
            else:
                self.root.right.insert(data)

    def sumGanjil(self,node,ganjil=[]):
        pass

    def sumGenap(self,node,genap=[]):
        pass

    def hasilGanjil(self):
        pass
    
    def hasilGenap(self):
        pass


if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.hasilGanjil())
    print(binaryT.hasilGenap())


Buatlah sebuah method/fungsi yang dapat digunakan untuk menjumlahkan semua data ganjil yang ada dalam struktur binary tree yang dibuat. Gunakan file main.py lalu tambahkan source code buatan kalian sesuai dengan keinginan masing-masing, yang penting dapat menghitung data ganjil dan genap yang ada dalam struktur binary tree. Boleh pakai source code tree yang dijelaskan dimodul. Harus menerapkan algoritma traversal yang sudah diajarkan untuk mencari data-data tersebut

misal ada sebuah tree yang jika diprint semua node nya menghasilkan: 20 2 10 2 5. Maka, tree tersebut jika dimasukkan ke hasilGanjil akan me-return 5; jika dimasukkan ke hasilGenap akan menghasilkan 34.

## Test Case

if __name__ == '__main__':

    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.hasilGanjil())
    print(binaryT.hasilGenap())

## Output

    Jumlah data ganjil: 35
    Jumlah data genap: 28



Certainly! Below is the modified code with the requested methods to calculate the sum of odd (ganjil) and even (genap) values in the binary tree:

```python
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

class BinaryTree:
    def __init__(self):
        self.root = Node(0, None)

    def add(self, data):
        if self.root.left is None and data % 2 != 0:
            self.root.left = Node(data, self.root)
        elif self.root.right is None and data % 2 == 0:
            self.root.right = Node(data, self.root)
        else:
            if data % 2 != 0:
                self.root.left.insert(data)
            else:
                self.root.right.insert(data)

    def sumGanjil(self, node, ganjil=[]):
        if node is not None:
            if node.data % 2 != 0:
                ganjil.append(node.data)
            self.sumGanjil(node.left, ganjil)
            self.sumGanjil(node.right, ganjil)

    def sumGenap(self, node, genap=[]):
        if node is not None:
            if node.data % 2 == 0:
                genap.append(node.data)
            self.sumGenap(node.left, genap)
            self.sumGenap(node.right, genap)

    def hasilGanjil(self):
        ganjil = []
        self.sumGanjil(self.root, ganjil)
        return sum(ganjil)

    def hasilGenap(self):
        genap = []
        self.sumGenap(self.root, genap)
        return sum(genap)

if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print(f"Jumlah data ganjil: {binaryT.hasilGanjil()}")
    print(f"Jumlah data genap: {binaryT.hasilGenap()}")
```

This code defines methods `sumGanjil` and `sumGenap` for traversing the binary tree and summing the odd and even values, respectively. The `hasilGanjil` and `hasilGenap` methods then use these traversal methods to get the sums.