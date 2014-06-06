## AdVantage<br />
A machine learning mobile ad monetization optimizer.
### Overview:
* A data product that predicts the mobile ad revenue prior to receiving the ad from ad networks.<br />
* Using Ad Vantage, mobile apps or ad exchanges can optimize revenue.<br />
* Advertisers can better understand their targeting demographics, publisher content relevance and user behavior.

### Results:
* Prediction accuracy: 79%.<br />
* Random Forest ROC Plot AUC: 0.85.<br />
* Logistic Regression ROC Plot AUC: 0.76.<br />
* Naive Bayes Gaussian AUC: 0.60.<br />
* Naive Bayes Multinomial AUC: 0.73.<br />
* Cross-Validation F1 Score Random Forest: 0.89.<br />
* Revenue Lift from "Random" baseline: 109%.<br />

### Data:
Logs of raw ad tags received from ad networks to classify five targeted revenue buckets.<br />

### Analysis and Modeling:
* The Classifiers were Random Forest, Logistic Regression (One-vs-All), Naive Bayes (One-vs-All).<br />
* Tuned Classifiers with Grid Search, conducted Feature Engineering and cross-validation.<br />

### On the Roadmap:
* A/B testing to verify revenue lift; or lift chart.
* Feature extraction, create device user session feature, behavior pattern.
* Core revenue group: top 20% apps, devices and locations.
* Train on more time-consuming models to improve accuracy.
* Build scalability.

### Project Details:
* Code files at:<br />
[project_code](https://github.com/aprial/AdVantage/tree/master/project_code) 
* Project Presentation:<br />
[Jun Zhang presso mobile ads.pdf](https://github.com/aprial/AdVantage/blob/master/Jun%20Zhang%20presso%20mobile%20ads.pdf)
* Some Visualization and more project details to come at:<br />
http://junkateannzhang.herokuapp.com/
