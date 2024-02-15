# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
from itemadapter import ItemAdapter


class FormatValuesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Format monetary values
        monetary_keys = ("price_excl_tax", "price_incl_tax", "tax")
        for key in monetary_keys:
            adapter[key] = self.format_money(adapter[key])
            
        # Format rating
        adapter["rating"] = self.format_rating(adapter["rating"])
        
        # Format description
        adapter["description"] = self.format_description(adapter["description"])
        
        # Format availability
        adapter["availability"] = self.format_availability(adapter["availability"])
        
        # Format image
        adapter["image"] = self.format_image_url(adapter["image"])
        
        return item
        
                    
    def format_image_url(self, value):
        formatted_value = re.sub(r"\.\./", "", value)
        
        return f"https://books.toscrape.com/{formatted_value}"


    def format_rating(self, value):
        return {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }[value]


    def format_money(self, value):
        return float(value[1:])


    def format_description(self, value):
        if isinstance(value, str):
            return value.replace("...more", "").strip() 
        
        return value


    def format_availability(self, value):
        return int(re.sub(r"\D", "", value) or 0)
