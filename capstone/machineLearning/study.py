from graphviz import *
from sklearn.datasets import load_iris
from sklearn import tree
 
from collections import Counter
from itertools import chain, combinations
 
import ast
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import graphviz
import seaborn as sns

class Node:
    def __init__(self,nodeId, label, isRoot=False,parentNode=None,
               leftNode=None,rightNode=None,isTerminal=False, 
                 attr={}):
        self.nodeId = nodeId ## 노드 식별 아이디
        self.label = label ## 노드 텍스트
        self.attr = attr ## 노드 스타일 속성
        self.isRoot = isRoot ## 루트 노드 여부
        self.parentNode = parentNode ## 부모 마디(노드)
        self.leftNode = leftNode ## 왼쪽 자식 노드(마디)
        self.rightNode = rightNode ## 오른쪽 자식 노드
        self.isTerminal = isTerminal ## 터미널 노드 여부
        self.level = 0 ## 노드가 속한 층
def visualize_tree(tree):
    def add_node_edge(tree, dot=None):
        if dot is None:
            dot = Digraph()
#             name = tree
            dot.node(name = str(tree.nodeId), label = str(tree.label), **tree.attr)

        ## left
        if tree.leftNode:
            dot.node(name=str(tree.leftNode.nodeId),label=str(tree.leftNode.label),
                    **tree.leftNode.attr) 
            dot.edge(str(tree.nodeId), str(tree.leftNode.nodeId),
                    **{'taillabel':"yes",'labeldistance':'2.5'})
            dot = add_node_edge(tree.leftNode, dot)
            
        if tree.rightNode:
            dot.node(name=str(tree.rightNode.nodeId),label=str(tree.rightNode.label),
                    **tree.rightNode.attr)
            dot.edge(str(tree.nodeId), str(tree.rightNode.nodeId),
                    **{'headlabel':" no",'labeldistance':'2'})
            dot = add_node_edge(tree.rightNode, dot)

        return dot
    
    dot = add_node_edge(tree)

    return dot
    
def RGBtoHex(vals, rgbtype=1):

    if len(vals)!=3 and len(vals)!=4:
        raise Exception("RGB or RGBA inputs to RGBtoHex must have three or four elements!")
    if rgbtype!=1 and rgbtype!=256:
        raise Exception("rgbtype must be 1 or 256!")

    #Convert from 0-1 RGB/RGBA to 0-255 RGB/RGBA
    if rgbtype==1:
        vals = [255*x for x in vals]

    #Ensure values are rounded integers, convert to hex, and concatenate
    return '#' + ''.join(['{:02X}'.format(int(round(x))) for x in vals])

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

