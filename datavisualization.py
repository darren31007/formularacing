import matplotlib.pyplot as plt

#Scatter plot
def create_rpm_tps_scatter(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data["TPS"], data["RPM"], s=10, alpha=0.1)

    plt.title("Relationship Between Throttle Position and Engine RPM")
    plt.xlabel("Throttle Position (%)")
    plt.ylabel("Engine Speed (RPM)")
    plt.grid(True)
    #plt.show()
    #Save Graph
    plt.savefig("graphs/rpm_vs_tps_scatter.png")
    plt.close()


def create_rpm_timeline(data):
    plt.figure(figsize=(12,6))
    plt.plot(data["Elapsed Time (seconds)"], data["RPM"])

    plt.title("Engine RPM Over Time")
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("Engine Speed (RPM)")
    plt.grid(True)
    #plt.show()
    #Save Graph
    plt.savefig("graphs/rpm_over_time_line.png")
    plt.close()