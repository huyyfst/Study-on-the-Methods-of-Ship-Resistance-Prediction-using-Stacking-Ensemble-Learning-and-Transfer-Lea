# Study-on-the-Methods-of-Ship-Resistance-Prediction-using-Stacking-Ensemble-Learning-and-Transfer-Learning


Ship resistance is an important performance index of ships and a topic that cannot be avoided in ship design. The rapid and accurate prediction of ship resistance can improve design efficiency.In this article, new resistance prediction methods using stacking ensemble learning and transfer learning are proposed. The work can be divided into two parts. In the first part, the research on resistance prediction of container ships using basic ML and stacking ensemble learning models is carried out. Four representative models, linear regression (LR), K-nearest neighbor (KNN), support vector regression (SVR), random forest (RF), are taken as basic ML models. Stacking ensemble models are constructed using basic models, shown in Fig. 1.  In the second part, stacking ensemble learning models used for the resistance prediction of container ships are adopted to predict the resistance of a bulk carrier using transfer learning, shown in Fig. 2.


![图片](https://user-images.githubusercontent.com/45836677/147429091-d98fe553-61b4-4da1-b7f7-56dedffd6cf9.png)

Fig. 1. The topology of stacking machine learning models. Where x1, x2, ..., xn represent the input ship features; y1, y2, y3, y4 are the prediction results of stacking ensemble learning models.

![图片](https://user-images.githubusercontent.com/45836677/147429165-3e88662a-3e5a-415f-91dd-9fa3d6140a75.png)

Fig. 2. The topology of transfer learning models.

In the learning of stacking ensemble models, container ships of 1100-TEU, 4250-TEU, 9000-TEU, 13500-TEU, are taken as the training set, 4700-TEU container ship and KCS are taken as the test set. Here, KCS data are taken to verify the results of the study. 

The workflow of programs is shown in Fig. 3.

<img width="1093" alt="flow" src="https://user-images.githubusercontent.com/45836677/147475181-edbec4ca-cb5e-45aa-89ac-b0415a6680d5.png">

Fig. 3. The workflow of programs
