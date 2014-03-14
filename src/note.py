
class Note(object):
    """
    This class represents a note found in, or to be written to a midi file.
    """

#the note class should be defined by two midichannel events.
# 1) the note on event
# 2) the note off event for that same pitch value.
#this will allow for the calculation of note name, and rhythmic value

    #a note has pitch, rhythmic value (quarternote etc) and place in measure

    def __init__(self, pitchdata, time_between_on_and_off):

        self.pitch = pitchdata
        self.rhythmicvalue = time_between_on_and_off
        

