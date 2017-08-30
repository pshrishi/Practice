#!/usr/bin/python
import re 
from mechanize import Browser
br = Browser()

# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

# Retrieve the Google home page, saving the response
br.open( "https://www.connectorride.com/Account/Login" )

# Select the search box and search for 'foo'
br.select_form(nr=0)
br.form[ 'UserName' ] = 'GIPATIL'
br.form[ 'Password' ] = 'Ar3eN@!Fc'

# Get the search results
br.submit()
'''
res = br.follow_link("https://www.connectorride.com/Flex/oneTimeFlex")
content = res.read()
with open("/Users/pshrishi/Workspace/Nodejs/mechanize_results.html", "w") as f:
    f.write(content)
'''

# Find the link to foofighters.com; why did we run a search?
resp = None
for link in br.links():
    siteMatch = re.compile( 'oneTimeFlex' ).search( link.url )
    if siteMatch:
        resp = br.follow_link( link )
        break

# Print the site
content = resp.get_data()
with open("/Users/pshrishi/Workspace/Nodejs/mechanize_results.html", "w") as f:
    f.write(content)