# <img src="icons/logo.png" alt="logo" width="32"> Touchydo Bot

[![Python](https://img.shields.io/badge/python%20%3E%3D-3.0-blue.svg)](https://www.python.org/)
[![GTK](https://img.shields.io/badge/gtk-3.0-brightgreen.svg)](https://www.gtk.org/)
[![OS](https://img.shields.io/badge/os-Linux-orange.svg)](https://www.ubuntu.com/download/desktop)

Farming bot for Dofus Touch game written in python & [GTK](https://www.gtk.org/).

THIS IS A PORT OF [DINDO-BOT](https://github.com/Gamerium/Dindo-Bot/) FOR DOFUS TOUCH, THANKS A LOT TO AXEL !! (License [here](https://github.com/malikhattabi/Touchydo-bot/blob/master/LICENSE))

I left the original fork network because this project is not going to the same direction as Dindo-bot (dindo is for dofus on PC).

[![screenshot](screenshot.png)](http://www.youtube.com/watch?v=1Qh_eNLuTYo "Watch Dindo-bot in action")

> What's a bot?

A bot is a software that emulates a real game client in order to automate some tasks. Dindo is a **pixel** bot, which means that it uses screen pixels (+ your mouse & keyboard) to emulate actions & keep tracking the progress in game.

:warning: Better know that this bot is only available on [Linux](https://www.wikipedia.org/wiki/Linux) for now.

## Features

- **Easy control**: play, pause/resume or stop the bot like if you were using your favorite music player.
- **Smart bot**: Dindo knows when your connection turns off and will wait for it to get back before proceeding or will automatically pause itself if it takes a long time.
- **Multi accounts management**: you don't have to worry about switching between your accounts, Dindo can handle that for you :wink:.
- **Integrated Path & Maps builder**: easily create your own custom paths & farming maps.
- **Keyboard shortcuts**.

## Use Cases

- Auto-connect to your Dofus account(s).
- Move around the map & save time for long dungeon paths, [paths](paths) pull requests are welcome :pray:.
- Farming & jobs (:construction: this part still needs to be improved, also, the bot cannot handle fights yet :warning:).
- Automated actions like flood :speech_balloon:.

## Installation

For now just don't it's not ready AT ALL.

First, clone this repository using git or just [download](https://github.com/AXeL-dev/Dindo-Bot/archive/master.zip) & unzip it:

<details>
  <summary>git installation</summary>
  
  ```bash
    sudo apt install git
  ```
</details>

```bash
git clone https://github.com/AXeL-dev/Dindo-Bot.git
```

Then, open a terminal & launch the installation script as below:
```bash
cd /path/to/bot
chmod +x install.sh
sudo ./install.sh
```

Once installed, you can run the bot from your app launcher or using the command below:
```bash
dindo-bot
```

## Tutorials

- [Farming tutorial](https://www.youtube.com/watch?v=obGDT9_AXvk)

## To Know

- You cannot use your computer for something else while Dindo is running.
- Since the bot simulates normal human behavior, you have less chances to get spotted by the Anti-bot (less is not 0).
> Tips: For more safety, try changing bot paths from time to time.
- The main goal of this bot is to simplify repetitive tasks and reduce boredom during your gameplay.
- We do not encourage multi-boting and do not support it anyway (it destroys the server economy :grimacing:).
- On Linux, Wayland is currently not supported so you will need to use X11 [#2](https://github.com/malikhattabi/Touchydo-bot/issues/2).
- Windows & Mac OS are not ~~yet~~ supported [#1](https://github.com/AXeL-dev/Dindo-Bot/issues/1) [#8](https://github.com/AXeL-dev/Dindo-Bot/issues/8).

## Version History

- There is only one for now, it's the master branch.

## Contributing

Want to contribute? Check the [todo list](todo.md). You may also read the [contributing guidelines](https://github.com/malikhattabi/contributing).

## Donations

Personally I don't really want donations I just love what I do, but if you have some bucks to donate, you may wanna look at those charities below (if you send me a screenshot of your donation by mail I'll be the happiest on earth).

[MSF](https://www.msf.org/donate)
[ICRC](https://www.icrc.org/en/donate)
[UNRWA](https://donate.unrwa.org/int/en/general)

Thanks :heart:

## License

Touchydo-Bot is licensed under the [MIT](LICENSE) license.
