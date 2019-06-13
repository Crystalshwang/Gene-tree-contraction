# Gene-tree-contraction
This is final project for ECE 208. Our group member is Xin Li, Sihan Wang, Yawen Zhao and Jiahao Zhu.

To evaluate the performance of aLRT with different parameters, we use Robinson-Foulds metric to calculate the distance between the estimated species tree and real species tree and compare the performance of situations with and without aLRT, and with aLRT of different parameters.

We use the preprocess_genes.py to pre-process the alignments, prune.py to prune gene trees and Visualize RF.ipynb to visualize the RF distance.

rf-200.xlsx, rf-400.xlsx include the RF distance of with support value threshold of 0, 5, 10, 20 for the entire 50 replicates.

Average.png and Scatter.png are the visualization of alignments.
