import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'areas': ['area', 'parent'], 'population': ['period', 'version', 'person', 'area', 'groups', 'internal', 'public'], 'progress': ['period', 'version', 'person', 'state', 'verified'], 'jurisdictions': ['staff', 'area', 'start', 'end'], 'catalog': ['cell', 'area', 'groups', 'status', 'sensitive', 'structural_zero'], 'policies': ['period', 'audience', 'minimum_values', 'population_upper_bound'], 'links': ['period', 'before', 'after', 'area', 'changed_at_most'], 'released': ['bulletin', 'audience', 'period', 'version', 'cell', 'count', 'at'], 'proposal': ['id', 'audience', 'period', 'version', 'cell', 'alternate', 'presentation']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
