"""Calculate laser energy density for sintering.

The calculator uses a simple engineering approximation:
energy density = power / (scan_speed * spot_diameter)

Units:
- power: W
- scan_speed: mm/s
- spot_diameter: mm
- result: J/mm^2
"""

from __future__ import annotations


def calculate_energy_density(power_w: float, scan_speed_mm_s: float, spot_diameter_mm: float) -> float:
    """Return laser energy density in J/mm^2.

    The formula assumes a simplified 2D estimate using the scan speed and
    spot diameter as the effective area term.
    """
    if scan_speed_mm_s <= 0:
        raise ValueError("scan_speed_mm_s must be greater than 0")
    if spot_diameter_mm <= 0:
        raise ValueError("spot_diameter_mm must be greater than 0")
    if power_w < 0:
        raise ValueError("power_w must not be negative")

    # Convert laser power into a per-area energy estimate.
    return power_w / (scan_speed_mm_s * spot_diameter_mm)


def main() -> None:
    power_w = float(input("输入激光功率(W): "))
    scan_speed_mm_s = float(input("输入扫描速度(mm/s): "))
    spot_diameter_mm = float(input("输入光斑直径(mm): "))

    energy_density = calculate_energy_density(
        power_w=power_w,
        scan_speed_mm_s=scan_speed_mm_s,
        spot_diameter_mm=spot_diameter_mm,
    )
    print(f"激光能量密度: {energy_density:.6f} J/mm²")


if __name__ == "__main__":
    main()
