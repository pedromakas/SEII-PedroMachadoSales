x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2
plt.scatter(x_data, y_data)
from scipy.optimize import curve_fit

def func(x, a, b):
    return a*x**2 + b
popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))
popt
plt.plot(t_data,y_data,'o--')
from scipy.optimize import curve_fit

def func(x, A, w, phi):
    return A*np.cos(w*x+phi)

popt, pcov = curve_fit(func, t_data, y_data, p0=(4, np.pi, 0))
popt
A, w, phi = popt
t = np.linspace(0, 10, 100)
y = func(t, A, w, phi)
plt.scatter(t_data,y_data)
plt.plot(t,y)
popt
np.sqrt(np.diag(pcov))
