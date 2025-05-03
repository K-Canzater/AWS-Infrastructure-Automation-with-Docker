import boto3
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create EC2 client
ec2_client = boto3.client("ec2")


def start_instances(instance_ids):
    try:
        response = ec2_client.start_instances(InstanceIds=instance_ids)

        for instance in response["StartingInstances"]:
            instance_id = instance.get("InstanceId", "Unknown")
            current_state = instance.get("CurrentState", {}).get("Name", "Unknown")

            logger.info(
                f"Started instance {instance_id} — Current state: {current_state}"
            )
    except Exception as e:
        logger.error(f"FAILED TO START INSTANCE: {e}")


if __name__ == "__main__":
    ids_env = os.environ.get("INSTANCE_IDS")

    if not ids_env:
        logger.error("No INSTANCE_IDS environment variable set.")
        exit(1)

    instance_ids = [i.strip() for i in ids_env.split(",") if i.strip()]
    start_instances(instance_ids)
