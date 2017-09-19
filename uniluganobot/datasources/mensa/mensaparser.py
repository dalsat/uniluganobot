from bs4 import BeautifulSoup


class MensaParser:

    parser = 'html.parser'


    def __init__(self, data: str):
        self.soup = BeautifulSoup(data, self.parser)


    def parse(self):
        return dict([self.parse_row(row) for row in self.soup.find('table').find_all('tr')])


    @classmethod
    def parse_row(cls, row):
        day, month = row.find_all('td')
        return (cls.parse_day(day), cls.parse_menu(month))


    @classmethod
    def parse_day(cls, day):
        return day.text.strip()


    @classmethod
    def parse_menu(cls, menu):
        ret_dict = {}
        section = None
        content = None

        for row in menu.text.strip().split('\n'):
            if row.startswith('\t'):
                assert section, 'no section found: %s' % section
                content.append(row.strip())
            else:
                if section:
                    ret_dict[section] = '\n'.join(content)
                section = row.strip()
                content = []
            ret_dict[section] = '\n'.join(content)
        return ret_dict
