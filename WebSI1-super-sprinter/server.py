from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
data = data_handler.data_dict
headers = data_handler.DATA_HEADER


@app.route('/')
def main_page():
    data = data_handler.data_dict



    return render_template('mainpage.html', data=data, headers=headers)



@app.route('/story', methods=['GET','POST'])
def route_story():
    user_stories = data_handler.get_all_user_story()
    actual_story = {}

    if request.method == 'POST':
        actual_story['id'] = data_handler.make_id(data)

        for i in range(1,6):
            actual_story[headers[i]] = request.form[headers[i]]
        actual_story['status'] = data_handler.STATUSES[0]

        data.append(actual_story)

        tosave = data_handler.make_list(data)
        data_handler.write_table_to_file(data_handler.DATA_FILE_PATH,tosave)
        actual_story = {}
        return redirect('/')


    return render_template('story.html', user_stories=user_stories)

@app.route('/story/<id>')
def story_id(id):
    pass

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
