# TASK 10
# Using the Shapiro-Wilk test, check whether the given sample has a normal distribution:
# [0.873, 2.817, 0.121, -0.945, -0,055, -1.436, 0.360, -1.478, -1.637, -1.869].

import scipy.stats as sps
import fme
import fmeobjects

class FeatureProcessor(object):
    def __init__(self):
        self.x = [0.873, 2.817, 0.121, -0.945, -0,055, -1.436, 0.360, -1.478, -1.637, -1.869]
    def input(self,feature):
        self.x.append(float(feature.getAttribute('shapiro.x')))
    def close(self):
        results = scipy.stats.shapiro(self.x)

        feature = fmeobjects.FMEFeature()
        feature.setAttribute('shapiro.result', results[0])
        feature.setAttribute('shapiro.pvalue', results[1])

        self.pyoutput(feature)