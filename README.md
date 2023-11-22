# Telegram weather bot with Python

### Attempting to replicate the Telegram weather bot from FK group chat

In the group chat "FK Lörs", there is a bot called "Tönkkäbot" that gives weather data to users from Helsinki.

The bot has three main commands:
- `temperature`, which gives the current (10 minute resolution) temperature from Helsinki-Vantaa airport in celcius with one decimal point
- `forecast`, which gives a plotted forecast of the next x hours specified as `forecast x`
- `history`, which gives a plot of the last ? hour temperatures

Other notable features include:
- Automatical scaling of the plot temperature axis