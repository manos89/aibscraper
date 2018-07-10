# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class aibitem(scrapy.Item):
    # define the fields for your item here like:
    case_reference = scrapy.Field()
    bnkrptc_type=scrapy.Field()
    first_name=scrapy.Field()
    surname=scrapy.Field()
    other_names=scrapy.Field()
    alias=scrapy.Field()
    address1=scrapy.Field()
    address2=scrapy.Field()
    address3=scrapy.Field()
    town=scrapy.Field()
    county=scrapy.Field()
    postcode=scrapy.Field()
    trading_address=scrapy.Field()
    trading_name=scrapy.Field()
    birth_date=scrapy.Field()
    death_date=scrapy.Field()
    occupation=scrapy.Field()
    seq_awarded=scrapy.Field()
    trustee_discharge_date=scrapy.Field()
    first_order_date=scrapy.Field()
    trst_appointed=scrapy.Field()
    trst_name=scrapy.Field()
    trst_organisation=scrapy.Field()
    trst_address=scrapy.Field()
    trst_phone=scrapy.Field()
    trst_email=scrapy.Field()
    trst_discharge_date=scrapy.Field()
