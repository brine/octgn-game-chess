
pieces = {
"Black": {
"king": "0df50d0f-0400-4a11-ab7f-1b3afbed5daf",
"knight": "75cd0ccd-9d7a-4578-8646-c17196d6b54b",
"pawn": "b9d0646c-5a0d-4066-9bc1-77efb891a618",
"queen": "f4ef6fea-046f-42bf-921d-92ed72ac5b5f",
"rook": "ba598f95-f373-48ec-be3c-62035f845f39",
"bishop": "e73920a6-151d-4a1f-9087-99346e189781"
},
"White": {
"bishop": "71357430-5d2b-44a4-83a4-50d6eb15be91",
"king": "ecabdb34-22fc-462c-ada5-0d6b47b3ca0b",
"knight": "41391a2b-5aba-4f77-91f3-c7708b37f977",
"pawn": "95d43b3d-7269-4aba-9f29-a01a9733b5d1",
"queen": "c2c49386-8f57-4237-9f23-1478c2d5abbe",
"rook": "d1b7956d-d7fa-4a72-9b6c-201072c0954f"
}
}

playercolor = None

def gameSetup(group, x = 0, y = 0):
  mute()
  for card in table:
    notify("Cannot set up pieces: There are already pieces on the table.  Please reset the game and try again.")
    return
  global playercolor
  if playercolor == None:
    if table.isTwoSided():
      if me.hasInvertedTable():
        playercolor = "Black"
      else:
        playercolor = "White"
    else:
      if confirm("Will you be White?"):
        playercolor = "White"
      else:
        playercolor = "Black"
  if table.isTwoSided() and me.hasInvertedTable():
    pside = -1
  else:
    pside = 1
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) - 400, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) - 300, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) - 200, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) - 100, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50), pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) + 100, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) + 200, pside*200, 1)
  table.create(pieces[playercolor]["pawn"], (pside*-50 + 50) + 300, pside*200, 1)
  table.create(pieces[playercolor]["rook"], (pside*-50 + 50) - 400, pside*300, 1)
  table.create(pieces[playercolor]["rook"], (pside*-50 + 50) + 300, pside*300, 1)
  table.create(pieces[playercolor]["knight"], (pside*-50 + 50) - 300, pside*300, 1)
  table.create(pieces[playercolor]["knight"], (pside*-50 + 50) + 200, pside*300, 1)
  table.create(pieces[playercolor]["bishop"], (pside*-50 + 50) - 200, pside*300, 1)
  table.create(pieces[playercolor]["bishop"], (pside*-50 + 50) + 100, pside*300, 1)
  table.create(pieces[playercolor]["king"], (pside*-50 + 50), pside*300, 1)
  table.create(pieces[playercolor]["queen"], (pside*-50 + 50) - 100, pside*300, 1)
  notify("{} set up their pieces.".format(me))

def kill(card, x = 0, y = 0):
  mute()
  card.moveTo(shared.Discard)
  notify("{}'s {} has been captured.".format(me, card))

def promote(card, x = 0, y = 0):
  mute()
  global playercolor
  newcard, quantity = askCard({"Color": playercolor}, "And")
  if quantity == 0 or newcard == None: return
  x, y = card.position
  card.moveTo(shared.Discard)
  newcard = table.create(newcard, x, y, 1)
  newcard.moveToTable(x, y)
  whisper("{} promoted {} to {}.".format(me, card, newcard))

def create(group, x = 0, y = 0):
  mute()
  global playercolor
  newcard, quantity = askCard({"Color": playercolor}, "And")
  if quantity == 0 or newcard == None: return
  newcard = table.create(newcard, x, y, 1)
  notify("{} created a {}.".format(me, newcard))