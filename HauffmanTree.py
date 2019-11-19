import cv2
import numpy as np
import os
import copy

from matplotlib import pyplot as plt

def str_to_dict(str):
    freqDict = dict()
    for x in str:
        if x in freqDict:
            freqDict[x] += 1
        else: freqDict[x] = 1
    return freqDict


def create_full_image_dict(image):

    # Creating a dictionary with a key for each unique (r,g,b) combination in image
    colorDictionary = dict()
    imageTuple = np.shape(image)
    (height, width, color) = imageTuple
    for x in range(height):
        for y in range(width):
            if f"{image[x][y][0]},{image[x][y][1]},{image[x][y][2]}" not in colorDictionary:
                colorDictionary[f"{image[x][y][0]},{image[x][y][1]},{image[x][y][2]}"] = 1
            else:
                colorDictionary[f"{image[x][y][0]},{image[x][y][1]},{image[x][y][2]}"] += 1
    return colorDictionary

def tuple_list(freqDict):
    freqList = [(v, k) for k, v in freqDict.items()]
    freqList.sort()
    return freqList

class TreeNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root

    def __repr__(self):
        if len(self) == 2:
            return str(self)
        else:
            return str(self.children())

    def __len__(self):
        if len(self.children()) == 1:
            return 1
        elif len(self.children()) == 2:
            return len(self.left) + len(self.right)

    def children(self):
        return (self.left, self.right)

def myRoot(lstOrNode):
    if type(lstOrNode) == tuple:
        return lstOrNode[0]
    else: return lstOrNode.root

def do_single_merge(rec_frequencies):
    rec_frequencies.sort(key=lambda x: myRoot(x))
    if len(rec_frequencies) == 1:
        return rec_frequencies
    else:
        root = myRoot(rec_frequencies[0]) + myRoot(rec_frequencies[1])
        rec_frequencies.append(TreeNode(rec_frequencies.pop(0), rec_frequencies.pop(0), root))

def create_tree_recursivly(rec_frequencies):
    rec_frequencies.sort(key=lambda x: myRoot(x))
    print(rec_frequencies)

    if len(rec_frequencies) == 1:
        return rec_frequencies
    else:
        root = myRoot(rec_frequencies[0]) + myRoot(rec_frequencies[1])
        rec_frequencies.append(TreeNode(rec_frequencies.pop(0), rec_frequencies.pop(0), root))
        create_tree_recursivly(rec_frequencies)

    return rec_frequencies

# def create_tree_iterativly(it_frequencies, solvedTree = []):
#     it_frequencies = copy.deepcopy(it_frequencies)
#     # print(it_frequencies)
#     while True:
#         solvedTree.sort(key=lambda x: myRoot(x))
#         print(iterative_frequencies)
#         print(solvedTree)
#         print("\n")
#         if len(it_frequencies) == 1:
#             # solvedTree = solvedTree
#             solvedTree = [(solvedTree[0], it_frequencies[0])]
#             return solvedTree
#             break
#         else:
#             root = myRoot(it_frequencies[0]) + myRoot(it_frequencies[1])
#             solvedTree.insert(0, TreeNode(it_frequencies.pop(0), it_frequencies.pop(0), root))

def print_tree(tree, depth = 0, path = None):
    if path == None:
        path = ""
    if (len(tree)) == 2:
        print(path + str(tree))
    else:
        print_tree(tree.right, depth+1, path + "0")
        print_tree(tree.left, depth+1, path + "1")

def print_image_tree():
    url = "SampleJPGImage_50kbmb.jpg"
    image = cv2.imread(url, 1)
    colorDictionary = create_full_image_dict(image)
    # frequencies = tuple_list(colorDictionary)
    # tree = create_tree_recursivly(frequencies)
    # print_tree(tree)




def print_text_tree():
    textDictionary = str_to_dict("AAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBccfvhjfyukhfctfgdc jhgfvyghc")
    frequencies = tuple_list(textDictionary)
    # tree = create_tree_recursivly(frequencies)
    # print_tree(tree[0])




if __name__ == "__main__":
    print_image_tree()
    # print_text_tree()









