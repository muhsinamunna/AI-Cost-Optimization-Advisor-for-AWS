import json

def generate_report(ec2_analysis, unused_volumes, ai_recommendations):
    """
    Generate a simple cost optimization report
    """

    report = {
        "EC2 Analysis": ec2_analysis,
        "Unused EBS Volumes": unused_volumes,
        "AI Recommendations": ai_recommendations
    }

    print("\n===== AWS Cost Optimization Report =====\n")

    print("EC2 Instances Analysis:")
    for item in ec2_analysis:
        print(f"Instance ID: {item['instance_id']}")
        print(f"Instance Type: {item['instance_type']}")
        print(f"Average CPU: {item['average_cpu']}%")
        print(f"Recommendation: {item['recommendation']}")
        print("-----------------------------------")

    print("\nUnused EBS Volumes:")
    for vol in unused_volumes:
        print(f"Volume ID: {vol} → Recommended action: Delete")

    print("\nAI Recommendations:")
    for rec in ai_recommendations:
        print(rec)
        print("-----------------------------------")

    return report


def save_report_to_file(report, filename="cost_report.json"):
    """
    Save report to JSON file
    """
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\nReport saved to {filename}")