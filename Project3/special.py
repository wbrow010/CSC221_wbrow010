import matplotlib.pyplot as plt

gpu_data = {
    2004: {'name': 'ATI Radeon X800 XT', 'MSRP': 499, 'TFLOPS': 0.2},
    2006: {'name': 'NVIDIA GeForce 8800 GTX', 'MSRP': 599, 'TFLOPS': 0.5},
    2008: {'name': 'ATI Radeon HD 4870', 'MSRP': 299, 'TFLOPS': 1.2},
    2010: {'name': 'NVIDIA GeForce GTX 580', 'MSRP': 499, 'TFLOPS': 1.5},
    2012: {'name': 'NVIDIA GeForce GTX 680', 'MSRP': 499, 'TFLOPS': 3.2},
    2014: {'name': 'NVIDIA GeForce GTX 980', 'MSRP': 549, 'TFLOPS': 4.9},
    2016: {'name': 'NVIDIA GeForce GTX 1080', 'MSRP': 599, 'TFLOPS': 8.8},
    2018: {'name': 'NVIDIA GeForce RTX 2080 Ti', 'MSRP': 999, 'TFLOPS': 14.2},
    2020: {'name': 'NVIDIA GeForce RTX 3080', 'MSRP': 1499, 'TFLOPS': 36},
    2022: {'name': 'NVIDIA GeForce RTX 4090', 'MSRP': 1599, 'TFLOPS': 82.5}
}

years = list(gpu_data.keys())
tflops_per_dollar = [gpu_data[year]['TFLOPS'] / gpu_data[year]['MSRP'] for year in years]
names = [gpu_data[year]['name'] for year in years]

plt.figure(figsize=(12, 6))
plt.plot(years, tflops_per_dollar, marker='o', linestyle='-', label='TFLOPS per Dollar')

plt.title('GPU TFLOPS per Dollar Over the Years')
plt.xlabel('Years')
plt.ylabel('TFLOPS per Dollar')

plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()

for i, (year, tpd) in enumerate(zip(years, tflops_per_dollar)):
    plt.text(year, tpd, names[i], ha='right', va='bottom')

plt.show()