# ONCE-3DLanes

[<span style='font-size: 20px'>Project Page</span>](https://once-3dlanes.github.io/) **|** [<span style='font-size: 20px'>Paper</span>]() **|** [<span style='font-size: 20px'>Data</span>](https://drive.google.com/file/d/1-blzGV6Q0R-6aa0dsRHjR9kKiA5o5bqv/view)



>ONCE-3DLanes: Building Monocular 3D Lane Detection
>
><a href="https://fudan-zvg.github.io/"> Fan Yan<sup>1</sup></a>  <a href="https://fudan-zvg.github.io/"> Ming Nie<sup>1</sup></a>  <a href="https://scholar.google.com/citations?hl=zh-CN&user=_L4ZS9MAAAAJ"> Xinyue Cai<sup>2</sup></a>  <a href="https://scholar.google.com/citations?hl=zh-CN&user=OEPMQEMAAAAJ"> Jianhua Han<sup>2</sup></a>  <a href="https://xuhangcn.github.io/"> Hang Xu<sup>2</sup></a>  <a href="https://scholar.google.com/citations?hl=zh-CN&user=tDjRkvcAAAAJ"> Zhen Yang<sup>2</sup></a> 
>
><a href="https://openreview.net/profile?id=~Chaoqiang_Ye1"> Chaoqiang Ye<sup>2</sup></a>  <a href="https://yanweifu.github.io/"> Yanwei Fu<sup>1</sup></a>   <a href=""> Michael Bi Mi<sup>2</sup></a> <a href="https://www.robots.ox.ac.uk/~lz/"> Li Zhang <sup>1</sup></a> 
>
><center><font size="3"><sup>1</sup>School of Data Science, Fudan University	</center>
><center><font size="3"><sup>2</sup>Huawei Noah's Ark Lab		</center>

<img src="C:\Users\Ivan\Desktop\cvpr\once3dlanes_example.png" style="zoom:80%;" />



## Introduction

We present **ONCE-3DLanes**, a real-world autonomous driving dataset with lane layout annotation in 3D space. Conventional 2D lane detection from a monocular image yields poor performance of following planning and control tasks in autonomous driving due to the case of uneven road. Predicting the 3D lane layout is thus necessary and enables effective and safe driving. However, existing 3D lane detection datasets are either unpublished or synthesized from a simulated environment, severely hampering the development of this field. In this paper, we take steps towards addressing these issues. By exploiting the explicit relationship between point clouds and image pixels, a dataset annotation pipeline is designed to automatically generate high-quality 3D lane locations from 2D lane annotations in 211K road scenes. In addition, we present an extrinsic-free, anchor-free method, called **SALAD**, regressing the 3D coordinates of lanes in image view without converting the feature map into the bird's-eye view (BEV).  To facilitate future research on 3D lane detection, we benchmark the dataset and provide a novel evaluation metric, performing extensive experiments of both existing approaches and our proposed method.

The aim of our work is to revive the interest of 3D lane detection in a real-world scenario.
We believe our work can lead to the expected and unexpected innovations in both academia and industry.

## More Details

You can refer to [here](https://once-3dlanes.github.io/3dlanes/) to get more details of our dataset.

## Install

- python 3.6, pytorch 1.4,  CUDA 10.2

```python
git clone https://github.com/once-3dlanes/once_3dlanes_benchmark.git
conda create -n once3dlanes python=3.6.9
conda activate once3dlanes
pip install -r requirements.txt
```

## Data Preparation

- You can refer to [here](https://once-3dlanes.github.io/3dlanes/) to download the official ONCE-3DLanes dataset.

- The `frame.json` file of predicted 3D lanes should be organized like this:

```python
{
  "lanes":[
    # One lane 
    [ 
      # The [x, y, z] coordinates of key points in the lane are listed as follows.
      [-2.475, 1.871, 31.082],
      [-2.547, 1.854, 28.394],        
      ...
    ]
    # Other lanes
    ...
    ]
}
```

- The final data structure should be:

```
once_3dlanes_benchmark
├── ONCE_3DLanes
│   ├── train
│   │   │── sequence
│   │   │   │──cam01 
|   |   |   |	|──frame.json
|   |   |   |	|──...
│   ...
├── pred_dir
│   ├── sequence
│   │   │   │──cam01 
|   |   |   |	|──frame.json
|   |   |   |	|──...
│   ├── ...
├── ...
├── eval.py
├── eval.sh
```

## Evaluation

You should refer to the `eval.sh` and change your `root`、 `gt_dir` and `pred_dir` path.

Take the final data structure for example, the `root = './once_3dlanes_benchmark'`, `'gt_dir = ONCE_3DLanes/train'`and the `pred_dir = 'pred_dir'`.

```python
bash eval.sh
```

## Results

![](https://s2.loli.net/2022/04/21/klh8yCZnW1bX67f.png)

![](https://s2.loli.net/2022/04/21/xRrYPdJacmEbQyB.png)

## Citation

Please cite this paper in your publications if it helps your research:

```
@InProceedings{yan2022once,
  title={ONCE-3DLanes: Building Monocular 3D Lane Detection},
  author= {Yan, Fan and Nie, Ming and Cai, Xinyue and Han, Jianhua and Xu, Hang and Yang, Zhen and Ye, Chaoqiang and Fu, Yanwei and Michael, Bi Mi and Zhang, Li},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2022},
}
```

