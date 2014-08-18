import json, os

files = [f for f in os.listdir('.') if os.path.isfile(f) and '.json' in f ]

print files

for f in files:
  s = open(f, 'r')
  x = s.read()
  data = eval(x)
  s.close()
  print data

  if data['speaker_party'] == "D":
    os.rename(f, 'D/' + f)
  elif data['speaker_party'] == "R":
    os.rename(f, 'R/' + f)
  else:
    os.rename(f, 'O/' + f)
