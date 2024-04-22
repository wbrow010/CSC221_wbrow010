import plotly.express as px

from die import Die

die1 = Die(6)
die2 = Die(6)
die3 = Die(6)

rolls = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    rolls.append(result)

freqs = []
possible_results = range(2, die1.num_sides + die2.num_sides + die3.num_sides + 1) # min is 3, max is 6 + 6 + 6 + 1

for value in possible_results:
    frequency = rolls.count(value)
    freqs.append(frequency)

title = "Rolling three D6's x1000"
fig = px.bar(x=possible_results, y=freqs, title=title)

fig.show()