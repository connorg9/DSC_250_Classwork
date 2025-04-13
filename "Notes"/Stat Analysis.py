import scipy.stats as stats
import matplotlib.pyplot as plt

vals1 = stats.norm.rvs(size = 10000)
vals2 = stats.expon.rvs(size = 10000)

stat1, p1 = stats.normaltest(vals1)
stat2, p2 = stats.normaltest(vals2)
print("Normal test p-values are p1 = {0:.2f} and p2 = {1:.2f}".format(p1, p2))

print("for vals1...")
if p1 >= 0.05:
    print("Dont reject null hypothesis")
else:
    print("reject null hypothesis")

print("for vals2...")
if p2 >= 0.05:
    print("Dont reject null hypothesis")
else:
    print("reject null hypothesis")

#%%

exp_data = [38.4, 39.3, 40.1, 37.6, 39.5, 40.0, 39.9, 39.2, 38.5, 39.5]

stat, p = stats.ttest_1samp(exp_data, popmean = 40)
print("The 1 sample t-test p-values is {0:.2f}".format(p))

if p < 0.05:
    print("Reject null hypothesis")
else:
    print("Dont reject null hypothesis")

#%%

company_A = stats.norm.rvs(size = 100, loc = 30, scale = 3)
company_B = stats.norm.rvs(size = 20, loc = 30, scale = 0.3)

stat, p = stats.ks_2samp(company_A, company_B)

print("The 2 sample KS test p-value is {0:.2f}".format(p))
if p < 0.05:
    print("Reject null hypothesis")
else:
    print("Dont reject null hypothesis")

