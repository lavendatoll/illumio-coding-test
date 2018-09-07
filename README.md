#Illumion Coding Assignment

A simplified firewall model.
This model determines the fate of a packet by checking whether the input is supported.

##Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

###Prerequisites
python version >= 3.5
numpy and pandas
```
pip3 install pandas
pip3 install numpy
```

##Running the test

```
cd Illumio_Coding_Test/version1
python3 test.py

cd Illumio_Coding_Test/version2
python3 test.py
```

## Interesting Design

For version1: naive version
In my code, I employed python library pandas to deal with rules.csv
I used pd.read_csv to load the entire rule file and processed it in advance.
I splited the 'port' to 'startport' and 'endport' by '-' and added them back to the datafame. I did same for 'ip_address'.
Then I could select in my accept_packet function based on all inputs.

After finishing it quickly, I started to think how should I do if the rule file is very large.
Then I revised it to version2.
In version 2, I readed the rule file chunk by chunk which cound be defined in advance.

Then I processed chunk by chunk. I trimed my current dataframe by selecting a condition once every time and tried to make the code run fast.
