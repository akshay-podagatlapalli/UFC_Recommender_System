# UFC Recommender System

Want to get into the exciting world of Mixed Martial Arts (MMA), only ever heard of UFC as a passing phrase, and watched all the trash talk that happens between UFC fighters have no idea where to start or which fights to watch? Look no further! This UFC Recommender System is here to help you dive into the thrilling world of MMA and discover some of the most epic fighters in UFC history. 


By utilizing a combination of data analysis and user preferences, this recommender system will provide you with personalized recommendations based on your interests. Whether you enjoy intense striking battles, technical ground game exchanges, or dramatic comebacks, this model’s got you covered.


To get started, simply respond to a few questions asked by the model. It will take your responses and preferences, scour through the extensive UFC fighters’ roster (active and retired) and curate a list of top 5 fighters for you to check out and learn more about. 

![rec_sys](https://github.com/akshay-podagatlapalli/UFC_Recommender_System/assets/65557678/c2af0d8e-86f0-4f58-a167-ad0c86fdf9cc)


## Data Collection
The data required to build this model was obtained from the following source (https://www.kaggle.com/datasets/rajeevw/ufcdata). 


## Data Cleaning
The final dataset that is being used to provide the recommendations was produced by going through the following stages: 
  *	All the stats presented in the original dataset were collected per fight, per fighter. This data was presented chronologically from the inception of the UFC until the year 2021. 
    *	Because this model recommends fighters, and not fights, the cumulative stats had to be collected per fighter. 
  *	The primary key in this dataset is the `fighter_name`. However, the original dataset had `R_fighter_name` and `B_fighter_name` as the primary and secondary keys. 
    *	Because there are going to be multiple records of the same fighter’s name in this dataset since the same fighter will have had multiple fights, all the fights per fighter were aggregated by the fighter name, for every `R_fighter_name` and `B_fighter_name`. 
  *	Once the primary key was obtained, the stats per fight, per fighter was aggregated, either by `average()`, `count()`, or `max()`. 
      *	The goal with this was to obtain a single record per fighter with the most accurate stats. 
  *	Once this data was prepared, the next step involved classifying every fighter into a specific fight style. This was done by following this excellent article (https://literalfightnerd.com/posts/2022-01-05-visualizing-fighter-styles/)
  *	After classifying every fighter into a specific fight style, data analysis and PCA was performed to build the recommender model. 
  

## Formulating the Recommender Model 
How does the model actually come up with the recommendations? 
The short answer is that it uses cosine similarity between the users’ responses and the fighter stats from the dataset. 
The more involved answer has a few steps involved, in how the model comes up with the recommendation, which are listed below: 
* The model asks the user 5 questions. 
* The first two questions help filter down the responses by asking the user their preferred fighting style and their preferred weight class. 
* This filtering step helps narrow down the dataset to focus on fighters who match the user's preferences in terms of fighting style and weight class. By identifying the user's preferred criteria, the model can reduce the number of potential recommendations and provide more relevant suggestions.
* The next three questions as mentioned in the previous section were forumulated using PCA analysis. 
  * Each of the 3 questions is associated with each of the first 3 PCs. 
    * Question 3 > PC1
    * Question 4 > PC2
    * Question 5 > PC3
  * Each PC’s loading score provides a vector representation of how much each feature contributes to it corresponding principal component. 
  * The user’s response, which is in between the range of [0, 10], adds an additional weight to the loading score vector by multiplying the features associated with the user’s preference and dividing the features that are opposite of the user’s preference by the value entered by the user. 
  * This is done for questions 3 to 5 and the modified loading scores are then combined into single vector. 
  * The more similar the fighter's stats are to the combined vector, the higher the cosine similarity score.
  * Based on the computed cosine similarity scores, the model ranks the fighters and generates a list of recommendations. Fighters with higher cosine similarity scores, indicating a stronger similarity to the user's combined preference vector, are considered more suitable recommendations.


It's important to note that in this approach, the PCA analysis and modification of loading scores with user preferences serve to capture the user's preferences and weigh the importance of different features accordingly. By incorporating the user's preferences into the loading scores and combining them into a single vector, the model can provide recommendations that align more closely with the user's specific preferences.


Additionally, the model may consider other factors or techniques to further refine the recommendations. These could include factors such as popularity, recent performance, user feedback, or any other relevant contextual information.
Overall, this approach utilizes PCA analysis to capture the underlying structure in the user's preferences and combines it with cosine similarity to identify fighters with stats that align well with the user's modified preference vector. By leveraging both PCA analysis and cosine similarity, the model can generate more personalized and relevant recommendations for the user.


## Next Steps


While this model serves a first iteration of a successful proof-of-concept, the next steps will involve utilizing more features that can be utilized to rank fighters based on other metrics such as their popularity, most watched fights, social media presence, or recent achievements. By incorporating additional features, the recommender model can provide a more comprehensive and dynamic ranking of fighters.
