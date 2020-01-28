import zipcodes
import json

if __name__ == '__main__':
    zipcode_info = []
    for info in zipcodes.list_all():
        if (float(info['lat']) and float(info['long'])):
            zip_tuple = [
                info['zip_code'],
                info['state'],
                info['lat'],
                info['long'],
            ]
            zipcode_info.append(zip_tuple)
    print(json.dumps(zipcode_info))
