# SMS Spam Detector

A machine learning web app that classifies English SMS messages
as Spam or Not Spam.

## Live Demo

https://ashok-sms-spam-detector.streamlit.app

## Features

- Enter a message and get a prediction
- Try built-in normal and spam examples
- Clear messages and results
- Colorful Streamlit interface
- Empty-input validation

## Technologies

Python, Pandas, scikit-learn, Joblib, and Streamlit.

## Machine Learning Approach

- Removed 403 duplicate rows, leaving 5,171 messages.
- Split the cleaned dataset into 80% training and 20% testing.
- Converted text into TF-IDF features.
- Trained a Multinomial Naive Bayes classifier.
- Used five-fold cross-validation on training data to select
  settings based on spam F1 score.
- Best settings: alpha=0.1 and ngram_range=(1, 2).

## Evaluation

Results on 1,035 held-out test messages:

| Metric | Result |
|---|---:|
| Accuracy | 98.55% |
| Spam precision | 99.15% |
| Spam recall | 89.31% |
| Spam F1 score | 93.98% |
| Spam detected | 117 of 131 |
| Spam missed | 14 |
| Normal messages incorrectly flagged | 1 |

These results describe this dataset split and do not guarantee
the same performance on new messages.

## Run Locally

Use Python 3.14, matching the development environment.

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -r requirements.txt
    python -m streamlit run app.py

The included spam_model.joblib contains the trained text
vectorizer and classifier.

## Dataset and Retraining

Dataset: UCI SMS Spam Collection
Creators: Tiago Almeida and José Hidalgo

https://archive.ics.uci.edu/dataset/228/sms+spam+collection

Dataset license: CC BY 4.0.
Dataset DOI: https://doi.org/10.24432/C5CC84

The dataset is not included in this repository.
To retrain:

1. Download and extract the dataset.
2. Place SMSSpamCollection inside a folder named data.
3. Run: python explore_data.py
4. Run: python train_model.py

## Limitations

- Intended for English SMS messages.
- Can miss spam or incorrectly flag normal messages.
- Does not automatically read or block phone messages.
- A Not Spam prediction does not guarantee safety.

## Author

ASHOK ANDRA
