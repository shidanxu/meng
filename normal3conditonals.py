import numpy as np
import pymc3 as pm
import scipy as sp
import pymc3 as pm
import pickle
import matplotlib.pyplot as plt

from collections import defaultdict

def run_ppc(trace, samples=100, model=None):
    """Generate Posterior Predictive samples from a model given a trace.
    """
    if model is None:
         model = pm.modelcontext(model)

    ppc = defaultdict(list)
    for idx in np.random.randint(0, len(trace), samples):
        param = trace[idx]
        for obs in model.observed_RVs:
            ppc[obs.name].append(round(obs.distribution.random(point=param)))

    return ppc

model = pm.Model()

# This model approximates the avg time spent per session as a distribution
observed_numberOccurrences = pickle.load( open( "numberOccurrence.p", "rb" ) )
# observed_ipFrequencies = pickle.load( open( "ipBinaryFrequency.p", "rb" ) )

observed_timeFrequencies = pickle.load( open( "TimeBinaryFrequency.p", "rb" ))


# print observed_ipFrequencies

plt.plot(observed_timeFrequencies, 'ro')
plt.show()


a = np.array(observed_numberOccurrences)
upper_bound = np.percentile(a, 95)
lower_bound = np.percentile(a, 5)
a = filter(lambda x: x <= upper_bound, observed_numberOccurrences)
a = filter(lambda x: x >= lower_bound, a)

observed_numberOccurrences = filter((lambda x: x < 200), observed_numberOccurrences)
n_bins = 50
n, bins, patches = plt.hist(a, n_bins, normed=1,
                            histtype='step')
plt.show()

with model: # model specifications in PyMC3 are wrapped in a with-statement
    # define priors
    # mu = pm.Uniform('mu', lower=0, upper=100)
    # tau = pm.Uniform('tau', lower=0, upper=1000)
    # lam = pm.Uniform('lam', lower = 0, upper = 1000)
    alpha = pm.Uniform('alpha', lower = 0.0000000000000001, upper = 100)

    # define likelihood
    # y_obs = pm.Normal('Y_obs', mu=mu, sd=sigma, observed=observed_numberOccurrences)
    # y_obs = pm.Lognormal("Y_obs", mu = mu, tau = tau, observed = a)
    # y_obs = pm.Exponential("Y_obs", lam = lam, observed = a)
    y_obs = pm.Pareto("Y_obs", alpha, 1, observed = a)


    print ("Hhahahahah\n")
    
    # inference
    start = pm.find_MAP()
    step = pm.Slice()
    niter = 500
    trace = pm.sample(niter, step, start, progressbar=True)
    ppc = run_ppc(trace, model=model, samples=200)

    print ppc['Y_obs']


    pm.summary(trace)
    # # Define random variables
    # theta_a = pm.Normal('theta_a', mu=15, sd=5) # prior
    # theta_b = pm.Normal('theta_b', mu=15, sd=5) # prior
    
    # # Define how data relates to unknown causes
    # data_a = pm.Normal('observed A',
    #                       p=theta_a, 
    #                       observed=algo_a)
    
    # data_b = pm.Normal('observed B', 
    #                       p=theta_b, 
    #                       observed=algo_b)
    
    # # Inference!
    # start = pm.find_MAP() # Find good starting point
    # step = pm.Slice() # Instantiate MCMC sampling algorithm
    # trace = pm.sample(10000, step, start=start, progressbar=False) # draw posterior samples using slice sampling 