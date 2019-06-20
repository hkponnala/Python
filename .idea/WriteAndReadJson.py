# This example narrates file IO and JSON formatted interface.
# I have leveraged JSON package.

import json

FileName = 'C:/Users/hkpon/DataFiles/Json/data.json'
data = {}

# Define subroutine - prepare JSON
# Instantiate a JSON object.
def PrepareJson():
    data['Family'] = []
    data['Family'].append({
        'First Name': 'Augustine',
        'Last Name': 'Washington',
        'Gender': 'Male'
    })
    data['Family'].append({
        'First Name': 'Mary Ball',
        'Last Name': 'Washington',
        'Gender': 'Female'
    })
    data['Family'].append({
        'First Name': 'George',
        'Last Name': 'Washington',
        'Gender': 'Male'
    })

# Open a file to write and output the JSON object to the file.
def WriteJson():
    with open(FileName, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()

# Open the file to read the JSON file.
def ReadJson():
    with open(FileName) as json_file:
        data = json.load(json_file)
        for p in data['Family']:
            print('First Name: ' + p['First Name'])
            print('Last Name: ' + p['Last Name'])
            print('Gender: ' + p['Gender'])
            print('')
        json_file.close()

# Call subroutines
try:
    print ('1. Prepare Json File')
    PrepareJson()
    print ('2. Write Json File')
    WriteJson()
    print ('3. Read Json File')
    ReadJson()

# Handle exceptions if any
except IOError as e :
    print ("IO exception encountered : ", e)
else:
    print ("Script completed successfully!")
finally:
    print ('End of Program!')