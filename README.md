![My Post(1)](https://user-images.githubusercontent.com/65361748/120073861-6c55f000-c09a-11eb-82fd-58c42e8c02e2.png)


**version 1.0.0**

The readme file explains how to run the Powerplant Energy Calculator software on your computer smoothly.

## Instalation


**Ubuntu Pre-requirements:**

Install Docker [click here](https://docs.docker.com/engine/install/ubuntu/)

Ubuntu 20.04+

**Ubuntu:**

Download and extract the application on your computer by clicking [here](https://github.com/ernesto03/powerplantenergycalculator/archive/refs/heads/main.zip).

Open Terminal

Go into the map of the application.
```sh
cd powerplantenergycalculator-main
```
Build the docker image for this app by running the command. Replace *nameapp* with a name of your chosing.
```sh
sudo docker build -t nameapp .
```
Run the docker image and replace *nameapp* by the name you've chosen when building the image
```sh
sudo docker run -p 8888:8888 nameapp
```
Now the application is running on your computer.

Read the next chapter **Usage** to understand how it works.
Enjoy!


## Usage

As the app is now running on your computer inside a docker image, open your browser.

Create a .json file on your computer and use the following structure.
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


Write this address inside your browser 
```
http://localhost:8888/productionplan
```



## Aditional info


## Contributions


## Lisence and copyright

© Ernest Lassman Kayembe *aka* chulolinux
