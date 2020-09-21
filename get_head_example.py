import urllib3
import sys
def header_example(attribute=None):
    http = urllib3.PoolManager() # Creating the PoolManager object, can be created into multiple threads
    r = http.request('HEAD', 'https://www.google.ca') # Only Grabs HTTP Header Metadata, Stored as a Dictionary
    try:
        if attribute is not None:
            print(r.headers[f'{attribute}']) # Matches 'attribute' key with it's content
        else:
            print(r.headers)
    except KeyError:
        print('Bad Header Key!') #Exception if Key doesn't exist
    except:
        print("Unexpected Error: ", sys.exc_info()[0]) # Any Generic Error

header_example(attribute_argument_placeholder) # Call to function, requires an argument, which is the attribute that you want to display.