class DecisionTree:
    def __init__(self, tree_type='classification',):
        tree_types = ['classification','regression']
        assert tree_type in tree_types, f'tree_type must be the one of the {tree_types}'
        self.tree_type = tree_type ## 트리 유형
        self.impurity_measure = None ## 불순도 측도
        self.root = None ## 트리 노드
        self.node_id = 0 ## 노드 아이디
        self.col_names = None ## 칼럼 이름
        self.col_types = None ## 변수 타입
        self.X = None ## train data X
        self.y = None ## train data y
        self.leaf_attr = None ## 끝마디 스타일 속성
    def traverseInOrder(self, node):
        res = []
        if node.leftNode != None:
            res = res + self.traverseInOrder(node.leftNode)
        res.append(node)
        if node.rightNode != None:
            res = res + self.traverseInOrder(node.rightNode)
        return res
    
    def getDepth(self, root):
        res = self.traverseInOrder(root)
        res = [abs(node.level) for node in res]
        return max(res)
    
    def getLevel(self, node, counter = 1):
        if node.parentNode is None:
            return counter
        else:
            counter += 1
            counter = self.getLevel(node.parentNode,counter)
        return counter
    def determineTypeOfCol(self,X, num_unique_values_threshold=15):
        col_types = []
        for col in X.columns:
            unique_values = X[col].unique()
            example_value = unique_values[0]
            
            if (isinstance(example_value, str)) or (len(unique_values) <= num_unique_values_threshold):
                col_types.append('categorical')
            else:
                col_types.append('continuous')
        self.col_types = col_types
    def isPure(self,y):
        if len(np.unique(y)) > 1:
            return False
        return True
    
    def impurity(self, left_y, right_y):
        y = self.y
        n = len(left_y)+len(right_y)
        
        if self.impurity_measure == 'chi2':
            try:
                label = np.unique(y)
                contingency_table = dict()
                expected_table = dict()
                for l in label:
                    temp1 = []
                    temp1.append(np.sum(left_y==l))
                    temp1.append(np.sum(right_y==l))
                    contingency_table[l] = temp1
                    temp2 = []
                    temp2.append((np.sum(left_y==l) + np.sum(right_y==l))*len(left_y)/n)
                    temp2.append((np.sum(left_y==l) + np.sum(right_y==l))*len(right_y)/n)
                    expected_table[l] = temp2
 
                observed = np.array([v for k,v in contingency_table.items()]).flatten()
                expected = np.array([v for k,v in expected_table.items()]).flatten()
                impurity_val = np.nansum(np.square(observed-expected)/expected)
            except RuntimeWarning:
                raise
        else:
            pl, pr = len(left_y)/n, len(right_y)/n
            impurity_val = pl*self.individualImpurity(left_y)+\
                            pr*self.individualImpurity(right_y)
        return impurity_val
            
    def individualImpurity(self, y):
        if self.impurity_measure == 'entropy':
            return self._entropy(y)
        elif self.impurity_measure == 'gini':
            return self._gini(y)
        elif self.impurity_measure == 'mse':
            return self._mse(y)
    
    def _entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        ps = counts / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])
    
    def _gini(self, y):
        _, counts = np.unique(y, return_counts=True)
        ps = counts / len(y)
        return np.sum([p*(1-p) for p in ps if p > 0])
    
    def _mse(self, y):
        if len(y) == 0:
            return 0
        mse = np.mean(np.square(y-np.mean(y)))
        return mse
    
    def createLeaf(self, y, tree_type):
        if tree_type == 'classification':
            classes, counts = np.unique(y, return_counts=True)
            index = counts.argmax()
            return classes[index]
        else:
            return np.mean(y)
    
    def powerset_generator(self, i):
        for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
            yield set(subset)
        
    def splitSet(self, x):
        ps = [i for i in self.powerset_generator(x) if i != set() and len(i) != len(x)]
        idx = int(len(ps)/2)
        split_set = []
        for j in range(idx):
            split_set.append(tuple(ps[j]))
        return split_set
        
    def getPotentialSplits(self,X):
        potential_splits = {}
        col_types = self.col_types
        for col_idx in range(X.shape[1]):
            unique_value = np.unique(X[:,col_idx])
            if col_types[col_idx] == 'continuous':
                potential_splits[col_idx] = unique_value
            else:
                potential_splits[col_idx] = self.splitSset(unique_value)
        return potential_splits
    
    def split(self,X, col_idx, threshold):
        X_col = X[:,col_idx]
        col_types = self.col_types
        if col_types[col_idx] == 'continuous':
            left_idx = np.argwhere(X_col<=threshold).flatten()
            right_idx = np.argwhere(X_col>threshold).flatten()
        else:
            left_idx = np.argwhere(np.isin(X_col,threshold)).flatten()
            right_idx = np.argwhere(~np.isin(X_col,threshold)).flatten()
        return left_idx, right_idx
    
    def determinBestSplit(self, X, y, potential_splits):
        best_split_column, best_split_value, opt_impurity = '', '', ''
        if self.impurity_measure in ['entropy','gini','mse']: 
            opt_impurity = np.infty
            for col in potential_splits:
                for val in potential_splits[col]:
                    left_idx, right_idx = self.split(X,col,val)
                    cur_impurity = self.impurity(y[left_idx],y[right_idx])
                    if cur_impurity <= opt_impurity:
                        opt_impurity = cur_impurity
                        best_split_column = col
                        best_split_value = val
        else:
            opt_impurity = -np.infty
            for col in potential_splits:
                for val in potential_splits[col]:
                    left_idx, right_idx = self.split(X,col,val)
                    cur_impurity = self.impurity(y[left_idx],y[right_idx])
                    if cur_impurity >= opt_impurity:
                        opt_impurity = cur_impurity
                        best_split_column = col
                        best_split_value = val
 
        return best_split_column, best_split_value, opt_impurity
    
    def fit(self,X,y,impurity_measure='entropy',min_sample=5, max_depth=5, 
            type_of_col=None, auto_determine_type_of_col=True,
            num_unique_values_threshold = 15
           ):
        '''
        impurity_measure : 불순도 측도
        min_sample : 노드가 포함해야하는 최소 샘플 개수,
        max_depth : 나무 최대 깊이 설정
        type_of_col : 변수 타입 리스트
        auto_determine_type_of_col : 변수 타입 자동 생성 여부
        num_unique_values_threshold : 범주형으로 지정할 최대 유니크 원소 개수
        '''
        self.X = X
        self.y = y
        ### 랜덤으로 칼럼 선택하는 것도 고르자. X = X[random_indices,:]
#         if type_of_col is None:
#             type_of_col = determinTypeOfCol(X)
        if auto_determine_type_of_col:
            self.determineTypeOfCol(X, num_unique_values_threshold)
        else:
            if type_of_col is None:
                raise ValueError('When auto_determine_type_of_col is False, then type_of_col must be specified')
            assert X.shape[1] == len(type_of_col), 'type_of_col has the same length of X columns'
            give_type_of_col = list(set(type_of_col))
            for toc in give_type_of_col:
                if toc != 'categorical' and toc != 'continuous':
                    raise ValueError('type_of_col must contain categorical or continuous')
            self.col_types = type_of_col
            
        tree_type = self.tree_type
        impurity_measures = ['entropy','gini','chi2'] if tree_type == 'classification' else ['mse']
        assert impurity_measure in impurity_measures,\
                f'impurity_measure must be the one of the {impurity_measures}'
        self.impurity_measure = impurity_measure
        tree_type = self.tree_type
        self.root = self._growTree(X,y,tree_type,min_sample=min_sample, max_depth=max_depth)
        
        ### assign node a style
        iod = self.traverseInOrder(self.root)
        root_node = [node for node in iod if node.nodeId == 1][0]
        root_node.isRoot = True
        ## set node level
        for nd in iod:
            nd.level = self.getLevel(nd)
        
        colors = sns.color_palette('hls', self.getDepth(self.root))
        
        ## set node level
        if tree_type == 'classification':
            leaf_color = sns.color_palette('pastel', len(np.unique(y)))
