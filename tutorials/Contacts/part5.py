# You don't need following 3 lines in your own applications.
import sys, os
sys.path.append("../../atlastk")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import atlastk, enum

class State(enum.Enum):
  DISPLAY = enum.auto()
  EDIT = enum.auto()

FIELDS = [
  "Name",
  "Address",
  "Phone",
  "Note"
]

EXAMPLE = [
  {
    "Name": "Holmes, Sherlock",
    "Address": "221B Baker Street, Londres",
    "Phone": "(use telegraph)",
    "Note": "Great detective!"
  },
  {
    "Name": "Holmes, Mycroft",
    "Address": "Diogenes Club, Pall Mall, Londres",
    "Phone": "(use telegraph)",
    "Note": "Works for the British government.\nBrother of Holmes, Sherlock."
  },
  {
    "Name": "Tintin",
    "Address": "Château de Moulinsart",
    "Phone": "421",
    "Note": "Has a dog named Snowy."
  },
  {
    "Name": "Tournesol, Tryphon (prof.)",
    "Address": "Château de Moulinsart",
    "Phone": "421",
    "Note": "Creator of the Bianca rose."
  }
]

EMPTY_CONTACT = {
  "Name": "",
  "Address": "",
  "Phone": "",
  "Note": ""
}

contacts = EXAMPLE


class Board:
  def __init__(self):
    self.state = State.DISPLAY


def display_contacts(dom):
  html = ""

  for contactId in range(len(contacts)):
    contact = contacts[contactId]
    html += f'<tr id="{contactId}" data-xdh-onevent="Select" style="cursor: pointer;">'
    for key in contact:
      html += f'<td>{contact[key]}</td>'
    html += '</td>'

  dom.inner("Content", html)


def display_contact(contactId,dom):
  dom.set_values(EMPTY_CONTACT if contactId == None else contacts[contactId])


def update_outfit(board,dom):
  if board.state == State.DISPLAY:
    dom.disable_elements(FIELDS)
    dom.disable_element("HideDisplay")
  elif board.state == State.EDIT:
    dom.enable_elements(FIELDS)
    dom.enable_element("HideDisplay")


def ac_connect(board,dom):
  dom.inner("",open("Main.html").read())
  display_contacts(dom)
  board.state = State.DISPLAY
  update_outfit(board,dom)


def ac_select(board,dom,id):
  display_contact(int(id),dom)  
  board.state = State.DISPLAY
  update_outfit(board,dom)


def ac_new(board,dom):
  board.state = State.EDIT
  display_contact(None,dom)
  update_outfit(board,dom)
  dom.focus("Name")


CALLBACKS = {
  "": ac_connect,
  "Select": ac_select,
  "New": ac_new
 }

atlastk.launch(CALLBACKS,Board,open("Head.html").read())