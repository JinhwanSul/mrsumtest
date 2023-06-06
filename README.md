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

## Mr.Sum dataset



## Most replayed crawler

Mr.Sum can grow bigger with more CC-BY videos on YouTube.

From the meta data, especially with YouTube video id, you can crawl 'Most replayed' statistics.

```
python crawler.py --vid <video_id>
```

## Preparing Mr.Sum Dataset

We provide data loader which takes h5 datasets inputs



1. given csv meta data --> youtube video id 를 가져옵니다.

2. video_id 로 most replayed 를 crawl합니다.

3. h5 만드는 코드
- video feature --> h5
- change point --> KTS
- most replayed --> gtscore
- ....

4. h5 읽어서 모델 학습하는 코드
- train
- evaluate

5. 결과
