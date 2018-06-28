from flask import (Flask, session,
                   render_template, url_for, redirect, request, jsonify)
import os
import json
import random

app = Flask(__name__)


# Routes
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')


@app.route("/generate_groups", methods=["POST", "GET"])
def generate_groups():
    if request.method == "GET":
        return redirect(url_for('index'))
    participant_list = json.loads(request.form['list_of_names'])
    number_per_group = int(request.form['number_per_group'])
    # processed_list = process_list(participant_list, number_per_group)
    # print(process_list(participant_list, number_per_group))
    # print(group(final_list,5))
    return jsonify(process_list(participant_list, number_per_group))


# The process_list function accepts a list of participants and a group size
# as arguments that are passed from the client.  A blank array
# that will eventually be returned by that function is declared, and
# the participant list is deduped and shuffled.  The function iterates over a
# range of numbers that starts with 0, ends with the length of the participant
# list, and steps in the size of the group. Each iteration adds a new
# individual group to the groups list, by slicing the original list
# from the i in range to the sum of i + the group size.  The groups list
# is returned.

def process_list(participant_list, group_size):
    groups = []
    new_list = list(set(participant_list))  # Remove duplicates
    random.shuffle(new_list)
    for i in range(0, len(new_list), group_size):
        groups.append(new_list[i:i+group_size])
    return groups


if __name__ == '__main__':
    app.run(debug=True)