#             class_to_color = dict()
#             for i, l in enumerate(np.unique(y)):
#                 class_to_color[l] = RGBtoHex(leaf_color[i])
            leaf_attr = dict()
            for i, l in enumerate(np.unique(y)):
                leaf_attr[l] = {'shape':'box', 'color':f'{RGBtoHex(leaf_color[i])}', 
                                       'fontcolor':f'{RGBtoHex(leaf_color[i])}','peripheries':'2'}
            self.leaf_attr = leaf_attr
        for l in range(1,self.getDepth(self.root)+1):
            color = RGBtoHex(colors[l-1])
            for nd in iod:
                if nd.level == l:
                    if nd.isTerminal:
                        if tree_type == 'classification':
                            nd.attr =  leaf_attr[nd.label]
#                             nd.attr = {'shape':'box', 'color':f'{class_to_color[nd.label]}', 
#                                        'fontcolor':f'{class_to_color[nd.label]}','peripheries':'2'}
                        else:
                            nd.attr = {'shape':'box','peripheries':'2'}
                    else:
                        nd.attr = {'shape':'box','style':'filled',
                                   'fillcolor':f'{color}'}
    
    def _growTree(self, X, y, tree_type, counter=0, min_sample=5, max_depth=5):
        self.node_id += 1
        
        if counter == 0:
            global col_names
 
            col_names = X.columns
            self.col_names = X.columns
            if isinstance(X, pd.DataFrame):
                X = X.values
            if isinstance(y, pd.Series):
                y = y.values
        else:
            X = X
        if (self.isPure(y)) or (len(y) <= min_sample) or (counter == max_depth):
            leaf = self.createLeaf(y, tree_type)
            if isinstance(leaf, float):
                if not leaf.is_integer():
                    leaf = round(leaf,2)
            return Node(self.node_id, label=leaf, isTerminal=True)
 
        else:
            counter += 1
            potential_splits = self.getPotentialSplits(X)
            best_split_column, best_split_value, opt_impurity =\
                self.determinBestSplit(X, y, potential_splits)
            opt_impurity = round(opt_impurity,4)
            left_idx, right_idx = self.split(X,best_split_column,best_split_value)
            
            ## check for empty data
            if len(left_idx) == 0 or len(right_idx) == 0:
                leaf = self.createLeaf(y, tree_type)
                if isinstance(leaf, float):
                    if not leaf.is_integer():
                        leaf = round(leaf,2)
                return Node(self.node_id, label=round(leaf,4), isTerminal=True)
            
            total_sample = len(y)
            
            col_name = col_names[best_split_column]
            if self.col_types[best_split_column] == 'continuous':
                question = f'{col_name} <= {best_split_value}\n'+\
                            f'{self.impurity_measure} : {opt_impurity}\n'+\
                            f'Samples : {total_sample}'
            else:
                question = f'{col_name} in {best_split_value}\n'+\
                            f'{self.impurity_measure} : {opt_impurity}\n'+\
                            f'Samples : {total_sample}'
 
            node = Node(self.node_id, label=question)
            
            left_child = self._growTree(X[left_idx,:],y[left_idx],tree_type,counter, min_sample, max_depth)  
            right_child = self._growTree(X[right_idx,:],y[right_idx],tree_type,counter, min_sample, max_depth)
            
 
            if left_child.label == right_child.label:
                node = left_child
            else:
                node.leftNode = left_child
                node.rightNode = right_child
                left_child.parentNode = node
                right_child.parentNode = node
 
            return node
    def predict(self,X):
        return np.array([self._traverse_tree(x, self.root) for _, x in X.iterrows()])
    
    def _traverse_tree(self, x, node):
        if node.isTerminal:
            if isinstance(node.label, str):
                node.label = node.label.replace('\n','')
            return node.label
        
        question = node.label.split('\n')[0]
        
        if ' <= ' in question:
            col_name, value = question.split(' <= ')
            if x[col_name] <= float(value):
                return self._traverse_tree(x, node.leftNode)
            return self._traverse_tree(x, node.rightNode)
        else:
            col_name, value = question.split(' in ')
            if x[col_name] in ast.literal_eval(value):
                return self._traverse_tree(x, node.leftNode)
            return self._traverse_tree(x, node.rightNode)

from sklearn.datasets import load_diabetes
dataset = load_diabetes()
X2 = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
y2 = pd.DataFrame(dataset['target'], columns=['target'])

X_