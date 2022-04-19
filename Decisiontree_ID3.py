## 코드 메모
# dropna() 메소드가 결측치를 삭제한다는 의미
# 엔트로피는 데이터 셋의 불순도를 측정.
# 엔트로피가 크게 나오는 이유는 tree status 가 많은 값을 가지기 때문
# 정보이득은 상위 노드의 엔트로피에서 하위 노드의 엔트로피를 뺀 값.


import pandas as pd
import numpy as np
#print("pandas version " + pd.__version__)
data = pd.DataFrame({"temp":["True","True","True","True","True","True","True","True","True","True","True","False","False","False","False","False","False","False","False","True","True","True"],
                    "humi":["True","True","True","True","True","True","True","False","False","False","False","True","True","True","True","False","False","False","False","True","True","True"],
                    "dirthumi":["True","True","True","True","True","False","False","True","True","False","False","True","True","False","False","True","True","False","False","True","True","True"],
                    "lux":["True","False","True","True","True","True","False","True","False","True","False","True","False","True","False","True","False","True","False","True","True","True"],
                    #"tree_status":["good","good","good","good","good","good","poor","good","poor","poor","poor","good","poor","poor","poor","poor","poor","poor","poor","good","good","good"]},
                    "tree_status":["good","NEl","good","good","good","NEdh","NEdh""NEl","NEh","NEh""NEl","NEh""NEdh","NEh""NEdh""NEl","NEt","NEt""NEl","NEt""NEdh","NEt""NEdh""NEl","NEt""NEh","NEt""NEh""NEl","NEt""NEh""NEdh","NEt""NEh""NEdh""NEl","good","good","good"]},#NE 는 not enough임 dh 는 dirthumi, h=humi, l=lux
                    columns=["temp","humi","dirthumi","lux","tree_status"])
    
features = data[["temp","humi","dirthumi","lux"]]

target = data["tree_status"]

#print(data)
#엔트로피 구하는 함수
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts = True)
    entropy = -np.sum([(counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

#print('H(x) = ', round(entropy(target), 5))

# 정보이득을 계산 하는 함수. 인자는 차례대로 데이터셋,  노드의 이름, 타깃 결과, tree_status를 넣음
def InfoGain(data,split_attribute_name,target_name):
 
    # 전체 엔트로피 계산
    total_entropy = entropy(data[target_name])
    #print('Entropy(D) = ', round(total_entropy, 5), '\n')
    
    # 가중 엔트로피 계산
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*
                               entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name])
                               for i in range(len(vals))])
    #print('H(', split_attribute_name, ') = ', round(Weighted_Entropy, 5), '\n')
 
    
    # 정보이득 계산
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain
 

# ID3알고리즘 사용. 트리의 성장을 시켜줌 3가지 기준에 따라서
def ID3(data,originaldata,features,target_attribute_name,parent_node_class = None):
 
    # 중지기준 정의
 
    # 1. 대상 속성이 단일값을 가지면: 해당 대상 속성 반환
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
 
    # 2. 데이터가 없을 때: 원본 데이터에서 최대값을 가지는 대상 속성 반환
    elif len(data)==0:
        return np.unique(originaldata[target_attribute_name])\
               [np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]
 
    # 3. 기술 속성이 없을 때: 부모 노드의 대상 속성 반환
    elif len(features) ==0:
        return parent_node_class
 
    # 트리 성장
    else:
        # 부모노드의 대상 속성 정의(예: Good)
        parent_node_class = np.unique(data[target_attribute_name])\
                            [np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        
        # 데이터를 분할할 속성 선택
        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        # 트리 구조 생성
        tree = {best_feature:{}}
        
        # 최대 정보이득을 보인 기술 속성 제외
        features = [i for i in features if i != best_feature]
        
        # 가지 성장
        for value in np.unique(data[best_feature]):
            # 데이터 분할. dropna(): 결측값을 가진 행, 열 제거
            sub_data = data.where(data[best_feature] == value).dropna()
            
            # ID3 알고리즘
            subtree = ID3(sub_data,data,features,target_attribute_name,parent_node_class)
            tree[best_feature][value] = subtree
            
        return(tree)
# 넘파이 함수
# numpy.unique: 고유값 반환
#print('numpy.unique: ', np.unique(data["tree_status"], return_counts = True)[1])
# numpy.max: 최대값 반환
#print('numpy.max: ', np.max(np.unique(data["tree_status"], return_counts = True)[1]))
# numpy.argmax: 최대값이 위치한  인덱스 반환
#print('numpy.argmax: ', np.argmax(np.unique(data["tree_status"], return_counts = True)[1]))

print('InfoGain( temp ) = ', round(InfoGain(data, "temp", "tree_status"), 5), '\n')
print('InfoGain( humi ) = ', round(InfoGain(data, "humi", "tree_status"), 5), '\n')
print('InfoGain( lux ) = ', round(InfoGain(data, "lux", "tree_status"), 5), '\n')
print('InfoGain( dirthumi ) = ', round(InfoGain(data, "dirthumi", "tree_status"), 5))


tree = ID3(data, data, ["temp","humi","dirthumi","lux"], "tree_status")
import pprint
pprint.pprint(tree)

#input = {"False", "True", "True", "True"}

print(tree['temp']['True']['humi']['False']['dirthumi']['True']['lux']['False'])