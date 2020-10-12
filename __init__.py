from mycroft import MycroftSkill, intent_file_handler


class FerengiRules(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rules.ferengi.intent')
    def handle_rules_ferengi(self, message):
        self.speak_dialog('rules.ferengi')


def create_skill():
    return FerengiRules()

