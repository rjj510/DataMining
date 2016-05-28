# -*- coding: utf-8 -*-
'''
Created on 2016-5-4

@author: root
'''
import dmpy.supervised.tree
import os
import numpy as np
import matplotlib.pyplot as plt


def load(force_contiguous=True):
    _winedatafile = os.path.dirname(__file__)+'/wine.data'
    data  = np.array([list(map(float,line.split(','))) for line in open(_winedatafile)])
    rows,cols = data.shape
    D = data[0:,:cols-1]
    D = D.astype(int)
    L = data[:,cols-1]
    L = L.astype(int)
    return D,L

if __name__ == '__main__' or __name__ == 'test_tree':
    print __name__
    
     # 从文件中读取训练数据
    D, L = load()
    
     # 随机生成训练数据
    #D = np.random.randint(5, size=(100, 20)) 
    #D[:50] *= 2
    #L = np.repeat((0,1), 50)
    
     # 决策树训练器ID3 , C45 , CART 可选
    criterion = 'C45'
    C = dmpy.supervised.tree.decision_tree_learner(criterion)
    
     # 根据训练集生成训练树模型
    model = C.train_tree(D, L)
    
     # 显示输出训练树模型
    #list_name = ['age','income','student','credit_rating']
    #ci_name   = ['no','yes']
    list_name = ['A0','A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19']
    ci_name   = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12']
    model.print_tree(list_name,ci_name ,outfile = '/root/workspace/DMPY/src/'+criterion+'.png')
    
     # 应用数据集进行预测
    data           = np.array([1,1,1,2,1,2,0,1,0,2,1])
    class_lable    = model.apply(data)
    print class_lable
    
     # 训练误差（再代入误差）
    apply_error , e_T_= model.apply_error(D, L)
    print "apply_error_rate=",apply_error,"e(T)=",e_T_
    
     # 悲观误差评估 
    pe = model.pessimistic_error(D, L,0.5)
    print "pessimistic_error=",pe
    
    # MDL误差评估
    mdl = model.MDL(D,L)
    print "MDL =" ,mdl  
    
    
    
    
    