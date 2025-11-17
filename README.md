# DIY Pro Extension
## Human Computer Interaction -- Olin College of Engineering -- Fall '25
### Lily Wei, Trinity Lee, Kelsey McClung, AJ Bulow, Charlie Mawn

# Running The Extension:
- Download this repo to your local device
- Open your chrome extensions tab (chrome://extensions)[chrome://extensions] (you might need to type this into a tab yourself, as chrome:// is usually not linkable)
- Turn on developer mode
- Click 'load unpacked'
- Select the this downloaded directory to load
- Open the extension by opening your extensions menu, and selecting the DIY Pro extension

# Running The Website
- Run `pip install django` to install the django web framework
- After installing, `cd` into the `diy_pro_website` directory
- Once inside `diy_pro_website`, run `python manage.py runserver`. This will start up a local server.
- With the local server running, all buttons on the extension will correctly redirect to our website. If this isn't running, redirects to the website will show errors.
- Once finished, use `ctrl + c` to close the local server. Note: this is needs to be running 

