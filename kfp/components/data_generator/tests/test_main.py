from src import data_generator
from io import StringIO

import numpy as np
import pytest


class TestFetchDataset:
    def test_fetch_dataset_from_right_formatted_data(self):
        source = StringIO(
            "species,culmen_length_mm,culmen_depth_mm,flipper_length_mm,body_mass_g\n"
            "0,0.2545454545454545,0.6666666666666666,0.15254237288135594,0.2916666666666667"
        )
        actual = data_generator.fetch_dataset(source)
        assert actual.dtype.names == (
            "species",
            "culmen_length_mm",
            "culmen_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        )
        assert actual["species"].dtype == np.int64
        assert actual["culmen_length_mm"].dtype == np.float64

    def test_fetch_dataset_fails_file_without_header(self):
        source = StringIO(
            "0,1\n"
            "0,1"
        )
        with pytest.raises(IndexError):
            data_generator.fetch_dataset(source)
