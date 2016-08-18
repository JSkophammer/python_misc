import xml.etree.ElementTree as ET
from music_anlyz import note_2_num
import matplotlib.pyplot as plt

notes = []
xml = 'canon_15.xml'
fpath = 'bach_xml/' + xml

tree = ET.parse(fpath)
extract = tree.findall('.//note')

for node in extract:
    try:
        tone = node.find('pitch').find('step').text
        octv = node.find('pitch').find('octave').text
        lgth = node.find('duration').text
        ltyp = node.find('type').text
        note = tone + octv
    except:
        continue
    notes.append((note, int(lgth), ltyp))

notexy = [(i+1, float(note_2_num([notes[i][0]])[0])) for i in range(len(notes))]
notex = [n[0] for n in notexy]
notey = [n[1] for n in notexy]

print(notexy)

#plt.figure(figsize=(18, 4), dpi=80)
#plt.scatter(notex, notey)
#plt.show()

