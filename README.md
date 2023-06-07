# Mr.Sum: Large-scale Video Summarization Dataset and Benchmark

Mr.Sum contains 31,892 videos selected from [YouTube-8M](https://research.google.com/youtube8m/). 

Mr.Sum uses 'Most replayed' statistics on YouTube as a importance score labels.
<img src="images/most_replayed.jpeg" alt="Example of Most replayed" width="300" height="200">

They are aggregated statistics from more than 50,000 watchers which makes this labeling reliable.

These are some few examples.
<img src="images/AC_sparta_all_gif_resized.gif" alt="Example of Soccer game Most replayed" width="1000" height="500">


**In this repository,**

1. We provide meta data and most replayed labels for 31,892 videos in [dataset](dataset) folder.

2. We provide Most replayed crawler enabling expansion of our dataset.

3. We provide sample codes to apply Mr.Sum dataset on a video summarization model.

----
## Getting Started

1. Install [YouTube-8M](https://research.google.com/youtube8m/) dataset.
2. Download [mrsum.h5](https://drive.google.com/file/d/1N_W1Z0MiN2sra2P9zhh7ZFgzN1OpHNVL/view?usp=sharing) and place it inside `dataset` folder
3. Install software packages using
```
pip -r requirments.txt ??
```
4. Now you are ready!

----
## Prepare Mr.Sum dataset

### Most replayed crawler

From the meta data, especially with YouTube video id, you can crawl 'Most replayed' statistics.

```
python crawler/crawler.py --vid <video_id>
```

### Complete Mr.Sum Dataset

You need four fields on your h5 dataset to prepare the dataset.

1. `features`: Video frame features from YouTube-8M dataset.
2. `gtscore`: Most replayed statistics in normalized 0 to 1 score.
3. `change_points`: Shot boundary information obtained with [Kernel Temporal Segmentation](https://github.com/TatsuyaShirakawa/KTS) algorithm.
4. `gtsummary`: Ground truth summary obtained from applying 0/1 knapsack algorithm on shots.

We already provide three fields: `gtscore`, `change_points`, and `gtsummary` inside `mrsum.h5`. 

You can add `features` field using
```
python preprocess/preprocess.py
```
----

## Apply Mr.Sum on your summarization model

We provide sample code for training and evaluating a summarization model on Mr.Sum.

4. h5 읽어서 모델 학습하는 코드
- train
- evaluate

5. 결과

## Mr.Sum dataset framework
