# Mr. Sum: Large-scale Video Summarization Dataset and Benchmark

Mr. Sum is a large-scale video summarization dataset, which contains 31,892 videos selected from YouTube-8M dataset and reliable frame importance score labels aggregated from 50,000+ users per video.  

## YouTube's Most replayed statistics
Mr.Sum uses 'Most replayed' statistics on YouTube as a importance score labels.

<!-- <img src="images/most_replayed.jpeg" alt="Example of Most replayed" width="300" height="200"> -->

These are some few examples of Most replayed.
<!-- <img src="images/AC_sparta_all_gif_resized.gif" alt="Example of Soccer game Most replayed" width="200" height="250"> -->

<!-- **In this repository,**

1. We provide meta data and most replayed labels for 31,892 videos in [dataset](dataset) folder.

2. We provide Most replayed crawler enabling expansion of our dataset.

3. We provide sample codes to apply Mr.Sum dataset on a video summarization model. -->




<div style="display:flex;">
  <div style="width:40%;">
    <img src="images/most_replayed.jpeg" width="100">
  </div>
  <div style="width:60%;">
    <table style="width:100;">
      <tr>
        <td><img src="images/AC_sparta_1_gif.gif" width="100"></td>
        <td><img src="images/AC_sparta_2_gif.gif" width="100"></td>
      </tr>
      <tr>
        <td><img src="images/AC_sparta_3_gif.gif" width="100"></td>
        <td><img src="images/AC_sparta_4_gif.gif" width="100"></td>
      </tr>
    </table>
  </div>
</div>




### Update
- **2023.06.07**, Repository created.


----
## Getting Started

1. Download [YouTube-8M](https://research.google.com/youtube8m/) dataset.

2. Download [mrsum.h5](https://drive.google.com/file/d/1N_W1Z0MiN2sra2P9zhh7ZFgzN1OpHNVL/view?usp=sharing) and [metadata.csv](https://drive.google.com/file/d/1GhUSEzPif5h2sUtHsSK9zn4qlEqeKcgY/view?usp=sharing) place it under `dataset` folder.

3. Install software packages.
    ```
    pip -r requirments.txt ??
    ```
4. Now you are ready!

----
## Complete Mr.Sum Dataset

You need four fields on your `mrsum.h5` to prepare.

1. `features`: Video frame features from YouTube-8M dataset.
2. `gtscore`: Most replayed statistics in normalized 0 to 1 score.
3. `change_points`: Shot boundary information obtained with [Kernel Temporal Segmentation](https://github.com/TatsuyaShirakawa/KTS) algorithm.
4. `gtsummary`: Ground truth summary obtained from by solving 0/1 knapsack algorithm on shots.

We already provide three fields, `gtscore`, `change_points`, and `gtsummary`, inside `mrsum.h5`. 

After downloading YouTube-8M dataset, you can add `features` field using
```
python preprocess/preprocess.py
```

Please read [DATASET.md](dataset/DATASET.md) for more details about the Mr.Sum.

----
## Apply Mr.Sum on your summarization model

We provide sample code for training and evaluating a summarization model on Mr.Sum.

Coming Soon!

----
## License
This dataset is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/) following the YouTube-8M dataset. All the Mr.Sum dataset users must comply with [YouTube Terms of Service](https://www.youtube.com/static?template=terms) and [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service#agreement).


----
