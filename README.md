# Pironman 5 Mini

Pironman Mini case

Quick Links:

- [Pironman 5 Mini](#pironman-5-mini)
  - [About Pironman 5 Mini](#about-pironman-5-mini)
  - [Links](#links)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Update](#update)
  - [Compatible Systems](#compatible-systems)
  - [Debug](#debug)
  - [About SunFounder](#about-sunfounder)
  - [Contact us](#contact-us)

## About Pironman 5 Mini

## Links

- SunFounder Online Store &emsp; <https://www.sunfounder.com/>
- Documentation &emsp; <https://docs.sunfounder.com/en/latest/>

## Installation

For systems that don't have git, python3 pre-installed you need to install them first

```bash
sudo apt-get update
sudo apt-get install git python3 -y
```

Execute the installation script

```bash
cd ~
git clone https://github.com/sunfounder/pironman5-mini.git
cd ~/pironman5-mini
sudo python3 install.py
```

## Usage

-

## Update

<https://github.com/sunfounder/pironman5-mini/blob/main/CHANGELOG.md>

## Compatible Systems

Systems that passed the test on the Raspberry Pi 5:
<font size=1>
<!-- https://apps.timwhitlock.info/emoji/tables/unicode#block-6c-other-additional-symbols -->
  | system |   is compatible ? |
  | :---   | :---:   |
  | Raspberry Pi OS Desktop - bookworm (32/64 bit) | &#x2705; |
  | Raspberry Pi OS lite - bookworm (32/64 bit) | &#x2705; |
  | Ubuntu Desktop 23.10 (64 bit) | &#x2705; |
  | Ubuntu Server 23.10 (64 bit) | &#x2705; |

</font>

## Debug

Debug commands

```bash
sudo /opt/pironman5-mini/venv/bin/pip3 uninstall sf_rpi_status -y
sudo /opt/pironman5-mini/venv/bin/pip3 install git+https://github.com/sunfounder/sf_rpi_status.git

cd ~/pironman5-mini
sudo /opt/pironman5-mini/venv/bin/pip3 uninstall pironman5-mini -y
sudo /opt/pironman5-mini/venv/bin/pip3 install .

cd ~/pm_auto
sudo /opt/pironman5-mini/venv/bin/pip3 uninstall pm_auto -y
sudo /opt/pironman5-mini/venv/bin/pip3 install .

cd ~/pm_dashboard
sudo /opt/pironman5-mini/venv/bin/pip3 uninstall pm_dashboard -y
sudo /opt/pironman5-mini/venv/bin/pip3 install .

sudo systemctl stop pironman5-mini.service
sudo systemctl start pironman5-mini.service
sudo systemctl restart pironman5-mini.service
sudo pironman5-mini start
```

## About SunFounder
SunFounder is a company focused on STEAM education with products like open source robots, development boards, STEAM kit, modules, tools and other smart devices distributed globally. In SunFounder, we strive to help elementary and middle school students as well as hobbyists, through STEAM education, strengthen their hands-on practices and problem-solving abilities. In this way, we hope to disseminate knowledge and provide skill training in a full-of-joy way, thus fostering your interest in programming and making, and exposing you to a fascinating world of science and engineering. To embrace the future of artificial intelligence, it is urgent and meaningful to learn abundant STEAM knowledge.

## Contact us
website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com
