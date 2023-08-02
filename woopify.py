import pandas as pd
import sys
import re

def clean_str(string):
    special_characters = re.compile(r"[^\w\s]+")
    string = special_characters.sub("", string)
    return string

def clear_newlines(string):
	string = string.replace("\\n", "")
	return string

def divide_dataframe(dataObj, size):
	dfList = []
	frequence = int(len(dataObj.get('Title'))/size)
	mem = 0
	for f in range(frequence):
		lst = []
		for i in range(f*size + (mem - f*size), size*(f+1)):
			obj = {}
			for key, value in dataObj.items():
				obj[key] = value[i]
			lst.append(obj)
		i = size*(f+1)
		while i < len(dataObj.get('Title')) and dataObj.get('Title')[i] == '':
			obj = {}
			for key, value in dataObj.items():
				obj[key] = value[i]
			lst.append(obj)
			i = i+1
		mem = i
		dfList.append(pd.DataFrame(lst))
	return dfList
	

if (len(sys.argv) not in range(2, 4)):
    print('Enter the wooComerce csv path.')
    sys.exit()


prods = pd.read_csv(sys.argv[1])

shopyData = {
	'Handle': [],
	'Title': [],
	'Body (HTML)': [],
	'Vendor': [],
	'Product Category': [],
	'Type': [],
	'Tags': [],
	'Published': [],
	'Option1 Name': [],
	'Option1 Value': [],
	'Option2 Name': [],
	'Option2 Value': [],
	'Option3 Name': [],
	'Option3 Value': [],
	'Variant SKU': [],
	'Variant Grams': [],
	'Variant Inventory Tracker': [],
	'Variant Inventory Qty': [],
	'Variant Inventory Policy': [],
	'Inventory Policy': [],
	'Fulfillment Service': [],
	'Variant Fulfillment Service': [],
	'Variant Price': [],
	'Variant Compare At Price': [],
	'Variant Requires Shipping': [],
	'Variant Taxable': [],
	'Variant Barcode': [],
	'Image Src': [],
	'Image Position': [],
	'Image Alt Text': [],
	'Gift Card': [],
	'SEO Title': [],
	'SEO Description': [],
	'Google Shopping / Google Product Category': [],
	'Google Shopping / Gender': [],
	'Google Shopping / Age Group': [],
	'Google Shopping / MPN': [],
	'Google Shopping / AdWords Grouping': [],
	'Google Shopping / AdWords Labels': [],
	'Google Shopping / Condition': [],
	'Google Shopping / Custom Product': [],
	'Google Shopping / Custom Label 0': [],
	'Google Shopping / Custom Label 1': [],
	'Google Shopping / Custom Label 2': [],
	'Google Shopping / Custom Label 3': [],
	'Google Shopping / Custom Label 4': [],
	'Variant Image': [],
	'Variant Weight Unit': [],
	'Variant Tax Code': [],
	'Cost per item': [],
	'Price / International': [],
	'Compare At Price / International': [],
	'Status':[]
}

