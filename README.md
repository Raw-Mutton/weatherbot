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

25.1.2024:
Almost 2 months since last edits yikes... Lots of schoolwork so less time for personal projects.

- Created first version of fetcing historical hourly temperatures
    - Currently works for only a set date (= 24.1.2024)
    - Returns it into Telegram as a list of 24 values
    - No custom filter yet
- What next:
    - History from list representation to a plot!
    - Seems the API only gives history of one single day? I can work with that I guess.

30.11.2023:
- Created first versions of `get_current_data()` and `get_temperature()`
- Created a first (but working!) version of the Bot's `\temperature`-command & `temperature`-text
    - Fiddled a long time with custom filters
- What next:
    - Temperature return text looks stupid
    - Plots?
    - Also other fun info from the weather API?
    - What is the location of the weather data??? Original bot uses HEL airport?
- Useful links:
    - [Example bot in GitHub](https://github.com/91DarioDev/forwardscoverbot)

29.11.2023:
- Testing Weather API
    - Got it to return JSON information correctly

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