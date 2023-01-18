""" Test the endpoint. """
import flask
import pytest
import flask_api_v1.flask_app as flask_app
import flask_api_v1.text as text
# pylint: disable=protected-access


@pytest.fixture()
def app():
    """ Create a test fixture Flask application. """
    return flask_app.api


def test_reverse_fast() -> None:
    """ Check the message contents. """
    string_to_reverse = "zxcvbn"
    message = text._reverse_fast(string_to_reverse)
    assert len(message) == 2
    assert message['original'] == string_to_reverse
    assert message['reversed'] == 'nbvcxz'


def test_reverse_fast_get(client) -> None:
    """ Reverse a string with GET. """
    string_to_reverse = "qwerty"
    url = flask.url_for("text_api.reverse_fast_get",
                        string_to_reverse=string_to_reverse)
    response = client.get(url)
    # There were only 8 tags in use at the time of the recording.
    message = response.json
    assert len(message) == 2
    assert message['original'] == string_to_reverse
    assert message['reversed'] == 'ytrewq'


def test_reverse_fast_post(client) -> None:
    """ Reverse a string with POST. """
    string_to_reverse = "asdfgh"
    url = flask.url_for("text_api.reverse_fast_post")
    post_message = {
        'string_to_reverse': string_to_reverse
    }
    response = client.post(url, json=post_message)
    message = response.json
    assert len(message) == 2
    assert message['original'] == string_to_reverse
    assert message['reversed'] == 'hgfdsa'