import random
import matplotlib.pyplot as plt

def headsOrTails(context = "Text"):
    heads = 0.5
    flips = 10
    prob  = 0.0
    
    results = {}
    plot_list = []
    list_results = []

    for flip in range(flips):
        random_number = random.random()
        if random_number <= heads:
        	prob += 1
        	result = prob / flips
        	results.update(
        		{
            		"Jogada": flip,
            		"Random": random_number,
            		"Resultado": result
        		}
        	)
        else:
        	results.update(
        		{
        			"Jogada": flip,
        			"Random": 0,
        			"Resultado": None
        		}
        	)
        list_results.append(results)
        results = {}

    for result in list_results:
    	if result.get('Resultado') is not None:
    		plot_list.append(1)
    	else:
    		plot_list.append(0)

    if context == "Text":
    	return list_results
    else:
    	histogram(plot_list, 10)


def histogram(results, samples):
    tosses = []
    for sample in range(samples):
        tosses.append(results[sample])

    fig, ax = plt.subplots(figsize=(12,9))
    plt.hist(tosses, bins=11)
    plt.savefig("histogram.png")

if __name__ == "__main__":
    with open('headsortails.txt', 'w+') as f:
       f.write(str(headsOrTails(context="Text")))    
    headsOrTails(context="Plot")
