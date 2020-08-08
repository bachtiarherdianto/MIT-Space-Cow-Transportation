''' Hypothesis testing in Machine learning using Python
    source: https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce '''
import pandas as pd, matplotlib.pyplot as plt, numpy as np
from scipy import stats
from statsmodels.stats import weightstats as stests


# INTRODUCTION - Normal Probability Density Function
x = np.linspace(-4, 4, num= 100)
constant = 1.0 / np.sqrt(2*np.pi)
pdf_normal_dist = constant * np.exp((-x**2)/2.0)
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x, pdf_normal_dist)
# ax.set_ylim(0)
# ax.set_title('Normal Distribution', size= 20)
# ax.set_ylabel('Probability Density', size= 20)
# plt.show()      # show probability density function

def hipothesisTest(pValue, alpha):
    if pValue < alpha:
        print('p-value: ', pValue,'| reject null hypothesis')
    else:
        print('p-value: ', pValue, '| accept null hypothesis')


''' Paired sampled t-test
    The paired sample t-test is also called dependent sample t-test. It’s an uni variate test that tests for 
    a significant difference between 2 related variables. An example of this is if you where to collect 
    the blood pressure for an individual before and after some treatment, condition, or time point. 
    H0 : means difference between two sample is 0
    H1 : mean difference between two sample is not 0 '''
df = pd.read_csv('blood_pressure.csv')
# print(df.head(5))       # to preview the file

tTest, pValue_t = stats.ttest_rel(df['bp_before'], df['bp_after'])    # t-test between bp_before and bp_after
# hipothesisTest(pValue_t, 0.05)    # Significance level = 0.05

''' Two-sample Z test
    In two sample z-test, here we are checking two independent data groups and deciding whether sample mean 
    of two group is equal or not.
    H0 : mean of two group is 0
    H1 : mean of two group is not 0
    Example : we are checking in blood data after blood and before blood data. '''
zTest, pValue_z = stests.ztest(df['bp_before'], x2=df['bp_after'], value= 0, alternative='two-sided')
# hipothesisTest(pValue_z, 0.05)      # Significance level = 0.05

''' One Way F-test(Anova) :
    It tell whether two or more groups are similar or not based on their mean similarity and f-score.
    Example : there are 3 different category of plant and their weight and need to check 
              whether all 3 group are similar or not. '''
# df_anova = pd.read_csv('PlantGrowth.csv')
# # print(df_anova.head(5))       # to preview the file
# grps = pd.unique(df_anova.group.values)
# d_data = {grp:df_anova['weight'][df_anova.group == grp] for grp in grps}
# F, pVal_one_way = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])
#
# hipothesisTest(pVal_one_way, 0.05)    # Significance level = 0.05

''' Two Way F-test :
    It is used when we have 2 independent variable and 2+ groups. 2-way F-test does not 
    tell which variable is dominant. if we need to check individual significance then Post-hoc 
    testing need to be performed. For example, let’s take a look at the Grand mean crop yield 
    (the mean crop yield not by any sub-group), as well the mean crop yield by each factor, 
    as well as by the factors grouped together. '''
import statsmodels.api as sm
from statsmodels.formula.api import ols

# df_anova2 = pd.read_csv('crop_yield.csv')
# # print(df_anova2.head(5))
# model = ols('Yield ~ C(Fert) * C(Water)', df_anova2).fit()
# # print(f"Overall model F({model.df_model: .0f},{model.df_resid: .0f}) = {model.fvalue: .3f}, p = {model.f_pvalue: .4f}")
# summaryModel = model.summary()
# # print(summaryModel)
# res = sm.stats.anova_lm(model, typ= 2)
# # print(res)

''' Chi-Square Test:
    The test is applied when you have two categorical variables from a single population. 
    It is used to determine whether there is a significant association between the two variables.
    For example, in an election survey, voters might be classified by gender (male or female) 
    and voting preference (Democrat, Republican, or Independent). We could use a chi-square test for 
    independence to determine whether gender is related to voting preference '''
from scipy.stats import chi2

def ChiSequareTest(chi_square_stats, critical_value, pValue, alpha):
    if chi_square_stats >= critical_value:
        print('Reject null hypothesis\nThere is a relationship between 2 categorical variables')
    else:
        print('Retain null hypothesis\nThere is no relationship between 2 categorical variables')
    print('---------------------------------------------------------')
    if pValue < alpha:
        print('p-value: ', pValue,'| reject null hypothesis\nThere is a relationship between 2 categorical variables')
    else:
        print('p-value: ', pValue, '| accept null hypothesis\nThere is no relationship between 2 categorical variables')

df_chi = pd.read_csv('chi-test.csv')
# print(df_chi.head(5))

contingency_table = pd.crosstab(df_chi['Gender'], df_chi['Like Shopping?'])
# print('contigency table:\n', contingency_table)

ObservedVal = contingency_table.values
# print('observes values :\n', ObservedVal)

i = stats.chi2_contingency(contingency_table)   # i[3] is Expected Values
# print('Expected Values :\n', i[3])

no_of_rows = len(contingency_table.iloc[0:2, 1])
no_of_columns = len(contingency_table.iloc[0, 0:2])
df = (no_of_rows - 1)*(no_of_columns - 1)   # Degree of Freedom
# print('Degree of Freedom: ', df)

chi_square = sum([(i - j)**2. / i for i, j in zip(ObservedVal, i[3])])
chi_square_statistic = chi_square[0] + chi_square[1]    # Chi-square statistic
# print('Chi-Square statistic: ', chi_square_statistic)

alpha = 0.05         # Significance level
critical_value = chi2.ppf(q=1-alpha, df= df)        # critical value
# print('Critical value: ', critical_value)

pVal = 1 - chi2.cdf(x=chi_square_statistic, df=df)      # p-value
# print('p-value: ', pVal)

# ChiSequareTest(chi_square_statistic, critical_value, pVal, alpha)

