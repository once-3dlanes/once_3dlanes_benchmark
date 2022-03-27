## ONCE-3DLanes: Building Monocular 3D Lane Detection

[$Fan Yan^1$](https://fudan-zvg.github.io/)	 [$Ming Nie^1$](https://fudan-zvg.github.io/)	 [$Xinyue Cai^2$](https://scholar.google.com/citations?hl=zh-CN&user=_L4ZS9MAAAAJ) 	[$Jianhua Han^2$](https://scholar.google.com/citations?hl=zh-CN&user=OEPMQEMAAAAJ) 	[$Hang Xu^2$](https://xuhangcn.github.io/) 	[$Zhen Yang^2$](https://scholar.google.com/citations?hl=zh-CN&user=tDjRkvcAAAAJ)

[$Chaoqiang Ye^2$](https://openreview.net/profile?id=~Chaoqiang_Ye1) 	[$Yanwei Fu^1$](https://yanweifu.github.io/)	$Michael Bi Mi^2$ 	[$Li Zhang^1$](https://www.robots.ox.ac.uk/~lz/)

<center><font size="5">School of Data Science, Fudan University<sup>1</sup>		</center>
<center><font size="5">Huawei Noah's Ark Lab<sup>2</sup>		</center>

<center><font size="4">CVPR 2022		</center>

<center>Paper| <a href="https://github.com/once-3dlanes/once_3dlanes_benchmark">Code</a> | Bibtex </center>

![](https://s2.loli.net/2022/03/27/fJp5UHKAv4EwBGy.png)

<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="90%" color=#987cb9 SIZE=3>

<center><font size="5"><b>Abstract</b></font></center>

We present ONCE-3DLanes, a real-world autonomous driving dataset with lane layout annotation in 3D space. Conventional 2D lane detection from a monocular image yields poor performance of following planning and control tasks in autonomous driving due to the case of uneven road. Predicting the 3D lane layout is thus necessary and enables effective and safe driving. However, existing 3D lane detection datasets are either unpublished or synthesized from a simulated environment, severely hampering the development of this field. In this paper, we take steps towards addressing these issues. By exploiting the explicit relationship between point clouds and image pixels, a dataset annotation pipeline is designed to automatically generate high-quality 3D lane locations from 2D lane annotations in 211K road scenes.
In addition, we present an extrinsic-free, anchor-free method, called SALAD, regressing the 3D coordinates of lanes in image view without converting the feature map into the bird's-eye view (BEV). 
To facilitate future research on 3D lane detection, we benchmark the dataset and provide a novel evaluation metric, performing extensive experiments of both existing approaches and our proposed method.

The aim of our work is to revive the interest of 3D lane detection in a real-world scenario. We believe our work can lead to the expected and unexpected innovations in both academia and industry.

<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="90%" color=#987cb9 SIZE=3>

<center><font size="5"><b>Results</b></font></center>

![](https://s2.loli.net/2022/03/27/disoUe472w5Xqzp.png)

![](https://s2.loli.net/2022/03/27/UcX16CSQmP3TA5f.png)

<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="90%" color=#987cb9 SIZE=3>

<center><font size="5"><b>Acknowledgment</b></font></center>

This work was supported in part by  National Natural Science Foundation of China (Grant No. 6210020439),
Lingang Laboratory (Grant No. LG-QS-202202-07), Natural Science Foundation of Shanghai (Grant No. 22ZR1407500), Shanghai Municipal Science and Technology Major Project (Grant No. 2018SHZDZX01 and 2021SHZDZX0103), Science and Technology Innovation 2030 - Brain Science and Brain-Inspired Intelligence Project (Grant No. 2021ZD0200204), MindSpore and CAAI-Huawei MindSpore Open Fund.