import pytest

from src.Webshop.shopping_cart import ShoppingCart
from src.Webshop.database import Database
from src.Webshop.item import Item


# 1. vi lägger till en item till en tom kundvagn
# 2. vi lägger till en ny item till en kundvagn som har andra saker
# 3. vi lägger till flera items av sa,,a sort till kundvagnen

@pytest.fixture
def seeds():
    return Item("blandade fröer", 25)

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def cart():
    return ShoppingCart()

@pytest.fixture
def db(mocker):
    mock_db = mocker.Mock(spec=Database)
    mock_db.add_item_to_cart.return_value = None
    return mock_db

@pytest.fixture
def cart(db):
    c = ShoppingCart()
    c.set_database(db)
    c.add_item("spade", 25)
    return c


def test_add_item_to_empty_cart(mocker, seeds, empty_cart):
        # Arrange
        mock_database = mocker.Mock(spec=Database)
        mock_database.add_item_to_cart.return_value = None
        empty_cart.set_database(mock_database)

        # Act
        empty_cart.add_item(seeds.name, seeds.price)

        # Assert
        mock_database.add_item_to_cart.assert_called_once()
        mock_database.add_item_to_cart.assert_called_with(seeds.name, seeds.price)



def test_add_item_to_cart(mocker, db, seeds, cart):
    cart.set_database(db)

    cart.add_item(seeds.name, seeds.price)

# Eftersom kundvagnen inte är tom, kommer add_item att ha enropats mer än en gång (exakt 2 gånger)
    # TODO: vi behöver ett sätt att se hur många saker som ligger i kundvagnen

    expected_call_count = 1 + 1

    actual_call_count = db.add_item_to_cart.call_count

    assert actual_call_count == expected_call_count
    db.add_item_to_cart.assert_called_with(seeds.name, seeds.price)

#"spade", 50
#"fröer", 25
#"fröer", 25

# Item-klass: name, price
# Hej