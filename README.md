![My Post(1)](https://user-images.githubusercontent.com/65361748/120073861-6c55f000-c09a-11eb-82fd-58c42e8c02e2.png)


**version 1.0.0**

The readme file explains how to run the Powerplant Energy Calculator software on your computer smoothly.

## Instalation


**Ubuntu Pre-requirements:**

Install Docker [click here](https://docs.docker.com/engine/install/ubuntu/)

Ubuntu 20.04+

**Windows Pre-requirements:**

Install Docker [click here](https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-10)

The system will install WSL2, set it as default version. Instructions [click here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package)

Windows 10

**Ubuntu:**

Download the application on your computer by clicking [here](https://github.com/ernesto03/powerplantenergycalculator/archive/refs/heads/main.zip).

Extract the application folder
```sh
unzip powerplantenergycalculator-main.zip
```
Open Terminal

Go into the extracted folder
```sh
cd powerplantenergycalculator-main
```
Build the docker image for this app by running the command. Replace *$nameimage* with a name of your chosing
```sh
sudo docker build -t $nameimage .
```
Run the docker image and replace *$nameimage* by the name you've chosen when building the image
```sh
sudo docker run -p 8888:8888 $nameimage
```
Now the application is running on your computer

Read the next chapter **Usage** to understand how it works

Enjoy!

**Windows:**

Download the application on your computer by clicking [here](https://github.com/ernesto03/powerplantenergycalculator/archive/refs/heads/main.zip).

Extract the application folder with WinZip or WinRar

Run Docker Desktop

Open Command-prompt / Run as administrator

Go into the extracted folder via command-prompt
```sh
cd powerplantenergycalculator-main
```
Build the docker image for this app by running the command. Replace *$nameimage* with a name of your chosing
```sh
docker build -t $nameimage .
```
Run the docker image and replace *$nameimage* by the name you've chosen when building the image
```sh
docker run -p 8888:8888 $nameimage
```
Now the application is running on your computer

Read the next chapter **Usage** to understand how it works

Enjoy!

## Usage

As the app is now running on your computer inside a docker image, open your browser

Create a *.json* file by copy and pasting the following code, and save it on your computer

**Only use the following structure/layout.**
**Do not change the structure/layout in any way.**

**Do not change the keys. The keys are before the ':' .**

example: "load", "fuels","gas", "powerplants", "name",..

**Do not change all the values. Values are after the ':'**

example: "500", "13.4", "460", "gasfired", "tj1,..

**Only the VALUES of the following keys can be changed: "load", "wind", "gas", "kerosine", "co2", "efficiency", "pmin", "pmax"**

```json
{
  "load": 500,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 100
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 160
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
}
```


Write the following address inside your browser 
```
http://localhost:8888/productionplan
```

Click on "Browse" in the select a file box

![uploadfilebox](https://user-images.githubusercontent.com/65361748/120082510-c28b5900-c0c3-11eb-89f7-a0065bb043b6.png)

Select the .json file you just created

Click on the blue button *Upload*.

You will be redirected to the page with the calculated powerplantplan

**Windows:**

To stop the application, use docker desktop.

**Ubuntu:**
To stop the application from running, use the following command to find the containerID which runs the application
```sh
sudo docker ps
```
output

![containerlisting](https://user-images.githubusercontent.com/65361748/120083887-32054680-c0cc-11eb-9314-0235fe99238d.png)

Now you can write the following command with the *$containerID* to stop the container and image from running
```sh
sudo docker stop $containerID
```
## Aditional info

It is possible to extract a log file

Use the following command an replace $filepath with *appRuntimeMonitor.log* and $output_path with a path to the file you want to save the log

example $output_path: ~/Desktop/log.txt

**ubuntu:**
```sh
sudo docker run $appimage cat $file_path > $output_path
```
**windows:**
```sh
docker run $appimage cat $file_path > $output_path
```

## Contributions

For contributions please send me a message on twitter first.

## Lisence and copyright

© Ernest Lassman Kayembe *aka* chulolinux
