# Early-Detection-of-Misinformation
Project Description

Title: AI-Based Early Detection of Misinformation in Social Media Posts

Overview:
Misinformation spreads on social media faster than manual fact-checking can handle. This project builds an AI system that estimates how likely a post is to be misinformation, using only the information available soon after it is published, before it goes viral.

How it works:
The system combines four types of signals instead of relying on text alone:

Text features: cleaned text, TF-IDF, sentiment and writing style (sensational words, excessive capitals, clickbait patterns)
Semantic embeddings: BERT or RoBERTa converts each post into a vector that captures its meaning
Engagement features: likes, shares, replies and how fast they arrive
Source features: account age, followers, follower-to-following ratio, verification status

These are combined in a multimodal fusion model built with PyTorch. It is compared against baseline models (Logistic Regression, Random Forest, SVM) built with Scikit-learn.

Data: the PHEME dataset, which contains tweets, replies, timestamps and account details for 9 breaking-news events. The model is evaluated by event (leave-one-event-out) to give honest results.

Early detection: features are built only from the first few minutes after posting (for example 5, 15 or 30 minutes). Performance is plotted against the time window to show how early the model works.

Explainability: SHAP and LIME show which words and features influenced each prediction, so the result can be understood and trusted.

Output: the user pastes a post (and optionally engagement and account details) into a Streamlit app, and gets a misinformation probability from 0 to 1 with an explanation. The app can also accept video by converting speech to text with Whisper.

Evaluation: accuracy, precision, recall, F1-score and ROC-AUC, plus an ablation study and a comparison with text-only baselines.

Expected outcome: a trained multimodal model that outperforms text-only baselines, with explanations, a working demo, a deployed link and full documentation.

Limitation: the score is a risk estimate based on patterns, not proof that a post is true or false.
