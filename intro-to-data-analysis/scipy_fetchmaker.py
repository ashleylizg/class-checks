import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

# Investigation of rottweiler tail length using average and standard deviation.

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")

print("The average rottweiler tail length is: {}".format(np.mean(rottweiler_tl)))
print("The standard deviation for rottweiler tail length is: {}".format(np.std(rottweiler_tl)))

# Investigation of how many whippets are rescues out of the total number, assuming the rate is predicted to be about 8%. 

whippet_rescue = fetchmaker.get_is_rescue("whippet")

num_whippet_rescue = np.count_nonzero(whippet_rescue)

num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippet_rescue, num_whippets, 0.08)
print("The P-value for the number of whippet rescues and number of total whippets is: {}".format(pval))

# Investigation of weight differences between whippets, terriers, and pitbulls.

whippet_weight = fetchmaker.get_weight("whippet")
whippet_weight_avg = np.mean(whippet_weight)

terrier_weight = fetchmaker.get_weight("terrier")
terrier_weight_avg = np.mean(terrier_weight)

pitbull_weight = fetchmaker.get_weight("pitbull")
pitbull_weight_avg = np.mean(pitbull_weight)

print("The average whippet weight is: {}".format(whippet_weight_avg))
print("The average terrier weight is: {}".format(terrier_weight_avg))
print("The average pitbull weight is: {}".format(pitbull_weight_avg))

fstat, pval = f_oneway(whippet_weight, terrier_weight, pitbull_weight)
print("The p-value for weights of whippets, terriers, and pitbulls: {}".format(pval))

dog_breeds = np.concatenate([whippet_weight, terrier_weight, pitbull_weight])
labels = ['whippet']*len(whippet_weight) + ['terrier']*len(terrier_weight) + ['pitbull']*len(pitbull_weight)
tukey_results = pairwise_tukeyhsd(dog_breeds, labels, 0.05)
print(tukey_results)

# Investigation of color differences between poodles and shihtzus.

poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

black_poodles = np.count_nonzero(poodle_colors == "black")
brown_poodles = np.count_nonzero(poodle_colors == "brown")
gold_poodles = np.count_nonzero(poodle_colors == "gold")
grey_poodles = np.count_nonzero(poodle_colors == "grey")
white_poodles = np.count_nonzero(poodle_colors == "white")

black_shihtzus = np.count_nonzero(shihtzu_colors == "black")
brown_shihtzus = np.count_nonzero(shihtzu_colors == "brown")
gold_shihtzus = np.count_nonzero(shihtzu_colors == "gold")
grey_shihtzus = np.count_nonzero(shihtzu_colors == "grey")
white_shihtzus = np.count_nonzero(shihtzu_colors == "white")

color_table = [[black_poodles, black_shihtzus], [brown_poodles, brown_shihtzus], [gold_poodles, gold_shihtzus], [grey_poodles, grey_shihtzus], [white_poodles, white_shihtzus]]

_ , pval, _ , _ = chi2_contingency(color_table)
print("The p-value for comparing dog colors is: {}".format(pval))

# Investigation of age difference between chihuahuas and greyhounds in the data set.

chih_age = fetchmaker.get_age("chihuahua")
grey_age = fetchmaker.get_age("greyhound")

age_chih_grey_results = ttest_ind(chih_age, grey_age)
if age_chih_grey_results < 0.05:
  print("Ages of chihuahuas and greyhounds are different!")
else:
  print("Ages of chihuahuas and greyhounds are not that different.")
  
# Investigation of weight differences between all breeds in the sample.
  
poodle_weight = fetchmaker.get_weight("poodle")

rottweiler_weight = fetchmaker.get_weight("rottweiler")

whippet_weight = fetchmaker.get_weight("whippet")

greyhound_weight = fetchmaker.get_weight("greyhound")

terrier_weight = fetchmaker.get_weight("terrier")

chihuahua_weight = fetchmaker.get_weight("chihuahua")

shihtzu_weight = fetchmaker.get_weight("shihtzu")

pitbull_weight = fetchmaker.get_weight("pitbull")

fstat, pval = f_oneway(poodle_weight, rottweiler_weight, whippet_weight, greyhound_weight, terrier_weight, chihuahua_weight, shihtzu_weight, pitbull_weight)
if pval < 0.05:
  print("The p-value is: {}".format(pval))
  print("Investigate further with a Tukey's Range Test!")
else:
  print("The p-value is: {}".format(pval))
  print("No need to investigate further, the breed weights are too similar.")
  
breed_weights = np.concatenate([poodle_weight, rottweiler_weight, whippet_weight, greyhound_weight, terrier_weight, chihuahua_weight, shihtzu_weight, pitbull_weight])
labels_for_breeds = ['poodle']*len(poodle_weight) + ['rottweiler']*len(rottweiler_weight) + ['whippet']*len(whippet_weight) + ['greyhound']*len(greyhound_weight) + ['terrier']*len(terrier_weight) + ['chihuahua']*len(chihuahua_weight) + ['shihtzu']*len(shihtzu_weight) + ['pitbull']*len(pitbull_weight) 

tukey_weight_results = pairwise_tukeyhsd(breed_weights, labels_for_breeds, 0.05)
print(tukey_weight_results)
