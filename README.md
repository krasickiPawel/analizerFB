# Messenger Analyzer

This application allows you to analyze statistics on what you write with your friends on messenger and what specific people write in group conversations

## Description

This project requires a lot of security fixes that will come over time and will reduce the risk of doing something wrong and destabilizing the program. By following the instructions in <a href="#usage">Usage</a> section, everything works fine. The assumption is to download a JSON file with a copy of Facebook messages data, unpack it, then run the program and select the appropriate folder for analysis, and then select the statistics you are interested in. Closing a given window starts another one. If the word "processing" changes its color from green to black, it means that all the graphs have been presented and you can close the main program window.

## Build With
* Python 3.9
* Matplotlib 
* Tkinter

## Getting Started

Make sure you have python 3.9 or higher installed.

You can get it here:
https://www.python.org/downloads/

For the use of the program to make sense, you also need a JSON file from Facebook for analysis. See the <a href="#usage">Usage</a> section to find out how to download it.

### Installing

1. Clone the repo
   ```sh
   git clone https://github.com/krasickiPawel/analyzeFB.git
   ```
2. Install requirements
   ```sh
   pip install -r reqirements.txt
   ```

### Executing program

   ```sh
   python main.py
   ```

## Usage

### 1. Download JSON from Facebook

Download conversation data from [**here**](https://www.facebook.com/dyi/?referrer=yfi_settings).

Data format needs to be in **JSON**.
For smaller file (and faster request process) select **low quality** media (if you don't want photos and videos from groups for personal use) and select only messages. Select the date range you are interested in and request the downloads. Depending on the number of messages and the selected date range, this process may take from a few minutes to a ball of days, even over a week.

### 2. Download and unpack zip file(s)

### 3. Execute program using **python main.py** command in appropriate directory or by using IDE eg PyCharm (which is always safer in the event of a program crash)

### 4. decide if you want to analyze conversations from your entire facebook <a href="#41-all-conversations">4.1</a> or just a single given conversation <a href="#42-specific-conversation">4.2</a>

#### 4.1 All conversations

Select directory named **inbox** in the messages folder where you extracted the file.

#### 4.2 Specific conversation

Select the desired conversation directory in the inbox folder in the messages folder where you extracted the file.

### 5. Choose what you want to analyze by clicking on the intuitive buttons and observe the charts. They are displayed sequentially, one after the other, each next after closing the current window.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Recommendations

Similar projects
* [PWr W4 ITE Messenger statistics by Byczax](https://github.com/Byczax/messenger_graphs_statistics)
* [Mine and KrystianOg project, which is an open API (web app) written in Django, doing the same as the project presented above]()
