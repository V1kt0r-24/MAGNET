# MAGNET - Implementation
## Meta-Path Based Attentional Graph Learning Model for Vulnerability Detection
## Introduction
Deep Learning (DL) methods based on the graph are widely used in code vulnerability detection. However, the existing studies focus on employing contextual value in the graph, which ignores the heterogeneous relations (i.e., the relations between different nodes and edges types). In addition, subject to a large number of nodes, current methods lack the ability to capture the long-range dependencies in the code graph (i.e., the relationship between distant nodes). These limitations may obstruct the learning
of vulnerable code patterns. In this paper, we propose MAGNET, a Meta-path based Attentional Graph learning model for code vulNErability deTection. We design a multi-granularity meta-path to consider the heterogeneous relations between different node and edge types to better learn the structural information in the graph. Furthermore, we propose a multi-level attentional graph neural network called MHAGNN, which considers the heterogeneous relations and exploits the long-range dependencies between distant nodes. Comprehensive experimental results on three public benchmarks show that MAGNET achieves 6.32%, 21.50% and 25.40% improvement in F1 score compared to state-of-the-art methods. These results demonstrate that MAGNET can effectively capture structural information of graph and perform well on vulnerability detection.

## Dataset
To investigate the effectiveness of MAGNET, we adopt three vulnerability datasets from these paper: 
* FFMPeg+Qemu [1]: https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF
* Chrome+Debian [2]: https://drive.google.com/drive/folders/1KuIYgFcvWUXheDhT--cBALsfy1I4utOyF

## Requirement
Our code is based on Python3 (>= 3.7). There are a few dependencies to run the code. The major libraries are listed as follows:
* torch  (==1.9.0)
* dgl  (==0.7.2)
* numpy  (==1.22.3)
* sklearn  (==0.0)
* pandas  (==1.4.1)
* tqdm

**Default settings in MAGNET**:
* Training configs: 
    * batch_size = 512 (FFMpeg+Qemu), 512 (Chrome+Debian)
    * lr = 5e-4, epoch = 100, patience = 30
    * opt ='Adam', weight_decay=1.2e-6
optim = Adam(model.parameters(), lr=5e-4, weight_decay=1.2e-6)

## Preprocessing
We use the Reveal[2]'s Joern to generate the code structure graph [here](https://github.com/VulDetProject/ReVeal). It is worth noting that the structure of the generated diagrams differs significantly between versions of Joern due to the rapidity of the iterative versions. After Joern had generated the graph, we processed it into a meta-path graph.

Or you can use the Reveal[2]'s Joern after I have fine-tuned it to suit this project under the ```Create_GGNN``` folder.

## Training Guide
The model implementation code is under the ``` Training_code``` folder. 
Hear is an example guide you can refer to for running this project.
Use ```Pre_Process_Dataset``` folder to preprocessing the dataset.

Use ```Create_GGNN/Vuld_SySe/word2vec_train.py``` to create a Word2Vec model

```
python word2vec_train.py --data_paths 'path_to_Train&Test_Json_Data'
```
After having the Word2Vec model, use ```Create_GGNN/data_processing/create_ggnn_data.py ``` to create the input for the MAGNET model

```
python create_ggnn_data.py --csv 'path_to_your_parsed' --src 'path_to_your_source_C_code' --wv 'path_to_your_model'
```

Finally, use ```Pre_Process_Dataset/createTrainTestValid.py``` to create Train, Test, Valid json for training MAGNET model.

```
python main_reveal.py --model_type 'devign/ggnn' --input_dir 'path_to_your_dataset' --log_dir 'path_to your_log'
```
## References

[1] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.
