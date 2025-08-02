import pytest

@pytest.mark.simulacao      # Posso criar marcadoresn (TAGS)
class  TestSimulacao():

    @pytest.mark.simulacao
    def test_simulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skid
    def test_simulacao_2(self):
        assert 1 == 2