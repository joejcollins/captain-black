
""" Thinking about reversing strings.  """
# The task needs to run for a long time
import flask
import flasgger.utils as swag_utils
import api.text_apidocs as apidocs
# import data.text as data_text

endpoints = flask.Blueprint("auth", __name__, url_prefix="/text/")

@endpoints.route('/reverse/fast/<string_to_reverse>', methods=['GET', 'POST'])
@swag_utils.swag_from(apidocs.REVERSE)
def reverse(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = "shit"# data_text.reverse_text(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return flask.jsonify(message)
