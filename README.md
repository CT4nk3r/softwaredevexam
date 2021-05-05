# softwaredevexam

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
2021 Május 5.-én reggel tíz órakor nekiültem ennek a feladatnak, eleinte sok düh és még annál is több energiaital kellett, viszont büszke vagyok magamra, és arra amit képes voltam összehözni.

A program alapvetően amikor megnyílik akkor kér egy számot a felhasználótol, ami azt dönti el, hogy melyik képen fogjuk végrehajtani a folyamatot.
Az egész program nagyon szépen végigsuhan mind a 3 JSON fájlon és megnézi melyikben található  a mi általunk keresett képnek az adatai. Ezeket az adatokat felhasználva pedig négyzetekkel be is jelöli a hibákat a PDF-ben látható módon.

Miután végez a program a kép szerkesztésével, utána felugrik nekik egy ablakban (vicces módon az első található python képszerkesztőt használtam amit a kereső mutatott https://www.w3schools.com/python/matplotlib_intro.asp ugyanis ezt már ismerősökkel használtuk Párhuzamos Programozás órán is)

## Technologies
Project is created with:
* Python version: 3.8.7 :snake:
* pip: 21.0.1
* matplotlib 3.4.1


## Setup
To run this project, install a running enviroment for python.
First of all, we have to install Python from [here](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe).
Now we have to use python to download the modules that we need, mainly we are using matplotlib. 
Open up the python terminal and type in to download discordpy: `python -m pip install -U matplotlib`

If you happen not to have pip -> `python -m pip install -U pip` <- ez updateolni fogja majd a pip-ünket és remélhetőleg lehet majd látni
