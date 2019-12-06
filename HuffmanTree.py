import cv2
import numpy as np
import copy
import zlib

def str_to_dict(str):
    freqDict = dict()
    for x in str:
        if x in freqDict:
            freqDict[x] += 1
        else: freqDict[x] = 1
    return freqDict

def create_full_image_dict(image):

    colorDictionary = dict()
    imageTuple = np.shape(image)
    (height, width, color) = imageTuple
    for x in range(height):
        for y in range(width):

            if tuple(image[x][y]) not in colorDictionary:
                colorDictionary[tuple(image[x][y])] = 1
            else:
                colorDictionary[tuple(image[x][y])] += 1
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
        return rec_frequencies

def create_tree(dictionary):
    frequencies = tuple_list(dictionary)
    while True:

        if len(frequencies) == 1:
            break
        else:
            frequencies = do_single_merge(frequencies)
    return frequencies[0]

def print_tree(tree, path = None):
    if path == None:
        path = ""
    if (len(tree)) == 2:
        print(path + str(tree))
    else:
        print_tree(tree.right, path + "0")
        print_tree(tree.left, path + "1")

def addBin(sofar, new):
    if sofar == 0:
        return new
    else:
        return 10*sofar + new

def encode_moves(tree, path = None, result = dict()):
    if path == None:
        path = 0
    if (len(tree)) == 2:
        result[tree[1]] = path
    else:
        encode_moves(tree.right, addBin(path, 0))
        encode_moves(tree.left, addBin(path, 1))
        return(result)

def encode_moves_poorly(tree, path = None, result = dict()):
    if path == None:
        path = ""
    if (len(tree)) == 2:
        result[str(tree[1])] = path
    else:
        encode_moves_poorly(tree.right, path + "0")
        encode_moves_poorly(tree.left, path + "1")
        return(result)

def return_image_tree():
    url = "SampleJPGImage_50kbmb.jpg"
    image = cv2.imread(url, 1)
    colorDictionary = create_full_image_dict(image)
    tree = create_tree(colorDictionary)
    encode_moves(tree[0])

def compress(image, scale = 9):
    if len(image):
        return zlib.compress(image, scale)

    new = np.ndarray(shape=(len(image), len(image[0])))
    for x in range(len(image)):
        for y in range(len(image[0])):
            # print(key[str(tuple(image[x][y]))])
            new[x][y] = key[str(tuple(image[x][y]))]
    return new.astype(int)

def decompress(compressedImage, decompressKey = None):

    if len(compressedImage):    #zlib Compression
        return zlib.decompress(compressedImage)
    for x in range(len(compressedImage)):
        for y in range(len(compressedImage[0])):
            print(str(compressedImage[x][y]))


def invert_key(compression_key):
    inv_map = {v: k for k, v in compression_key.items()}
    return inv_map


# url = "Frames/lilpeg.jpg"
# image = cv2.imread(url)
# dic = create_full_image_dict(image)
# tree = create_tree(dic)
# key = encode_moves_poorly(tree)
#
#
# compressedImage = compress(image)


# print(compressedImage)
# inverted_key = invert_key(key)
# print(inverted_key)
#
# decompress(compressedImage, inverted_key)



