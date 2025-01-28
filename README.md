# Instagram-Followers
A light weight program that let's you see which users don't follow you back and which users you don't follow back. The data are imported manually by requesting your them from Meta. The program only proccess them locally.

Python Requirement:

You must have Python installed to run this program.
If you don't have Python installed, you can download it from https://www.python.org/downloads/.


How to Get your data from Meta

1) Go to your instagram account.
2) Open Settings (3 horizontal bars at the top right).
3) Go to Accounts center.
4) Go to Your information and permissions.
5) Download your information.
6) Download or transfer information.
7) If you have multiple accounts (like Facebook) choose only the instagram one and click Next.
8) Choose "Some of your information".
9) Mark as ticked only the checkbox "Followers and following". (You need to scroll a little and it is under Connections section).
10) You can choose either to Download to Device or transfer it (mostly using Google Drive).
11) Whatever you chose at Step 10, make sure that the settings you choose now are: Date Range = All time, Format = JSON, Media Quality = High.
12) Click Create Files.
13) You will get notified when the files will be available for download. (In my experience, they were available in less than a couple of hours).
14) When the files (a .zip folder) are delivered to you go to your PC/Laptop and exctract it. (If you chose "Download to device" instead of "Transfer" in Step 6, you need to navigate to the window at Step 4 and there will be your files waiting for you to download).


Instructions to Run the Program

1) Prepare the Input Files:

- Copy the following.json and followers_1.json files and paste them to the "data" folder of this repository release (You have already extracted the release package).
- Rename the files and make sure that they are named EXACTLY as followers.json and following.json, into the "data" folder.

2) Run the Program:

- Execute the program.py file.

3) View the Results:

- The results will appear in the command window.

*The output files can also be found in the "generated" folder.