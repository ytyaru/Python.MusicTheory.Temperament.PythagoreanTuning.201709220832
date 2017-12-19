import math
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.NoteNumber import NoteNumber
from MusicTheory.pitch.PitchClass import PitchClass
class EqualTemperament:
    def __init__(self, fundamentalTone=None):
        self.__fundamentalTone = fundamentalTone
        if None is fundamentalTone:
            self.__fundamentalTone = FundamentalTone()
    @property
    def FundamentalTone(self): return self.__fundamentalTone
    def GetFrequency(self, pitchClass, octaveClass):
        return self.FundamentalTone.Hz * math.pow(2, (NoteNumber.Get(pitchClass, octaveClass) - self.FundamentalTone.NoteNumber) / (PitchClass.Max + 1))

