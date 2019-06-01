import sys
import os
import unittest
from maggma.stores import Store, JSONStore, MemoryStore
from maggma.runner import Runner
from emmet.materials.visualization import VisualizationBuilder
from emmet.materials.structure_visualization import StructureVisualization

__author__ = "Tyler Huntington"
__email__ = "tylerhuntington222@lbl.gov"

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
test_mats = os.path.join(
    module_dir, "..", "..", "..", "test_files",
    "visualization_test.json"
)


class TestVisualizationBuilder(unittest.TestCase):

    def setUp(self):

        self.materials = JSONStore(test_mats)
        self.visualization = MemoryStore("visualization")

    def test_build(self):

        builder = VisualizationBuilder(self.materials, self.visualization)
        runner = Runner([builder])
        runner.run()

        # use StuctureVisualization for schema validation of built data
        for doc in self.visualization.query():
            StructureVisualization(**doc)


if __name__ == "__main__":
    unittest.main()
