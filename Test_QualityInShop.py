

from QualityInShop import Product
from QualityInShop import recalculate_quality

potato = Product("potato", 18)
cheese = Product("cheese", 23)
carrot = Product("carrot", 3)
water = Product("water", 20)

def test_recalculate_quality_cheese():
    recalculate_quality(cheese)
    assert cheese.quality == 21
    
def test_recalculate_quality_potato():
    recalculate_quality(potato)
    assert potato.quality == 17.5
    
def test_reclaculate_quality_carrot():
    recalculate_quality(carrot)
    assert carrot.quality == 3
    
def test_recalculate_quality_water():
    recalculate_quality(water)
    assert water.quality == 17