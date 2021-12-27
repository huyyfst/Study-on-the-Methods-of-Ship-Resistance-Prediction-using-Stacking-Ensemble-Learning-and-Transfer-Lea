import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from pylab import *
import pickle
'''-----------------------------------------*Process of data preprocessing*---------------------------------'''
def input_split_scaler_output_data(file_name, sheet_name):
    Train_set = pd.read_excel('2nd_train3.xls', 'Sheet1')
    print('Train_set =\n',Train_set)
    tra_set = Train_set.loc[:, :]
    print('tra_set=\n',tra_set)
    SS = StandardScaler().fit(tra_set)

    Data_set = pd.read_excel(file_name, sheet_name)
    dat_set = Data_set.loc[:, :]
    data_set_feature1 = dat_set.drop('Cr*1000', axis=1)
    data_set_feature = SS.transform(data_set_feature1)
    data_set_label = dat_set['Cr*1000'].copy()
    print('------over--------')
    return(data_set_feature, data_set_label)
'''-----------------------------------------*test samples after preprocessing*---------------------------------'''
test_set_feature,test_set_label = input_split_scaler_output_data('2nd_test_KCS.xls', 'Sheet1')
X_test = test_set_feature
Y_test = np.array(test_set_label)#.reshape(14,1)
'''-----------------------------------------*load trained model*---------------------------------'''
# f = open('models\\2nd_vc3_KNN.pickle', 'rb') #load model
# f = open('models\\2nd_vc3_LR.pickle', 'rb')
f = open('models\\2nd_vc3_SVR.pickle', 'rb')
# f = open('models\\2nd_vc3_RF.pickle', 'rb')

regressor_model = pickle.load(f)
f.close()
'''-----------------------------------------*Export forecast results of test samples*---------------------------------'''
# pd.DataFrame(regressor_model.predict(X_test)).to_excel('2nd_prediction_results\\vc3_KNN.xls')
# pd.DataFrame(regressor_model.predict(X_test)).to_excel('2nd_prediction_results\\vc3_LR.xls')
pd.DataFrame(regressor_model.predict(X_test)).to_excel('2nd_prediction_results\\vc3_SVR.xls')
# pd.DataFrame(regressor_model.predict(X_test)).to_excel('2nd_prediction_results\\vc3_RF.xls')


'''-----------------------------------------*prediction errors*---------------------------------'''
def precision(origin_data, prediction_data):
    relative_error = []
    for i in range(len(origin_data)):
         relative_error.append(((abs((origin_data[i] - prediction_data[i]) * 100 / origin_data[i]))))
    mean_relative_absolute_error = np.mean(relative_error)
    return(mean_relative_absolute_error)
print('mean_relative_absolute_error：\n', precision(Y_test, regressor_model.predict(X_test)))

'''----------------------------------------*Fig Plot*--------------------------------------------------'''
def plot_origin_prediction(origin_set, prediction_set,name):
    plt.figure(figsize=(6,4))
    plt.scatter(range(len(origin_set)), origin_set, marker='o', label=u'Actual Value')
    plt.scatter(range(len(prediction_set)), prediction_set, marker='x', label=u'Predicted Value')
    plt.text(0, 1.0, 'Maximum_Error=%.4f' % precision(origin_set,prediction_set), fontdict={'size': 10, 'color': 'black'})
    plt.legend(loc='upper left')
    plt.ylim(0,1.5)
    plt.title(name)
    plt.xlabel('Sample')
    plt.ylabel('1000*Ct')
    plt.show()
plot_origin_prediction(Y_test, regressor_model.predict(X_test),'Testing-set')