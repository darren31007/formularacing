import matplotlib.pyplot as plt


def create_rpm_tps_scatter(data):
    plt.figure(figsize=(10, 6))

    plt.scatter(data["TPS"], data["RPM"], s=10, alpha=0.1)

    plt.title("Relationship Between Throttle Position and Engine RPM")
    plt.xlabel("Throttle Position (%)")
    plt.ylabel("Engine Speed (RPM)")
    plt.show()
    plt.grid(True)
    plt.tight_layout()