# NEURO140_FinalProject

BERT_Models.ipynb provides code for the following BERT models. Even-numbered models were trained and tested on concatenated reviews. Extractive summarization using a Cosine-similarity matrix was used to create concatenated reviews by extracting a maximum of three sentences from each of the original reviews.

Models 1 and 2: BERT model trained and tested on Amazon reviews, using a train-test-validation split of 70-15-15

Models 3 and 4: BERT model trained and tested on Goodreads reviews, using a train-test-validation split of 70-15-15. Training data are oversampled so that 50% are negative

Models 5 and 6: BERT model trained on Amazon reviews and tested on Goodreads reviews

Subsets of the Amazon and Goodreads datasets are provided. Due to file size constraints in Github, the Amazon and Goodreads subsets contain roughly 15K rows each. These subsetted datasets already contain columns containing the cleaned reviews (with any target information such as '2 stars' removed), as well as columns for the concatenated reviews. Functions to perform extractive summarization and remove target information from the reviews are provided in ExtractiveSummarization.py and Data_Preproc.py, respectively. The original datasets can be found here:

https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/reviews

https://www.kaggle.com/datasets/bittlingmayer/amazonreviews

The main file, BERT_Models.ipynb, was executed in Google Colab Pro.
