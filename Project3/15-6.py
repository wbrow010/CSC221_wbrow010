import plotly.express as px

from die import Die

die1 = Die(8)
die2 = Die(8)

rolls = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    rolls.append(result)

freqs = []
possible_results = range(2, die1.num_sides + die2.num_sides + 1) # min is 2, max is 8 + 8 + 1

for value in possible_results:
    frequency = rolls.count(value)
    freqs.append(frequency)

title = "Rolling two D8's x1000"
fig = px.bar(x=possible_results, y=freqs, title=title)

fig.show()