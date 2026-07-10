import unittest

from sintering_energy import calculate_energy_density


class CalculateEnergyDensityTests(unittest.TestCase):
    def test_calculates_expected_value(self) -> None:
        self.assertAlmostEqual(calculate_energy_density(100, 200, 0.5), 1.0)

    def test_rejects_negative_power(self) -> None:
        with self.assertRaises(ValueError):
            calculate_energy_density(-1, 200, 0.5)

    def test_rejects_nonpositive_scan_speed(self) -> None:
        with self.assertRaises(ValueError):
            calculate_energy_density(100, 0, 0.5)

    def test_rejects_nonpositive_spot_diameter(self) -> None:
        with self.assertRaises(ValueError):
            calculate_energy_density(100, 200, 0)


if __name__ == "__main__":
    unittest.main()
