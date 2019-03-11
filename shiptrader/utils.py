import json

import requests
from django.utils.text import slugify

from shiptrader.models import Starship, Listing


class StrashipsImporter(object):

    def read_process_data(self):

        """
        This function get data from Straships and save them to db
        """
        for page_num in range(1, 5):
            url = "https://swapi.co/api/starships/?page={}".format(page_num)
            response = requests.get(url, verify=True)
            data = response.text
            parsed_data = json.loads(data)

            if page_num in [1, 2, 3]:
                loop_num = range(0, 10)
            else:
                loop_num = range(0, 7)

            for i in loop_num:
                starship = Starship.objects.create(
                    starship_class=parsed_data["results"][i]["starship_class"],
                    manufacturer=parsed_data["results"][i]["manufacturer"],
                    length=parsed_data["results"][i]["length"],
                    hyperdrive_rating=parsed_data["results"][i]["hyperdrive_rating"],
                    cargo_capacity=parsed_data["results"][i]["cargo_capacity"],
                    crew=parsed_data["results"][i]["crew"],
                    passengers=parsed_data["results"][i]["passengers"],
                    starship_class_slug=slugify(parsed_data["results"][i]["starship_class"])
                )
                Listing.objects.create(
                    name=parsed_data["results"][i]["name"],
                    ship_type=starship,
                    price=parsed_data["results"][i]["cost_in_credits"],
                    created=parsed_data["results"][i]["created"]
                )


if __name__ == '__main__':
    si = StrashipsImporter()
    si.read_process_data()
