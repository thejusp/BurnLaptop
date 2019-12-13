# BurnLaptop
#### (Research method 30.502)

A statistical analysis of five different brands of laptops with same specification to investigate which one performs better !!. This research work is done as a part of course Research Methods, Engineering Product Development Pillar
Singapore University of Technology and Design.
The database consist of temperature, noise and time stamps recorded from differnt laptops at same environment conditions.
### Method of Analysis 

The following statistical methods has been used for analysing the experiment data:
* ANOVA - (Analysis of Variance Test)
* Tukey Comparison

### Dependencies 

Following python modules are essential for running the scripts 
(Tested on Windows, OSX and Linux )
* matplotlib 
* numpy 
* scipy 
* pandas 
* pyaml
For Linux distributions you can install the dependencies using pip package installer 
```sh
$  sudo -H pip install pyaml
$  sudo -H pip install matplotlib 
$  sudo -H pip install scipy
$  sudo -H pip install pandas
```

For Importing the database python module: 

```py
import datastructure as ds
```

#### Configure your environment
You can set your path by changing the parameters on yaml file inside scripts DIR :
```yaml 
Platform:      "Linux"
DatabaseDIR:   "/home/User/BurnLaptop/Database"
file_pattern:  "csv"
epoch:         2
endtime:       12
```

##### Developed by:
Nidhi Nagaraju |  Pathmakumar Thejus | Thein Than Tun
Sathian Pookkuttath | Samarakoon M Bhagya 


**&copy; 2019 Singapore University of Technology and Design **




