import boto3

# Initialize AWS clients
ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")


def get_ec2_instances():
    """
    Fetch all EC2 instances
    """
    instances = []

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "InstanceId": instance["InstanceId"],
                "InstanceType": instance["InstanceType"],
                "State": instance["State"]["Name"]
            })

    return instances


def get_cpu_utilization(instance_id, start_time, end_time):
    """
    Get CPU utilization from CloudWatch
    """

    metrics = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,
        Statistics=["Average"]
    )

    datapoints = metrics["Datapoints"]

    cpu_values = [point["Average"] for point in datapoints]

    return cpu_values


def get_ebs_volumes():
    """
    Get all EBS volumes
    """

    volumes = []

    response = ec2.describe_volumes()

    for vol in response["Volumes"]:
        volumes.append({
            "VolumeId": vol["VolumeId"],
            "State": vol["State"],
            "Size": vol["Size"]
        })

    return volumes