import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

with open("../data-settings.txt", "r") as settings:
    beb_settings = [float(i) for i in settings.read().split ("\n")]


data_array = np.loadtxt("../data.txt", dtype=int)

# getting shit data

size = len(data_array)
maxIndex = data_array.argmax()
chargeTime = maxIndex * beb_settings[0]
unchargeTime = (size - maxIndex) * beb_settings[0]

timeArr = np.arange(size) * beb_settings[0]

#plotting shit data

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(timeArr, data_array * beb_settings[1], 'o', linestyle='solid', markevery=30, linewidth=2, color='brown', label="V(t)")

ax.grid(which='minor', linewidth=0.5, linestyle='dashed', color="cyan")
ax.grid(which='major', linewidth=1, color="yellow")

# adjusting shit data's axis ticks and limits
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.set_ylim(0,3.5)
ax.set_xlim(0, max(timeArr) + 0.5)

# writing text so everyone understand what shit data we plotted

ax.text(8.5, 2, f"Время зарядки t  = {chargeTime} c", fontsize=16)
ax.text(8.5, 2.2, f"Время разрядки t = {unchargeTime} c", fontsize=16)

ax.set_xlabel("Время, c", fontsize=16)
ax.set_ylabel("Напряжение, B", fontsize=16)
ax.set_title("График зависимости напряжение от времени", fontsize=16)
ax.legend (fontsize=16, shadow=True, edgecolor="orange", title="Это кто")

fig.savefig("bebra.png")
