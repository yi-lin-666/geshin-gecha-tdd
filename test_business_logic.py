import pytest
def calculate_gacha_probability(pull_num):
    if pull_num <= 0:
        raise ValueError()
    if pull_num > 90:
        pull_num = pull_num - 90
    if pull_num <= 73:
        return 0.006
    elif pull_num == 90:
        return 1.0
    else:
        return 0.006 + (pull_num - 73) * 0.06

class TestGachaProbability:
    def test_base_probability(self):
        for i in range(1,74):
            assert calculate_gacha_probability(i) == 0.006
    def test_soft_pity(self):
        assert calculate_gacha_probability(74) == 0.066
    def test_hard_pity(self):
        assert calculate_gacha_probability(90) == 1.0
    def test_over_90(self):
        assert calculate_gacha_probability(91) == 0.006
    def test_invalid(self):
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)
