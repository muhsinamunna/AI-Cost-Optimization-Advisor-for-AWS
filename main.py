from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

from collector.aws_resource_collector import (
    get_ec2_instances,
    get_cpu_utilization,
    get_ebs_volumes
)

from analyzer.cost_analyzer import (
    analyze_ec2_usage,
    analyze_ebs_volumes
)

from ai_engine.recommendation_engine import generate_recommendation

from reports.report_generator import (
    generate_report,
    save_report_to_file
)


def main():

    ec2_analysis_results = []
    ai_recommendations = []

    # Time range for CPU metrics
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    print("Collecting AWS resources...")

    instances = get_ec2_instances()

    for instance in instances:

        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]

        cpu_metrics = get_cpu_utilization(instance_id, start_time, end_time)

        analysis = analyze_ec2_usage(instance_id, cpu_metrics, instance_type)

        ec2_analysis_results.append(analysis)

        ai_result = generate_recommendation(analysis)

        ai_recommendations.append(ai_result)

    # EBS analysis
    volumes = get_ebs_volumes()
    unused_volumes = analyze_ebs_volumes(volumes)

    # Generate report
    report = generate_report(ec2_analysis_results, unused_volumes, ai_recommendations)

    # Save report
    save_report_to_file(report)


if __name__ == "__main__":
    main()