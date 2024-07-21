import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    dataPoints= [
      ("ABC", 120.48, 121.2, (120.48 + 121.2) / 2),
      ("DEF", 117.87, 121.68, (117.87 + 121.68) / 2)
    ]

    """ ------------ Add the assertion below ------------ """
    for i in range(len(quotes)):
      self.assertEqual(getDataPoint(quotes[i]), dataPoints[i])

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    results = [
      True,
      False
    ]
    """ ------------ Add the assertion below ------------ """
    for i in range(len(quotes)):
      self.assertEqual(quotes[i]['top_bid']['price'] > quotes[i]['top_ask']['price'], results[i])  

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_HandlesPrice2Is0(self):
    comparison = (1, 0)
    self.assertIsNone(getRatio(*comparison))

  def test_getRatio_calculateRatio(self):
    comparisons = [
      (0, 190),
      (100, 200),
    ]

    results = [
      0,
      100 / 200
    ]

    for i in range(len(comparisons)):
      self.assertEqual(getRatio(*comparisons[i]), results[i])




if __name__ == '__main__':
    unittest.main()
