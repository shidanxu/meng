import random_generator
import pymc3 as pm
import os
import random

path = "fakeData"
for filename in filter( lambda f: not f.startswith('.'), os.listdir(path)):
	states = random_generator.parseEntry(path, filename)
	print states



# define the system and the data
true_pos, true_vel = 0, .7
true_positions = [true_vel * step for step in range(100)]

# we're using `some_tau` for the noise throughout the example.
# this should be replaced with something more meaningful.
some_tau = 1 / .5**2

# PRIORS
# we don't know too much about the velocity, might be pos. or neg. 
vel = pm.Normal("vel", mu=0, tau=some_tau)

# MODEL
# next_state = prev_state + vel (and some gaussian noise)
# That means that each state depends on the prev_state and the vel.
# We save the states in a list.
states = [pm.Normal("s0", mu=true_positions[0], tau=some_tau)]
for i in range(1, len(true_positions)):
    states.append(pm.Normal(name="s" + str(i),
                            mu=states[-1] + vel,
                            tau=some_tau))

# observation with gaussian noise
obs = pm.Normal("obs", mu=states, tau=some_tau, value=true_positions, observed=True)