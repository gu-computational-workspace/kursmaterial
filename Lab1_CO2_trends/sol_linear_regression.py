n = co2flask.date_delta.count()

t = co2flask.date_delta.values
tmean = np.mean(t)
c = co2flask.analysis_value.values
cmean = np.mean(c)

a = np.sum( (t - tmean) * (c - cmean) ) / np.sum( (t - tmean)**2)

b = np.mean(c) - a * np.mean(t)

print(a, b)

ax = plt.subplot()

ax.plot(co2flask.date_delta, co2flask.analysis_value, label="measured", color="k")
ax.plot(co2flask.date_delta, a*co2flask.date_delta.values + b, label="fitted", color="r")

xticks = np.linspace(co2flask.date_delta.values[0], co2flask.date_delta.values[-1], 5)
xtick_indices = []
for i in range(len(xticks)):
    idx = np.argmin(np.abs(co2flask.date_delta.values - xticks[i]))
    xtick_indices.append(idx)
ax.set_xticks(xticks)
ax.set_xticklabels(co2flask.datetime.iloc[xtick_indices].dt.year)

ax.set_ylabel("CO2 mole fraction (ppm)")
ax.set_xlabel("Years")

plt.grid()

plt.legend()