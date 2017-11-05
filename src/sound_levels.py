class SoundLevels():
    LOUDEST_DECIBEL = 130
    SOFTEST_DECIBEL = 40
    ALARM_CLOCK = 70
    GAS_LAWNMOWER = 106
    def get_sound_levels(self, decibels):
        if decibels > self.LOUDEST_DECIBEL:
            return "Your sound is louder than a jackhammer."
        elif decibels < self.SOFTEST_DECIBEL:
            return "Your sound is softer than a quiet room."
        elif decibels == self.LOUDEST_DECIBEL:
            return "Your sound is as loud as a jackhammer."
        elif decibels == self.SOFTEST_DECIBEL:
            return "Your sound is as soft as a quiet room."
        elif decibels == self.ALARM_CLOCK:
            return "Your sound is as soft as an alarm clock."
        elif decibels == self.GAS_LAWNMOWER:
            return "Your sound is as loud as a gas lawnmower."
        elif self.SOFTEST_DECIBEL < decibels < self.ALARM_CLOCK:
            return "Your sound is between a quiet room and alarm clock."
        elif self.ALARM_CLOCK < decibels < self.GAS_LAWNMOWER:
            return "Your sound is between an alarm clock and a gas lawnmower."
        else:
            return "Your sound is louder than a gas lawnmower and a jackhammer."

decibels = int(input("Enter amount of decibels: "))
given_decibels = SoundLevels()
print given_decibels.get_sound_levels(decibels)
