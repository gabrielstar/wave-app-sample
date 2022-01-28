from h2o_wave import site, ui

# Your Wave server instance holds a collection of pages.
# To change a page, simply grab a reference to a page, change it, and save it.
# Grab a reference to the page at route '/hello'

page = site['/hello']  # site is a dictionary of all the pages at wave server

# Add a markdown card to the page.
page['quote'] = ui.markdown_card(  # page is collection of cards
    box='1 1 2 2',
    title='Hello World chnaged',
    content='"The Internet? Is that thing still around?" - *Homer Simpson*',
)

# Finally, save the page.balck setup.cfg spe
page.save()  # this will broadcast our chaneg to all connected browsers
