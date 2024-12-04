import scipy.optimize as optimize

def fit_func(x, a, b):
    return a*x + b

popt, pcov = optimize.curve_fit(fit_func, co2flask.date_delta, co2flask.analysis_value.values)

print(popt, pcov)

ax = plt.subplot()

ax.plot(co2flask.date_delta, co2flask.analysis_value, label="measured")
ax.plot(co2flask.date_delta, fit_func(co2flask.date_delta.values, *popt), label="fitted")

xticks = np.linspace(co2flask.date_delta.values[0], co2flask.date_delta.values[-1], 5)
xtick_indices = []
for i in range(len(xticks)):
    idx = np.argmin(np.abs(co2flask.date_delta.values - xticks[i]))
    xtick_indices.append(idx)
ax.set_xticks(np.linspace(co2flask.date_delta.values[0], co2flask.date_delta.values[-1], 5))
ax.set_xticklabels(co2flask.datetime.iloc[xtick_indices].dt.year)

ax.set_ylabel("CO2 mole fraction (ppm)")
ax.set_xlabel("Years")

plt.grid()

plt.legend()