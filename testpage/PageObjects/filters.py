from robot.libraries.BuiltIn import BuiltIn

locators = {
    'Procedures': {
        'buttonFilter': 'xpath=//*[@class="svg-rendered icon-toolbar svg-icon-tb_filter"]',
        'fieldName': 'xpath=//div[@class="form-group"]//input[contains(@placeholder,"Name")]',
        'selectorType': 'xpath=//div[./label[text()="Type"]]//select[@data-element="filter_control"]',
        'selectorStatus': 'xpath=',
        'selectorContentType': 'xpath=',
        'fieldCreatedBy': 'xpath=',
        'calendarCreatedStart': 'xpath=',
        'calendarCreatedEnd': 'xpath=',
        'fieldLastModifiedBy': 'xpath=',
        'calendarUpdatedAtStart': 'xpath=',
        'calendarUpdatedAtEnd': 'xpath=',
        'fieldDescription': 'xpath=',
        'fieldScript': 'xpath=',
        'buttonApply': 'xpath=//input[@class="btn btn-primary apply-grid-filter"]'
    },
    'Profiles': {
        'buttonFilter': 'xpath=',
        'checkBoxAndroid': 'xpath=',
        'checkBoxIOS': 'xpath=',
        'checkBoxWindows': 'xpath=',
        'checkBoxOSX': 'xpath=',
        'fieldName': 'xpath=',
        'fieldCreatedBy': 'xpath=',
        'fieldCreatedFrom': '',
        'fieldUpdatedAtFrom': '',
        'fieldUpdatedAtTo': '',
        'buttonApply': 'xpath=//input[@class="btn btn-primary apply-grid-filter"]'
    },
    'Alerts': {
        'buttonFilter': '',
        'fieldCreatedBy': '',
        'fieldLastModifiedBy': '',
        'calendarCreatedStart': '',
        'calendarCreatedEnd': '',
        'calendarUpdatedAtStart': '',
        'calendarUpdatedAtEnd': ''
    }
}


def _selenium():
    return BuiltIn().get_library_instance("Selenium2Library")


class Filters(object):
    def procedures_filter(self, page):
        _selenium().click_element(locators[page].get('buttonFilter'))

    def get_locators(self):
        return locators

