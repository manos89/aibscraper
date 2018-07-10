import scrapy
from scrapy.loader import ItemLoader

from aibscrapr.items import aibitem


def get_urls():
    base_url="https://roi.aib.gov.uk/roi/Insolvency/Insolvency/Details/{ID}"
    return [base_url.replace("{ID}",str(i)) for i in range(1,10000)]




class QuotesSpider(scrapy.Spider):
    name = "aib"

    def start_requests(self):
        urls =  get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        CaseReference=response.css("p#Bo_CaseReference::text").extract_first()
        l = ItemLoader(item=aibitem(), response=response)
        l.add_css('case_reference', 'p#Bo_CaseReference::text')
        l.add_css('bnkrptc_type', 'p#Bo_BankruptcyType::text')
        l.add_css('first_name', 'p#Bo_Debtor_FirstName::text')
        l.add_css('surname', 'p#Bo_Debtor_Surname::text')
        l.add_css('other_names', 'p#Bo_Debtor_OtherNames::text')
        l.add_css('alias', 'p#Bo_Debtor_Alias::text')
        l.add_css('address1', 'p#Bo_Debtor_HomeAddress_AddressLine1::text')
        l.add_css('address2', 'p#Bo_Debtor_HomeAddress_AddressLine2::text')
        l.add_css('address3', 'p#Bo_Debtor_HomeAddress_AddressLine3::text')
        l.add_css('town', 'p#Bo_Debtor_HomeAddress_Town::text')
        l.add_css('county', 'p#Bo_Debtor_HomeAddress_County::text')
        l.add_css('postcode', 'p#Bo_Debtor_HomeAddress_Postcode::text')
        l.add_css('trading_address', 'p#Bo_Debtor_TradingName::text')
        l.add_css('trading_name', 'p#Bo_Debtor_TradingName::text')
        l.add_css('birth_date', 'p#Bo_Debtor_DateOfBirth::text')
        l.add_css('death_date', 'p#Bo_Debtor_DateOfDeath::text')
        l.add_css('occupation', 'p#Bo_Debtor_Occupation::text')
        l.add_css('seq_awarded', 'p#Bo_SequestrationAwardedBy::text')
        l.add_css('trustee_discharge_date', 'p#Bo_TrusteeDischargeDate::text')
        l.add_css('first_order_date', 'p#Bo_FirstOrderDate::text')
        l.add_css('trst_appointed', 'p#Bo_CurrentTrustee_DisplayDateAppointed::text')
        l.add_css('trst_name', 'p#Bo_CurrentTrustee_Name::text')
        l.add_css('trst_organisation', 'p#Bo_CurrentTrustee_OrganisationName::text')
        l.add_css('trst_address', 'p#Bo_CurrentTrustee_Address_FullAddressSingleLine::text')
        l.add_css('trst_phone', 'p#Bo_CurrentTrustee_PhoneNumber::text')
        l.add_css('trst_email', 'p#Bo_CurrentTrustee_EmailAddress::text')
        l.add_css('trst_discharge_date', 'p#Bo_DisplayTrusteeDischargeDate::text')
        return l.load_item()
