import os
import unittest
from maggma.stores import JSONStore, MemoryStore
from maggma.runner import Runner
from emmet.materials.visualization import VisualizationBuilder

__author__ = "Tyler Huntington"
__email__ = "tylerhuntington222@lbl.gov"

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
test_mats = os.path.join(
    module_dir, "..", "..", "..", "test_files",
    "visualization_mats_sample.json"
)


class TestVisualizationBuilder(unittest.TestCase):

    def setUp(self):

        self.materials = JSONStore(test_mats)
        self.visualization = MemoryStore("visualization")

    def test_build(self):

        builder = VisualizationBuilder(self.materials, self.visualization)
        runner = Runner([builder])
        runner.run()

        crit = {'task_id': 'mp-8042'}
        doc = list(self.visualization.query(criteria=crit))[0]

        self.assertTrue('scene' in doc)


if __name__ == "__main__":
    unittest.main()