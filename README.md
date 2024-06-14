1. Create a folder on your Desktop named "PhotoExport"
2. Download the installPhotos.py file to your PhotoExport folder, located on your desktop
3. Locate the Install Photos form in Coperniq that you want to extract photos from, click on the form, at the top right click Export, Only Photo Fields, PDF, Export
4. Save this new PDF into your PhotoExport folder on your desktop
5. Hold the `Windows + R` on your keyboard to pull up the "Run" window.
6. Type CMD in the box then click "Okay"
7. Type the following then hit enter: python --version
8. If it gives you your current Python version, proceed to step 15. If not, go to step 9.
9. Download the Python installer from https://python.org/downloads
10. Open the installer and click the checkbox that says "Add Python to Path" then click next and install it
11. Open Notepad by searching for it in the windows search bar
12. In Notepad, click File -> Open and change the file type at the bottom right from .txt files to All Files, then navigate to your PhotoExport folder in the Desktop and click on your installPhotos.py file
13. Hit `CTRL + F` on your keyboard and search for the following: Set the PDF
14. Below this line, there should be a line that reads something similar to: pdf_name = "YOUR PDF's NAME HERE"
15. Replace the text inside the quotes with the name of your PDF and save the file. You can hit `CTRL + S` to save
17. Open your PhotoExport folder, click once on your installPhotos.py file and press `Alt + Enter`
18. Look for the "Location:" and copy the location. It should look something like this: \Users\brighthouse\OneDrive\Desktop\Brighthouse\PhotoExport
19. Hit `Windows + R` again and open the CMD again.
20. In the window that pops up, type what's in these quotes exactly "cd C:" then hit paste.
21. You should end up with it saying something like: cd C:\Users\brighthouse\OneDrive\Desktop\Brighthouse\PhotoExport. If it looks like this, hit enter
22. After hitting Enter, it should start a new line that reads "C:\Users\brighthouse\OneDrive\Desktop\Brighthouse\PhotoExport" with a cursor blinking waiting for you to type
23. If this isn't the case, try from step 18 again.
24. If this is the case, type the following and hit enter: python installPhotos.py
25. It should start pulling those photos. They will be placed into a folder in your PhotoExport folder.
26. If it doesn't work, contact Keaton
