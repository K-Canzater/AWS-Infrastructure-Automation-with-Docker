import boto3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ec2_client = boto3.client('ec2', region_name= 'us-east-1')

def stop_instances(instance_ids):
    try:
        response = ec2_client.stop_instances(InstanceIds=instance_ids)
        for instance in response['StoppingInstances']:
            instance_id = instance.get("InstanceId", 'ID Unknown')
            current_state = instance.get("CurrentState", {}).get("Name", 'State Unknown')
            logger.info(f"Instance ID: {instance_id} | Current State: {current_state}")
    except Exception as e:
        logger.error(f"FAILED TO STOP INSTANCE: {e}")

if __name__ == "__main__":
    ids_str = os.getenv("INSTANCE_IDS")  # Example: "i-02e535df52e47f346,i-0abc123456def7890"
    if not ids_str:
        logger.error("No INSTANCE_IDS provided. Set the environment variable.")
    else:
        instance_ids = [x.strip() for x in ids_str.split(",")]
        stop_instances(instance_ids)
