from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import extract_number


class FerengiRules(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rules.ferengi.intent')
    def handle_rules_ferengi(self, message):
        spoken_number = message.data.get('number')
        number = extract_number(spoken_number, ordinals=True)
        self.log.info("DEBUG: number")
        self.log.info(number)
        rules = self.translate_list('rules_of_acquisition')
        self.log.info("DEBUG: rule")
        self.log.info(rules[number -1])
        self.speak_dialog(rules[number - 1])

def create_skill():
    return FerengiRules()

