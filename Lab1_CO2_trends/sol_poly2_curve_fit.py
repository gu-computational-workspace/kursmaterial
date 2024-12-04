def fit_func_polynomial(x, a, b, c):
    return a*x**2 + b*x + c

popt, pcov = optimize.curve_fit(fit_func_polynomial, co2flask.date_delta.values, co2flask.analysis_value.values)

print(popt, pcov)

ax = plt.subplot()

ax.plot(co2flask.date_delta, co2flask.analysis_value, label="measured")
ax.plot(co2flask.date_delta.values, fit_func_polynomial(co2flask.date_delta, *popt), label="fitted")

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