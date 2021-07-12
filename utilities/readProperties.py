import xml.etree.ElementTree as et
config = et.parse("Configurations/config.xml").getroot()


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.find("section/url").text
        return url
