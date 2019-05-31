import sys
import os
import unittest
from maggma.stores import Store, JSONStore, MemoryStore
from maggma.runner import Runner
from emmet.materials.visualization import VisualizationBuilder

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

        crit = {'task_id': 'mp-779001'}
        doc = list(self.visualization.query(criteria=crit))[0]

        self.assertIn('scene', doc)
        scene = doc['scene']
        self.assertIsInstance(scene, dict)
        self.assertTrue(len(scene['contents']) > 0)

        self.assertIn('legend', doc)
        legend = doc['legend']
        self.assertIn('composition', legend)
        leg_comp = legend['composition']
        self.assertIsInstance(leg_comp, dict)

        self.assertIn('colors', legend)
        leg_colors = legend['colors']
        self.assertIsInstance(leg_colors, dict)

        self.assertIn('settings', doc)
        expected_settings_keys = [
            "bonding_strategy",
            "bonding_strategy_kwargs",
            "color_scheme",
            "color_scale",
            "radius_strategy",
            "draw_image_atoms",
            "bonded_sites_outside_unit_cell",
            "hide_incomplete_bonds",
        ]
        test_instance_settings = doc['settings']
        self.assertIsInstance(test_instance_settings, dict)
        for k in expected_settings_keys:
            self.assertIn(k, test_instance_settings)

        self.assertIn('source', doc)
        source = doc['source']
        self.assertIsInstance(source, dict)


if __name__ == "__main__":
    unittest.main()
