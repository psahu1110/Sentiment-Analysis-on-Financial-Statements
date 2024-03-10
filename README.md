# Project Title: Sentiment Analysis on Financial Statements
Overview:
This project focuses on sentiment analysis of financial statements, categorizing sentiments as positive, negative, or neutral. The dataset used for this project was provided by the training instructor.

Process Overview:
1. Dataset Import-
The dataset was imported for analysis. Descriptive statistics were obtained using Pandas functions such as head, tail, and shape.

2. Data Cleaning-
Data was transformed using label encoding for further analysis.
Checked and handled missing values and duplicates in the dataset.

3. Exploratory Data Analysis (EDA)-
Conducted exploratory data analysis to understand the distribution of sentiments.
Visualized sentiment counts using plots, identifying an imbalance in the dataset.

4. Handling Imbalanced Data-
Recognized the imbalance issue and applied strategies to address it for better model performance.

5. Natural Language Processing (NLP) with NLTK-
Utilized the NLP library NLTK for text processing.
Implemented text preprocessing tasks, including tokenization, stopwords removal, punctuation removal, and stemming.

6. Visualization-
Created Word Clouds for each sentiment to visually represent the most frequently used words in the text.

7. Model Building-
Employed TF-IDF for feature extraction.
Split the data and applied various machine learning algorithms, including:
Support Vector Classifier (SVC)
Multinomial Naive Bayes
Gaussian Naive Bayes
Bernoulli Naive Bayes
Logistic Regression
K-Nearest Neighbors
Decision Tree
Random Forest

8. Model Evaluation-
Analyzed the accuracy of each algorithm and fine-tuned parameters for optimal results.
Evaluated metrics such as precision and recall, selecting Random Forest as the final model due to its high accuracy(79%) and robust performance.
![Screenshot]([paste_the_image_url_here](https://github.com/psahu1110/Sentiment-Analysis-on-Financial-Statements/blob/main/model%20accuracy.PNG))
   
10. Deployment-
Utilized Streamlit for deploying the sentiment analysis model.
![Screenshot]((https://github.com/psahu1110/Sentiment-Analysis-on-Financial-Statements/blob/main/deployment.PNG))

Conclusion:
This project successfully addressed sentiment analysis on financial statements, from initial data import to deploying a reliable model. The use of NLP techniques, EDA, and handling imbalanced data contributed to the effectiveness of the sentiment classification.
