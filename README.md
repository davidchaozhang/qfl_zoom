QFL online zoom registration and email notification
===================================================


1. QFL registration will receive data from online registration site:
rccc.org/gcamp
The data is logged in salesforce. The database outputs the following table format in csv:

 Chinese Name    English Name      Email Address      Church
  xxxxx  xxx      Elon Mask      elonmask@yahoo.com    RCCC
   .....
   
2. There will be manual effort to divide all registrants into groups. Coworkers will work
with other church coworkers. The updated csv table looks like this:
 
 Group Chinese Name    English Name      Email Address      Church
   1    xxxxx  xxx     Elon Mask      elonmask@yahoo.com    RCCC
   2    yyy  yyy       Peter Pan      peter.pan@gmail.com   PCC
   .....
   50    zzz zzz       Brian Adam     bdam@eccc.org         ECCC
   
We will divide them to up to 50 groups.
The saved file name is grouped_registrants.csv 

3. We will first generate a file that can import to zoom to setup breakout rooms. 
Each breakroom will contains a group of pre-assigned registrants. The breakout rooms csv 
file look like this:

Pre-assign Room Name,Email Address
1,elonmask@yahoo.com
2,peter.pan@gmail.com
50,bdam@eccc.org

Two columns: group id and email address, which are seperated by column. 
You need to keep the head (Pre-assign Room Name,Email Address) in the first row. 
The file name is breakout_room_assign.csv

Then the zoom admin will take this file, under "Breakout Room Pre-assign",import
"breakout_room_assign.csv", check if there is any error after import. 
Please disable email notification after the import is finished.Click save.

4. Run python scripts on "grouped_registrants.csv". Zoom meeting link is generated per registrant. 
The python scripts combine ground id, English Name, and Church initials into one word, 
and associate email address to the new display name. It also generate a new csv file that has the following format:

1,elonmask@yahoo.com,谌东,Elon Mask,NJ-RCCC-X教會,https://us02web.zoom.us/w/86941866544?tk=Q72REBJZ34INUFwY4qR1icMomR1y5czHGdQlC2FyojQ.DQIAAAAUPiOaMBYtQUhyWXQ2aVNsaXJkODJ6cEF2VUZBAAAAAAAAAAAAAAAAAAAAAAAAAAAA
2,peter.pan@gmail.com,黄健,Peter Pan,NJ-PCC-Y教會,https://us02web.zoom.us/w/86941866544?tk=hhhFNRUoCONdahKOcJfty8_GRCb48SvnW_EyCZjawkE.DQIAAAAUPiOaMBY4YmlkRDVBaFFZcWJYS3Zrb2l4MEd3AAAAAAAAAAAAAAAAAAAAAAAAAAAA
50,bdam@eccc.org,马彰,Brian Adam,MA-ECCC-Z教會,https://us02web.zoom.us/w/86941866544?tk=cccXqpmTiVQbz26eYT1yy66eqhRpi-83gvO_aMK8E7I.DQIAAAAUPiOaMBZWSWttaUItQ1MtU1NFM1R0VkdkeVlBAAAAAAAAAAAAAAAAAAAAAAAAAAAA
....

the file name is called "join_links.csv"

Disable any email notification from zoom since we will use MailChimp to send group emails.

5. Provide "join_links.csv" to the coworker in charge. (S)He will send out group emails to all registrants. 
The email is formatted to contains other information from the camp.  