for row in prods.iloc:
	length = len(row['Images'].split(','))
	if length >= 1:
		shopyData.get('Image Src').append(row['Images'].split(',')[0])
		shopyData.get('Title').append(row['Name'])
		shopyData.get('Handle').append('_'.join(clean_str(str(row['Name'])).lower().split(' ')))
		shopyData.get('Body (HTML)').append(clear_newlines(row['Description']))
		shopyData.get('Tags').append(row['Tags'])
		shopyData.get('Vendor').append('')
		shopyData.get('Type').append('')
		shopyData.get('Product Category').append('')
		shopyData.get('Option1 Name').append('')
		shopyData.get('Option1 Value').append('')
		shopyData.get('Option2 Name').append('')
		shopyData.get('Option2 Value').append('')
		shopyData.get('Option3 Name').append('')
		shopyData.get('Option3 Value').append('')
		shopyData.get('Variant SKU').append('')
		shopyData.get('Variant Grams').append('')
		shopyData.get('Variant Inventory Tracker').append('')
		shopyData.get('Variant Inventory Qty').append('')
		shopyData.get('Variant Inventory Policy').append('deny')
		shopyData.get('Inventory Policy').append('deny')
		shopyData.get('Fulfillment Service').append('manual')
		shopyData.get('Variant Fulfillment Service').append('manual')
		shopyData.get('Variant Price').append(row['Regular price'])
		shopyData.get('Variant Compare At Price').append(int(row['Regular price']) + int(row['Regular price'])*.3)
		shopyData.get('Variant Requires Shipping').append('')
		shopyData.get('Variant Taxable').append('')
		shopyData.get('Variant Barcode').append('')
		shopyData.get('Image Position').append('1')
		shopyData.get('Image Alt Text').append('')
		shopyData.get('Gift Card').append('')
		shopyData.get('SEO Title').append(row['Name'])
		shopyData.get('SEO Description').append(row['Name'])
		shopyData.get('Google Shopping / Google Product Category').append('')
		shopyData.get('Google Shopping / Gender').append('')
		shopyData.get('Google Shopping / Age Group').append('')
		shopyData.get('Google Shopping / MPN').append('')
		shopyData.get('Google Shopping / AdWords Grouping').append('')
		shopyData.get('Google Shopping / AdWords Labels').append('')
		shopyData.get('Google Shopping / Condition').append('')
		shopyData.get('Google Shopping / Custom Product').append('')
		shopyData.get('Google Shopping / Custom Label 0').append('')
		shopyData.get('Google Shopping / Custom Label 1').append('')
		shopyData.get('Google Shopping / Custom Label 2').append('')
		shopyData.get('Google Shopping / Custom Label 3').append('')
		shopyData.get('Google Shopping / Custom Label 4').append('')
		shopyData.get('Variant Image').append('')
		shopyData.get('Variant Weight Unit').append('')
		shopyData.get('Variant Tax Code').append('')
		shopyData.get('Cost per item').append('')
		shopyData.get('Price / International').append(row['Regular price'])
		shopyData.get('Compare At Price / International').append(int(row['Regular price']) + int(row['Regular price'])*.3)
		shopyData.get('Status').append('active')
		if (row['Visibility in catalog'] == 'visible'):
			shopyData.get('Published').append('TRUE')
		else:
			shopyData.get('Published').append('FALSE')
	if length > 1:
		for i in range(1, length):
			shopyData.get('Image Src').append(row['Images'].split(',')[i])
			shopyData.get('Title').append('')
			shopyData.get('Handle').append('_'.join(clean_str(str(row['Name'])).lower().split(' ')))
			shopyData.get('Body (HTML)').append('')
			shopyData.get('Tags').append('')
			shopyData.get('Vendor').append('')
			shopyData.get('Type').append('')
			shopyData.get('Product Category').append('')
			shopyData.get('Option1 Name').append('')
			shopyData.get('Option1 Value').append('')
			shopyData.get('Option2 Name').append('')
			shopyData.get('Option2 Value').append('')
			shopyData.get('Option3 Name').append('')
			shopyData.get('Option3 Value').append('')
			shopyData.get('Variant SKU').append('')
			shopyData.get('Variant Grams').append('')
			shopyData.get('Variant Inventory Tracker').append('')
			shopyData.get('Variant Inventory Qty').append('')
			shopyData.get('Variant Inventory Policy').append('')
			shopyData.get('Inventory Policy').append('')
			shopyData.get('Fulfillment Service').append('')
			shopyData.get('Variant Fulfillment Service').append('')
			shopyData.get('Variant Price').append('')
			shopyData.get('Variant Compare At Price').append('')
			shopyData.get('Variant Requires Shipping').append('')
			shopyData.get('Variant Taxable').append('')
			shopyData.get('Variant Barcode').append('')
			shopyData.get('Image Position').append(str(i+1))
			shopyData.get('Image Alt Text').append('')
			shopyData.get('Gift Card').append('')
			shopyData.get('SEO Title').append('')
			shopyData.get('SEO Description').append('')
			shopyData.get('Google Shopping / Google Product Category').append('')
			shopyData.get('Google Shopping / Gender').append('')
			shopyData.get('Google Shopping / Age Group').append('')
			shopyData.get('Google Shopping / MPN').append('')
			shopyData.get('Google Shopping / AdWords Grouping').append('')
			shopyData.get('Google Shopping / AdWords Labels').append('')
			shopyData.get('Google Shopping / Condition').append('')
			shopyData.get('Google Shopping / Custom Product').append('')
			shopyData.get('Google Shopping / Custom Label 0').append('')
			shopyData.get('Google Shopping / Custom Label 1').append('')
			shopyData.get('Google Shopping / Custom Label 2').append('')
			shopyData.get('Google Shopping / Custom Label 3').append('')
			shopyData.get('Google Shopping / Custom Label 4').append('')
			shopyData.get('Variant Image').append('')
			shopyData.get('Variant Weight Unit').append('')
			shopyData.get('Variant Tax Code').append('')
			shopyData.get('Cost per item').append('')
			shopyData.get('Price / International').append('')
			shopyData.get('Compare At Price / International').append('')
			shopyData.get('Status').append('')
			if (row['Visibility in catalog'] == 'visible'):
				shopyData.get('Published').append('')
			else:
				shopyData.get('Published').append('')
	if length == 0:
		print('The products must have at least one image each.')
		sys.exit()



if (len(sys.argv) == 3):
	n = int(len(shopyData.get('Title')) / (int(sys.argv[2])))
	list_df = divide_dataframe(shopyData, n)
	for i in range(0, len(list_df)):
		list_df[i].to_csv('shopify'+str(i+1)+'.csv', index=False)
else:
	dataFrame = pd.DataFrame(shopyData)
	dataFrame.to_csv('shopify.csv', index=False)

print("DONE CONVERTING!")