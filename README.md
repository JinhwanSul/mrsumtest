# Mr.Sum: Large-scale Video Summarization Dataset and Benchmark

Mr.Sum contains 31,892 videos selected from [YouTube-8M](https://research.google.com/youtube8m/). 

Mr.Sum uses 'Most replayed' statistics on YouTube as a importance score labels.
<img src="images/most_replayed.jpeg" alt="Example of Most replayed" width="300" height="200">

They are aggregated statistics from more than 50,000 watchers which makes this labeling reliable.

**In this repository,**

1. We provide meta data and most replayed labels for 31,892 videos in [dataset](dataset) folder.

2. We provide Most replayed crawler enabling expansion of our dataset.

3. We provide sample codes to apply Mr.Sum dataset on a video summarization model.

----

## How to create & use Mr.Sum dataset

### Most replayed crawler

From the meta data, especially with YouTube video id, you can crawl 'Most replayed' statistics.

```
python crawler/crawler.py --vid <video_id>
```

### Preparing Mr.Sum Dataset

You need four fields on your h5 dataset to prepare the dataset.

1. `features`: Video frame feature you can obtain from YouTube-8M dataset.
2. `gtscore`: Most replayed statistics in normalized 0 to 1 score.
3. `change_points`: Shot boundary information obtained with [Kernel Temporal Segmentation](https://github.com/TatsuyaShirakawa/KTS) algorithm.
4. `gtsummary`: Ground truth summary obtained from applying 0/1 knapsack algorithm on shots.

We already provide three fields: `gtscore`,`change_points`, and `gtsummary` inside [mrsum.h5](dataset/mrsum.h5-fake). 

You can add `features` field using
```
python preprocess/preprocess.py
```


### Apply Mr.Sum on your summarization model

We provide sample code for training and evaluating a summarization model.

3. h5 만드는 코드
- video feature --> h5
- change point --> KTS
- most replayed --> gtscore
- ....

4. h5 읽어서 모델 학습하는 코드
- train
- evaluate

5. 결과

## Mr.Sum dataset framework