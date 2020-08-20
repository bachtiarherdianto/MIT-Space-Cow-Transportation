from scipy.integrate import quad
import numpy as np, matplotlib.pyplot as plt, matplotlib.image as mpimg, seaborn as sns, pandas as pd, copy


''' Box-plot are a standardized way of displaying the distribution of data based on a five number 
    summary ('minimum', first quartile (Q1), median, third quartile (Q3), and 'maximum').
    - To tell about the values of your outliers
    - To identify if data is symmetrical
    - To determine how tightly data is grouped
    - To see if the data is skewed '''
# plt.imshow(mpimg.imread('box_plot_example.png'))
# plt.show()  # to show image about box-plot diagram

''' The data used to demonstrate box-plot is the Breast Cancer Wisconsin (Diagnostic).
    The goal of the visualization is to show how the distributions for the column "area_mean"
    differs for Benign v.s. Malignant "diagnosis" '''
cancer_df = pd.read_csv('box_plot_tutorial.csv')    # load dataset into dataframe (df)
# # print(cancer_df.head(6))                            # to look at first 6 row of the data

# dataDist = cancer_df['diagnosis'].value_counts(dropna= False)
# # print(dataDist)       # looking at the distribution of the dataset in terms of diagnosis

''' Create Box-plot using Matplotlib package
    Data from the Breast Cancer Wisconsin '''
malignant = cancer_df.loc[cancer_df['diagnosis']=='M', 'area_mean'].values
benign = cancer_df.loc[cancer_df['diagnosis']=='B', 'area_mean'].values
#
plt.boxplot([malignant, benign], labels=['M', 'B'])   # plotting
plt.show()

''' Create Box-plot using Pandas package
    Data from the Breast Cancer Wisconsin '''
# cancer_df.boxplot(column= 'area_mean', by= 'diagnosis')   # plotting
# plt.title('')   # delete the title
# plt.suptitle('')    # delete the sub-title
# plt.show()

''' Create Box-plot using Seaborn package
    Data from the Breast Cancer Wisconsin '''
# sns.boxplot(x='diagnosis', y='area_mean', data=cancer_df) # plotting
# plt.show()

''' The goal of the visualization is to show how the Box-plot for 
    "smoothness_mean" differs for Benign v.s. Malignant "diagnosis" '''
# fig, smoothness_mean = plt.subplots(nrows= 1, ncols= 1, figsize= (10, 10))
# sns.boxplot(x='diagnosis', y='smoothness_mean', data=cancer_df, palette='Set1', ax=smoothness_mean)
# smoothness_mean.set_xlabel('diagnosis', fontsize= 20)
# smoothness_mean.set_ylabel('smoothness_mean', fontsize= 20)
# plt.xticks(fontsize= 15)
# plt.yticks(fontsize= 15)
# plt.show()    # to show

''' The goal of the visualization is to show how the Box-plot for 
    "compactness_mean" differs for Benign v.s. Malignant "diagnosis" '''
# fig, compactness_mean = plt.subplots(nrows= 1, ncols= 1, figsize= (10, 10))
# sns.boxplot(x='diagnosis', y='compactness_mean', data=cancer_df, palette='Set1', ax=compactness_mean)
# compactness_mean.set_xlabel('diagnosis', fontsize= 20)
# compactness_mean.set_ylabel('compactness_mean', fontsize= 20)
# plt.xticks(fontsize= 15)
# plt.yticks(fontsize= 15)
# plt.show()    # to show

# temp_df = cancer_df.copy()
# diag_map = {'M':1, 'B':0}
# temp_df['diagnosis'] = temp_df['diagnosis'].map(diag_map)
#
# fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (8,8));
#
#
# corr = temp_df.corr().abs()
# sns.heatmap(corr,
#             xticklabels=corr.columns.values,
#             yticklabels=corr.columns.values,
#             cmap = 'Blues',
#             linewidths=.5,
#             square = True,
#             ax = axes);
#
# plt.yticks(fontsize = 13);
# plt.xticks(fontsize = 13);
# # plt.show()

# with open('box_plot_tutorial.csv') as f:
#     headers = f.read()
#
# headerList = headers.split()
#
# df = pd.read_csv(filepath_or_buffer ='box_plot_tutorial.csv', names= headerList)
#
# theFeatures = ['radius_mean', 'radius_sd_error','radius_worst', 'texture_mean', 'texture_sd_error', 'texture_worst', 'perimeter_mean', 'perimeter_sd_error', 'perimeter_worst', 'area_mean', 'area_sd_error', 'area_worst', 'smoothness_mean', 'smoothness_sd_error', 'smoothness_worst', 'compactness_mean', 'compactness_sd_error', 'compactness_worst', 'concavity_mean', 'concavity_sd_error', 'concavity_worst', 'concave_points_mean', 'concave_points_sd_error', 'concave_points_worst', 'symmetry_mean', 'symmetry_sd_error', 'symmetry_worst', 'fractal_dimension_mean', 'fractal_dimension_sd_error', 'fractal_dimension_worst']
#
# color_dic = {'M':'red', 'B':'blue'}
# colors = df['diagnosis'].map(lambda x: color_dic.get(x))
#
# pd.plotting.scatter_matrix(df[theFeatures], c=colors, alpha=0.4, figsize=((15,15)));
# plt.show()



# ''' Exploratory Data Analysis (EDA)
#     is an approach to analyzing data sets to summarize their
#     main characteristics '''
# features = cancer_df.columns        # load features from the main data
# all_features = []                   # make list of all features
# for i in range(1, len(features)-1):
#     all_features.append(features[i])
#
# # theFeatures = copy.copy(all_features)
# # print(theFeatures)        # print all features
#
theFeatures = ['radius_mean', 'radius_sd_error','radius_worst', 'texture_mean', 'texture_sd_error', 'texture_worst', 'perimeter_mean', 'perimeter_sd_error', 'perimeter_worst', 'area_mean', 'area_sd_error', 'area_worst', 'smoothness_mean', 'smoothness_sd_error', 'smoothness_worst', 'compactness_mean', 'compactness_sd_error', 'compactness_worst', 'concavity_mean', 'concavity_sd_error', 'concavity_worst', 'concave_points_mean', 'concave_points_sd_error', 'concave_points_worst', 'symmetry_mean', 'symmetry_sd_error', 'symmetry_worst', 'fractal_dimension_mean', 'fractal_dimension_sd_error', 'fractal_dimension_worst']
#
# # bins = 12
# # plt.figure(figsize=(20, 100))
# # for i, all_features in enumerate(theFeatures):
# #     rows = int(len(theFeatures) / 2)
# #     plt.subplot(rows, 2, i + 1)
# #     sns.boxplot(x = 'diagnosis', y= theFeatures, data= cancer_df, palette='Set1')
# #     plt.xlabel('diagnosis', fontsize= 24)
# #     plt.ylabel(all_features, fontsize= 24)
# #     plt.xticks(fontsize= 20)
# #     plt.yticks(fontsize= 20)
#
#
# plt.figure(figsize=(20, 100))
# for i, feature in enumerate(theFeatures):
#     rows = int(len(theFeatures) / 2)
#
#     plt.subplot(rows, 2, i + 1)
#
#     sns.boxplot(x='diagnosis', y=feature, data=cancer_df, palette="Set1")
#
#     # Changing default seaborn/matplotlib to be more readable
#     plt.xlabel('diagnosis', fontsize=24)
#     plt.ylabel(feature, fontsize=24)
#     plt.xticks(fontsize=20)
#     plt.yticks(fontsize=20)
#
#
# plt.tight_layout()
