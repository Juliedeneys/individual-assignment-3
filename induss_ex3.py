

from flask import Flask, jsonify


phonebook = {"Julie":"68636",
            "Thibault":"67886",
            "Zineb":"12357",
            "Edem":"54367"
             }

server = Flask("MyPhonebook")

@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)

@server.route("/addcontact/<name>/<phone_number>")
def add_contact(name,phone_number):
    new_contact = {name:phone_number}
    phonebook.update(new_contact)
    return jsonify(phonebook)

@server.route("/removecontact/<name>")
def remove_contact(name):
    phonebook.pop(name)
    return jsonify("Your contact has been deleted!")

@server.route("/updatecontact/<name>/<phone>")
def update_contact(name,phone):
    phonebook [name] = phone
    return jsonify("Your contact has been updated!")

@server.route("showphone/<name>")
def show_contact(name):
    contact = phonebook[name]
    return jsonify(contact)

server.run()