flatten = lambda l: [item for sublist in l for item in sublist]

def n_terminal_split(cutoff, sequence_array):
  #corte antes del aminoacido
  new_seq_array = []
  for i in sequence_array:
    new_seq = i.split(cutoff)
    #print(new_seq)
    for k in range(1, len(new_seq)):
      new_seq[k] = cutoff  + new_seq[k]
    new_seq_array.append(new_seq)
  new_sequence_array = flatten(new_seq_array)
  return new_sequence_array

def c_terminal_split(cutoff, sequence_array):
  #corte despues del aminoacido
  new_seq_array = []
  for i in sequence_array:
    new_seq = i.split(cutoff)
    #print(new_seq)
    for k in range(0, len(new_seq)-1):
      new_seq[k] = new_seq[k] + cutoff
    new_seq_array.append(new_seq)
  new_sequence_array = flatten(new_seq_array)
  return new_sequence_array

def protease_split(protease, sequence):
  protease_dict = [
    {
      "protease": "Tripsina",
      "cutoff": ["K", "R"],
      "type": "C"
    },
    {
      "protease": "Elastasa",
      "cutoff": ["V", "A"],
      "type": "C"
    },
    {
      "protease": "Proteinasa-K",
      "cutoff": ["A","E","F","I","L","T","V","W", "Y"],
      "type": "C"
    },
    {
      "protease": "ArgC",
      "cutoff": ["R"],
      "type": "C"
    },
    {
      "protease": "AspN",
      "cutoff": ["D"],
      "type": "N"
    },
    {
      "protease": "Quimiotripsina",
      "cutoff": ["F", "L", "Y", "W", "M"],
      "type": "C"
    },
    {
      "protease": "GluC",
      "cutoff": ["D"],
      "type": "C"
    },
    {
      "protease": "LysC",
      "cutoff": ["K"],
      "type": "C"
    },
    {
      "protease": "LysN",
      "cutoff": ["K"],
      "type": "N"
    },
  ]
  prot_type = False
  prot_cutoff = False
  for i in protease_dict:
    if i["protease"] == protease:
      prot_type = i["type"]
      prot_cutoff = i["cutoff"]
  sequence_array = [sequence]
  for cutoff in prot_cutoff:
    if prot_type == "N":
      sequence_array = n_terminal_split(cutoff, sequence_array)
    elif prot_type == "C":
      sequence_array = c_terminal_split(cutoff, sequence_array)
  return sequence_array
