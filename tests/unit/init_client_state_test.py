from h2o_wave.core import Expando

from app.main import init_client_state


# test init() method
def test_init():
    # Given
    client_state = Expando()
    # When
    init_client_state(client_state)
    # Then
    assert client_state.initialized
    assert client_state.number == 0
