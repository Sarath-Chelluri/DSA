'''
Question 2 : Game Of Clicks (R->Hard)
Problem Statement  :

Sahil watches TV all day and gets bored. He started playing this dumb game of identifying minimum number of inputs needed to reach a channel. As his cousin, you have to help him, but you live far from his house. So you decide to write a code that will ask Sahil for some inputs and give outputs respectively.

Here are the problems you need to keep in mind :

There are 13 buttons on his remote: 10 buttons for the numbers (0-9) to form integers denoting respective channel index, “Up channel” button and “ Down channel” button for going i +1th channel and i-1th channel from i respectively, and a “Last viewed” button to see what’s the last channel before it.
The number buttons allow you to jump directly to a specific channel (Ex: to go to channel 172 by typing 1,7,2).
If the channel which you are in is ith and that is the max channel index possible, by Up channel, you will reach the first channel possible. Same goes for the down channel button. You can go to the highest channel possible if you go down from the lowest channel possible.
Sahil can get from one channel to the next in one of the two ways.
Sahil’s parents have set some parental control on some channels on Aniruth’s television. The “Up Channel “ and “Down buttons” buttons skip these channels as these channels are not viewable.
Given a list of channels to view, the lowest channel, the highest channel, and a list of blocked channels, your program should return the minimum number of clicks necessary to get through all the shows that Anirudh would like to match.
Input Format :

First line is the lowest Channel
Second-line is the highest Channel
Followed by a number of blocked channels B,
and the next B lines contain the actual blocked channels.
Followed by the number of Channels to view V, and the next V lines contain the actual channels to view.
Constraints :

The lowest channel on the television will be greater than 0. and less than or equal to 10,000.
The highest channel on the television will be greater than or equal to the lowest channel. and less than or equal to 10.000.
The list of channels that are blocked on Anirudh’s television. All the channels in this list will be valid channels (greater than or equal to lowest channel, less than or equal 1 to highest channel). Duplicates may be Ignored. The blocked list can be a maximum of 40 channels.
The sequence that Sahil must view contains between 1 and 50 elements. inclusive. All channels in this sequence are not in the blocked list and are between lowest channel and highest channel. Inclusive.
Sample Input 0:
1
20
2
18
19
5
15
14
17
1T
17
Sample output 0:
7
'''

def minimum_clicks(low,high,block,view):
    










low = int(input())
high = int(input())
num_block = int(input())
blocked = [int(input()) for i in num_block]

num_view = int(input())
views=[int(input()) for i in num_view]