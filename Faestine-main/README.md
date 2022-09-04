# Faestine
Multi-purpose Discord bot ready to skill up and boost your server

---

## Public Instance
You can use the link below to invite the public instance to your server.
 * [Faestine](https://discord.com/api/oauth2/authorize?client_id=1006378744379883633&permissions=8&scope=bot%20applications.commands)

## Self Hosting Instructions
The following instructions are for those who wish to self host the bot.

### Requirements

 * **Python**: [3.8](https://www.python.org/downloads/)
 * **py-cord**

#### Windows

* Clone the bot repo to your device with `git clone https://github.com/NimbiDev/Faestine.git`
* Fill in the required fields in the `.env-example` file and then rename it to `.env`
* Create a virtual environment inside the root directory of the bot with `python3 -m venv pyenv`
* Activate the virtual environment with `pyenv\Scripts\activate.bat`th `python3 -m venv pyenv`
* Activate the virtual environment with `pyenv\Scripts\activate.bat`
* Install `py-cord` with `pip install -U py-cord`
* Install the requirements with `pip install -r requirements.txt`
* Run the bot with `python bot.py`

#### Linux

* Clone the bot repo to your device with `git clone https://github.com/NimbiDev/Faestine.git`
* Fill in the required fields in the `.env-example` file and then rename it to `.env`
* Create a virtual environment inside the root directory of the bot with `python3 -m venv pyenv`
* Activate the virtual environment with `source pyenv/bin/activate`
* Install `py-cord` with `pip install -U py-cord`
* Install the requirements with `pip install -r requirements.txt`
* Run the bot with `python bot.py`

---

### Notes

 * I suggest using either `pm2` or `tmux` if you wish to keep the bot running 24/7.
 * Refer to your OS or Distro instructions to learn how to install those.

---

![](assets/logo.png)