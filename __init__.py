from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import extract_number

class FerengiRules(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rules.ferengi.intent')
    def handle_rules_ferengi(self, message):
        spoken_number = message.data.get('number')
        number = extract_number(spoken_number, ordinals=True)
        rules = self.translate_list('rules_of_acquisition')
        if (number - 1) > len(rules):
            self.speak_dialog("No such rule. There are only " + len(rules) + " rules")
            return

        self.speak_dialog(rules[number - 1])


def create_skill():
    return FerengiRules()

