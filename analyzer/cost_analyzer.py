import statistics

def analyze_ec2_usage(instance_id, cpu_metrics, instance_type):
    """
    Analyze CPU utilization for an EC2 instance and recommend optimization.
    """

    if not cpu_metrics:
        return {
            "instance_id": instance_id,
            "status": "No metrics available",
            "recommendation": "Unable to analyze"
        }

    avg_cpu = statistics.mean(cpu_metrics)

    if avg_cpu < 10:
        recommendation = "Instance underutilized. Consider downsizing instance type."
    elif avg_cpu > 80:
        recommendation = "Instance highly utilized. Consider scaling up."
    else:
        recommendation = "Instance utilization is normal."

    return {
        "instance_id": instance_id,
        "instance_type": instance_type,
        "average_cpu": round(avg_cpu, 2),
        "recommendation": recommendation
    }


def analyze_ebs_volumes(volumes):
    """
    Detect unattached EBS volumes.
    """
    unused_volumes = []

    for vol in volumes:
        if vol['State'] == "available":
            unused_volumes.append(vol['VolumeId'])

    return unused_volumes