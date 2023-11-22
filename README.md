# Telegram weather bot with Python

### Attempting to replicate the Telegram weather bot from FK group chat

In the group chat "FK Lörs", there is a bot called "Tönkkäbot" that gives weather data to users from Helsinki.

The bot has three main commands:
- `temperature`, which gives the current (10 minute resolution) temperature from Helsinki-Vantaa airport in celcius with one decimal point
- `forecast`, which gives a plotted forecast of the next x hours specified as `forecast x`
- `history`, which gives a plot of the last ? hour temperatures

Other notable features include:
- Automatical scaling of the plot temperature axis

### **Diary**

22.11.2023:
- Project created
- Some initial setups done
    - Possibly all necessary files created
    - Telegram API connection and `start` command
    - Weather API key created
    - Everything is working in GitHub
- What next:
    - Get weather API requests running
        - Maybe easiest to start from `temperature` command
    - Start thinking about plots
- Useful links:
    - [Python API tutorial](https://www.dataquest.io/blog/python-api-tutorial/)
    - [WeatherAPI Docs](https://www.weatherapi.com/docs/)
    - [TGBot tutorial and docs](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot)
    - [TGBot code snippets](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets)