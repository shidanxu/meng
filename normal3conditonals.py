import numpy as np
import pymc3 as pm
import scipy as sp
import pymc3 as pm
model = pm.Model()

# This model approximates the avg time spent per session as a distribution
observed_numberOccurrences = pickle.load( open( "numberOccurrence.p", "rb" ) )
with model: # model specifications in PyMC3 are wrapped in a with-statement
    # define priors
    mu = pm.Uniform('mu', lower=0, upper=100)
    sigma = pm.Uniform('sigma', lower=0, upper=1000)

    # define likelihood
    y_obs = pm.Normal('Y_obs', mu=mu, sd=sigma, observed=observed_numberOccurrences)

    print ("Hhahahahah\n")
    
    # inference
    start = pm.find_MAP()
    step = pm.Slice()
    niter = 500
    trace = pm.sample(niter, step, start, progressbar=True)



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