import unittest
from src.pipeline.data_loader import DataLoader
from src.pipeline.model import Model

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.data_loader = DataLoader()
        self.model = Model()

    def test_data_loading(self):
        images = self.data_loader.load_images('path/to/test/images')
        self.assertIsNotNone(images)
        self.assertGreater(len(images), 0)

    def test_model_inference(self):
        images = self.data_loader.load_images('path/to/test/images')
        outputs = self.model.generate_3d_models(images)
        self.assertIsNotNone(outputs)
        self.assertGreater(len(outputs), 0)

if __name__ == '__main__':
    unittest.main()